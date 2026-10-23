from flask import Flask, render_template, request, redirect, url_for, flash, session
from biblioteca import *
from cliente import *
from agencia import *
from conta import *

app = Flask(__name__)
app.secret_key = "chavinho"  # para gerenciar sessões e mensagens flash/print
app.register_blueprint(agencia)
app.register_blueprint(op)

@app.route("/")
def index():
    # recupera o cliente logado na sessão
    cliente_logado = session.get("cliente_logado")
    
    # pega os dados atualizados do cliente logado
    conta_logada = None
    if cliente_logado:
        contas = acessar_contas()
        numconta = cliente_logado.get("numconta")
        conta_logada = contas.get(numconta)

    return render_template("index.html", cliente=cliente_logado, conta=conta_logada)


@app.route("/entrar", methods=["POST"])
def Entrar():
    cpf = cpf_com_pontinhos(request.form.get("cpf"))
    
    clientes = acessar_clientes()
    dados_cliente = clientes.get(cpf)

    #verifica se existe
    if dados_cliente is None:
        flash("Cliente não encontrado! É preciso efetuar cadastro.", "danger")
        return redirect(url_for("index"))
    else:
        #salva o cliente na sessão
        session["cliente_logado"] = dados_cliente
        flash("Login realizado com sucesso!", "success")
        return redirect(url_for("index"))


@app.route("/registrar", methods=["POST"])
def Registrar():
    nome = request.form.get("nome")
    cpf = cpf_com_pontinhos(request.form.get("cpf"))
    tipo = request.form.get("tipo")

    if ValidarCPF(cpf):
        AdicionarCliente(nome, cpf)

        # recupera cliente cadastrado
        clientes = acessar_clientes()
        cliente_logado = clientes.get(cpf)

        # cria a conta e adiciona no .json
        CriarConta(tipo, cliente_logado)

        #recarrega os dados novos
        clientes_atts = acessar_clientes()
        cliente = clientes_atts.get(cpf)

        #salva os novos
        session["cliente_logado"] = cliente.get(cpf)
        flash("Cadastro realizado com sucesso!", "success")
    else:
        flash("CPF inválido!", "danger")
        
    return redirect(url_for("index"))


@app.route("/sair")
def Sair():
    session.pop("cliente_logado", None)
    flash("Você saiu da conta.", "info")
    return redirect(url_for("index"))


if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    app.run(debug=True)