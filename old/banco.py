from flask import Flask, render_template, request, redirect, url_for, session
from biblioteca import *

app = Flask(__name__)
app.secret_key = 'chave_secreta_banco'  # Necessário para gerenciar a sessão do usuário

# Banco de dados simulado em memória (CPF como chave)
# Exemplo inicial: {"12345678900": {"nome": "Maria Silva", "saldo": 42584.17, "extrato": [...]}}

clientes = acessar_dados()

@app.route('/')
def index():
    return render_template('index.html', erro=request.args.get('erro'))

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome', '').strip()
    cpf = request.form.get('cpf', '').strip()

    if not nome or not cpf:
        return redirect(url_for('index', erro='Preencha Nome e CPF.'))

    # Verifica se a conta existe
    if cpf in clientes:
        session['cpf_logado'] = cpf
        return redirect(url_for('dashboard'))
    else:
        # Se não existir, redireciona informando que precisa cadastrar e informando o saldo inicial
        return render_template('index.html', erro='Conta não encontrada! Defina o saldo inicial abaixo para cadastrar.', modo_cadastro=True, nome=nome, cpf=cpf)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome', '').strip()
    cpf = request.form.get('cpf', '').strip()
    
    try:
        saldo_inicial = float(request.form.get('saldo_inicial', 0))
    except ValueError:
        saldo_inicial = 0.0

    if not nome or not cpf:
        return redirect(url_for('index', erro='Preencha Nome e CPF para o cadastro.'))

    if cpf in clientes:
        return redirect(url_for('index', erro='Este CPF já possui conta! Faça login.'))

    # Cria a nova conta
    clientes[cpf] = {
        'nome': nome,
        'saldo': saldo_inicial,
        'extrato': [{'tipo': 'Abertura de Conta', 'valor': saldo_inicial, 'data': 'Hoje'}] if saldo_inicial > 0 else []
    }

    salvar_dados(clientes)
    session['cpf_logado'] = cpf
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    cpf = session.get('cpf_logado')
    if not cpf or cpf not in clientes:
        return redirect(url_for('index'))
    
    conta = clientes[cpf]
    return render_template('dashboard.html', conta=conta)

@app.route('/transacao', methods=['POST'])
def transacao():
    cpf = session.get('cpf_logado')
    if not cpf or cpf not in clientes:
        return redirect(url_for('index'))

    tipo = request.form.get('tipo')
    try:
        valor = float(request.form.get('valor', 0))
    except ValueError:
        valor = 0

    conta = clientes[cpf]

    if valor <= 0:
        return redirect(url_for('dashboard'))

    if tipo == 'deposito':
        conta['saldo'] += valor
        conta['extrato'].insert(0, {'tipo': 'Deposit', 'valor': valor, 'data': 'Hoje'})
    elif tipo == 'saque':
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            conta['extrato'].insert(0, {'tipo': 'Withdrawal', 'valor': -valor, 'data': 'Hoje'})

    return redirect(url_for('dashboard'))

@app.route('/sair')
def sair():
    session.pop('cpf_logado', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    app.run(debug=True)