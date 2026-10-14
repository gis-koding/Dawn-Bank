from flask import Flask, render_template, request, redirect, url_for
from bibliotec import *

banco = Flask(__name__)

@banco.route('/')
def listag():
    """Página principal: exibe a lista de clientes cadastrados."""
    clientes = acessar_dados()
    return render_template('listag.html', clientes=clientes)

@banco.route('/registrar', methods=['POST'])
def registrar():
    """Recebe os dados do formulário e salva o novo cliente."""
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')

    # Cria o dicionário do novo cliente
    novo_cliente = {
        'nome': nome,
        'cpf': cpf,
    }

    # Carrega a lista atual, adiciona o novo cliente e salva no arquivo
    clientes = acessar_dados()
    clientes.append(novo_cliente)
    salvar_dados(clientes)

    # Redireciona para a página principal atualizada
    return redirect(url_for('listag'))

if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    banco.run(debug=True)