from flask import Flask, render_template, request, redirect, url_for, flash, session
from biblioteca import cpf_com_pontinhos
from agencia import agencia, agencia_unica
from cliente import Cliente

#agora o main só precisa do agencia unica
app = Flask(__name__)
app.secret_key = "chavinho"  # para gerenciar sessões e mensagens flash/print
app.register_blueprint(agencia)
#app.register_blueprint(op); não vamos mais usar
agencia_unica.carregar_json()


@app.route("/")
def index():
    # recupera o cliente logado na sessão
    cliente_logado = session.get("cliente_logado")
    
    # pega os dados atualizados do cliente logado
    conta_logada = None
    if cliente_logado:
        numconta = cliente_logado.get("numconta")
        conta_logada = agencia_unica.buscar_conta(numconta)

    return render_template("index.html", cliente=cliente_logado, conta=conta_logada)


@app.route("/entrar", methods=["POST"])
def Entrar():
    cpf = cpf_com_pontinhos(request.form.get("cpf"))
    cliente = agencia_unica.buscar_cliente(cpf)

    #verifica se existe
    if cliente is None:
        flash("Cliente não encontrado! É preciso efetuar cadastro.", "danger")
        return redirect(url_for("index"))
    else:
        #salva o cliente na sessão
        session["cliente_logado"] = cliente.to_dict() 
        flash("Login realizado com sucesso!", "success")
        return redirect(url_for("index"))


@app.route("/registrar", methods=["POST"])
def Registrar():
    nome = request.form.get("nome")
    cpf = cpf_com_pontinhos(request.form.get("cpf"))
    tipo = request.form.get("tipo")

    if agencia_unica.validar_cpf(cpf):
        novo_cliente = agencia_unica.adicionar_cliente(nome, cpf)
        # recupera cliente cadastrado
        if novo_cliente:
            agencia_unica.abrir_conta(novo_cliente, tipo)
            agencia_unica.salvar_json()
        
            #salva os novos
            session["cliente_logado"] = novo_cliente.to_dict()
            flash("Cadastro realizado com sucesso!", "success")
        else:
            # ALTEREI AQUI: Tratamento caso o CPF já exista no sistema (o adicionar_cliente retorna None se já existir).
            flash("Erro: Cliente já cadastrado.", "danger")
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