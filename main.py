from flask import Flask, render_template, request, redirect, url_for, flash, session
from biblioteca import cpf_com_pontinhos, decimal_ao_jeito_brasileiro
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


@app.route("/deposito", methods=["POST"])
def Deposito():
    cliente_logado = session.get("cliente_logado")
    if not cliente_logado:
        return redirect(url_for("index"))
    
    # Pega o valor que o usuário digitou no HTML e converte para número
    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))
    
    # Busca a conta do cliente na memória
    conta = agencia_unica.buscar_conta(cliente_logado.get("numconta"))
    
    if conta:
        conta.deposito(valor) # Chama o método da classe Conta
        agencia_unica.salvar_json() # Salva no arquivo JSON
        
    return redirect(url_for("index"))


@app.route("/saque", methods=["POST"])
def Saque():
    cliente_logado = session.get("cliente_logado")
    if not cliente_logado:
        return redirect(url_for("index"))
    
    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))
    conta = agencia_unica.buscar_conta(cliente_logado.get("numconta"))
    
    if conta:
        conta.saque(valor) # Chama o método da classe Conta
        agencia_unica.salvar_json()
        
    return redirect(url_for("index"))


@app.route("/pix", methods=["POST"])
def Pix():
    cliente_logado = session.get("cliente_logado")
    if not cliente_logado:
        return redirect(url_for("index"))
    
    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))
    cpf_destino = cpf_com_pontinhos(request.form.get("destino"))
    
    conta_origem = agencia_unica.buscar_conta(cliente_logado.get("numconta"))
    cliente_destino = agencia_unica.buscar_cliente(cpf_destino)
    
    # Verifica se a conta de origem existe e se o cliente destino tem conta
    if conta_origem and cliente_destino and cliente_destino.contas:
        conta_destino = cliente_destino.contas[0] # Pega a primeira conta do destino
        
        # Chama o método pix passando o valor e o OBJETO da conta destino
        conta_origem.pix(valor, conta_destino)
        agencia_unica.salvar_json()
    else:
        flash("Conta de destino não encontrada ou inválida.", "danger")
        
    return redirect(url_for("index"))

if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    app.run(debug=True)