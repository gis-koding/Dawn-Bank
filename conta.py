from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from agencia import *
from biblioteca import *

op = Blueprint('op', __name__)

#formato json: {"num da conta": {"titulares":---,"tipo":---,"saldo":---, "extrato":---} }

def CriarConta(tipo, cliente_logado):
    cpf = cliente_logado.get("cpf")
    # 6 ultimos dig do cpf
    numconta = int(cpf) // 100000

    #definindo o tipo de conta // agencia
    if tipo == "salario":
        numconta = "01" + f"{numconta}"
    elif tipo == "corrente":
        numconta = "02" + f"{numconta}"
    elif tipo == "poupança":
        numconta = "03" + f"{numconta}"

    #caso tenha 0 no cpf
    while len(str(numconta)) < 8:
        numconta = str(numconta) + "5"

    #N° da conta = agencia + 6 dig do cpf
    #adicionando os dados necessarios no json
    AdicionarConta(cpf, numconta, tipo)


def AdicionarConta(cpf, numconta, tipo):
    clientes = acessar_clientes()
    contas = acessar_contas()

    #pega os dados
    cliente = clientes.get(cpf)
    cliente["numconta"] = numconta
    clientes[cpf] = cliente
    salvar_clientes(clientes)

    #cria conta nova
    conta = {
        "titular": cpf,
        "numconta": numconta,
        "tipo": tipo,
        "saldo": 0.13
    }

    #salva os dados
    contas[numconta] = conta
    salvar_clientes(clientes)
    salvar_contas(contas)


#Seção: Operações


@op.route("/deposito", methods=["POST"])
def deposito():

    #verifica se esta logado
    if "cliente_logado" not in session:
        flash("Você precisa estar logado para realizar esta operação.", "warning")
        return redirect(url_for("index"))

    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))

    #verifica se o valor não é negativo
    if valor <= 0:
        flash("Valor inválido para depósito.", "danger")
        return redirect(url_for("index"))

    #pega os dados
    contas = acessar_contas()
    numconta = session["cliente_logado"].get("numconta")
    conta = contas.get(numconta)

    #faz a operacao e salva
    if conta:
        conta["saldo"] += valor
        contas[numconta] = conta
        salvar_contas(contas)
        flash(f"Depósito de R$ {valor:.2f} realizado com sucesso!", "success")
    else:
        flash("Conta não encontrada.", "danger")

    return redirect(url_for("index"))


@op.route("/saque", methods=["POST"])
def saque():
    # verifica login
    if "cliente_logado" not in session:
        flash("Você precisa estar logado para realizar esta operação.", "warning")
        return redirect(url_for("index"))

    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))

    # dados
    contas = acessar_contas()
    numconta = session["cliente_logado"].get("numconta")
    conta = contas.get(numconta)

    # verifica a conta na lista
    if not conta:
        flash("Conta não encontrada.", "danger")
        return redirect(url_for("index"))

    #verifica se o valor e o saque é valido
    if valor > conta.get("saldo") or valor <= 0:
        flash("Saldo insuficiente ou valor inválido para saque.", "danger")
    else:
        #diminui e aumenta saldo; salva
        conta["saldo"] -= valor
        contas[numconta] = conta
        salvar_contas(contas)
        flash(f"Saque de  R$ {valor:.2f} realizado com sucesso!", "success")

    return redirect(url_for("index"))


@op.route("/pix", methods=["POST"])
def pix():
    if "cliente_logado" not in session:
        flash("Você precisa estar logado para realizar esta operação.", "warning")
        return redirect(url_for("index"))

    destino = request.form.get("destino")
    valor = decimal_ao_jeito_brasileiro(request.form.get("valor"))

    #verifica se o cpf é válido
    if not ValidarCPF(destino):
        flash("CPF de destino inválido.", "danger")
        return redirect(url_for("index"))

    clientes = acessar_clientes()
    contas = acessar_contas()

    #pega o saldo do cliente 
    cliente = session["cliente_logado"]
    conta = contas.get(cliente.get("numconta"))

    #pega os dados do cliente d destino
    cliente_destino = clientes.get(destino)

    if not cliente_destino:
        flash("Cliente de destino não encontrado.", "danger")
        return redirect(url_for("index"))

    numconta_destino = cliente_destino.get("numconta")
    conta_destino = contas.get(numconta_destino)

    #verifica se saldo disponível
    if conta.get("saldo") < valor:
        flash("Saldo insuficiente para transferência.", "danger")
        return redirect(url_for("index"))

    #transfere
    conta["saldo"] -= valor
    conta_destino["saldo"] += valor

    #salva
    contas[cliente.get("numconta")] = conta
    contas[numconta_destino] = conta_destino
    salvar_contas(contas)

    flash(f"Pix de R$ {valor:.2f} enviado com sucesso para {cliente_destino.get('nome', destino)}!", "success")
    return redirect(url_for("index"))