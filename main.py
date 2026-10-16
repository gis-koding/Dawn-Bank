from flask import Flask, render_template, request, redirect, url_for
from biblioteca import *

banco = Flask(__name__)


#funções para rodar o html

@banco.route('/')
def listagem():
    # Página principal: exibe a lista de clientes cadastrados.
    clientes = acessar_dados()
    return render_template('site.html', clientes=clientes)

@banco.route('/registrar', methods=['POST'])
def registrar():
    # Recebe os dados do html (formulário) e guarda nas variáveis python.
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    saldo = request.form.get('saldo',0)
                             
    saldo_float = decimal_ao_jeito_brasileiro(saldo)

    # Cria o dicionário do novo cliente
    novo_cliente = {
        'nome': nome,
        'cpf': cpf,
        'saldo': saldo_float
    }

    # Carrega a lista atual, adiciona o novo cliente e salva no arquivo json.
    clientes = acessar_dados()
    clientes.append(novo_cliente)
    salvar_dados(clientes)

    # Redireciona a lista para a página principal atualizada.
    return redirect(url_for('listagem'))

@banco.route('/deletar/<cpf>', methods=['POST'])
def deletar(cpf):
    """Remove um cliente existente buscando pelo CPF."""
    clientes = acessar_dados()
    # Mantém apenas os clientes cujo CPF seja diferente do informado
    clientes = [c for c in clientes if c.get('cpf') != cpf]
    salvar_dados(clientes)

    return redirect(url_for('listagem'))


if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    banco.run(debug=True)