from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from biblioteca import *

agencia = Blueprint('agencia', __name__)


#Seção: Cadastramento


def AdicionarCliente(nome,cpf):
    '''Adiciona cliente no banco de dados.'''

    clientes = acessar_clientes()
    if cpf in clientes:
        print("Cliente já cadastrado") #evita sobrescrever dados no dicionário
    else:
        clientes[cpf] = {'nome': nome, 'cpf': cpf}
        salvar_clientes(clientes)

#cadastroclientes direto no html

def ValidarCPF(cpf):
    '''Verifica se o cpf está no formato padrão.'''

    #formatação de cpf adicionada na biblioteca
    if len(cpf) != 11 or not cpf.isdigit():
        return False #não permitido
    #se for permitido, hora de verificar os dígitos
    digitos = []
    for numero in cpf: 
        digitos.append(int(numero))  #coloco os digitos cpf numa lista
    
    tudo_igual = True #flag, para mudar no for
    for inteiro in digitos:
        if digitos[0] != inteiro: 
            tudo_igual = False #checo se tem digitos diferentes; 
    if tudo_igual: 
        return False #não é válido !
    #primeira verificação, digito1
    soma = 0 
    peso = 10 #faz parte da soma, é 10 e decresce;
    for i in range(0,9): #do 1 ao 9
        soma += digitos[i] * peso
        peso -= 1 #para decrescer o 10
    resto1 = soma % 11 #mesma etapa 
    if resto1 < 2:
        digito1 = 0 #primeiro digito verificador
    else:
        digito1 = 11 - resto1
    
    #segunda verificação, para digito2
    soma2 = 0
    peso2 = 11
    for a in range(0,10):
        soma2 += digitos[a] * peso2
        peso2 -= 1
    resto2 = soma2 % 11 
    if resto2 < 2:
        digito2 = 0 #segundo digito verificador
    else:
        digito2 = 11 - resto2
                
    if digito1 == digitos[9] and digito2 == digitos[10]: #digito 10 e 11
        return True #é válido
    else:
        return False #não é válido


#Seção: Listagem


def lista_de_agencias(): #etapa4
    '''Verifica as agências existentes. Sem cliente, sem agência.'''
    contas = acessar_contas()
    return sorted({conta[:2] for conta in contas})


@agencia.route("/excluir_cliente", methods=["POST"])
def excluir_cliente():
    # dados do cliente
    cpf = request.form.get("cpf")
    clientes = acessar_clientes()
    contas = acessar_contas()
    
    # verifica se o cliente existe
    if cpf in clientes:
        cliente = clientes[cpf]
        numconta = cliente.get("numconta")
        
        # remove do dicionário
        del clientes[cpf]
        salvar_clientes(clientes)
        
        # remove a conta (se existir)
        if numconta and numconta in contas:
            del contas[numconta]
            salvar_contas(contas)
            
        flash(f"Cliente (CPF: {cpf}) foi excluído com sucesso!", "success")
    else:
        flash("Cliente não encontrado para exclusão.", "danger")
        
    return redirect(url_for("agencia.relatorios"))

#listagem de clientes e contas automatica no html 

#Seção: Buscas / Consulta

@agencia.route("/buscar_cpf", methods=["POST"])
def BuscarPorCpf():
    dict_clientes = acessar_clientes()
    consultar_cpf = cpf_com_pontinhos(request.form.get("cpf"))
    
    if consultar_cpf in dict_clientes:
        flash(f"CPF encontrado! Dados: {dict_clientes[consultar_cpf]}", "success")
    else:
        flash("CPF não encontrado na lista de clientes!", "danger")
        
    return redirect(url_for("agencia.relatorios"))


@agencia.route("/buscar_conta", methods=["POST"])
def BuscarPorConta():
    consultar_conta = request.form.get("numconta")
    dict_contas = acessar_contas()
    
    if consultar_conta in dict_contas:
        flash(f"Conta encontrada! Dados: {dict_contas[consultar_conta]}", "success")
    else:
        flash("Conta não encontrada na lista de contas!", "danger")
        
    return redirect(url_for("agencia.relatorios"))


#Seção: Avaliação de Clientes


def numero_de_clientes():
    clientes = acessar_clientes()
    return len(clientes) 

#etapa 4
def numero_de_contas():
    contas = acessar_contas()
    return len(contas)

def contas_saldo_positivo():
    contas = acessar_contas()
    return [(conta, dados_da_conta) for conta, dados_da_conta in contas.items() if dados_da_conta.get('saldo') > 0]
#{numconta: {"titular":---, "numconta":---, "tipo":---, "saldo":---}} o "items" devolve (chave, valor)

def maior_menor_saldo():
    contas = acessar_contas()

    if not contas:  # se o dict estiver vazio
        print("Nenhuma conta cadastrada!")
        return None

    saldos = [dados.get('saldo', 0) for dados in contas.values()] #extraio os saldos

    maior_saldo = max(saldos)
    menor_saldo = min(saldos)

    for conta, dados in contas.items(): 
        if dados.get('saldo', 0) == maior_saldo:
            maior = (conta, dados)
        if dados.get('saldo', 0) == menor_saldo:
            menor = (conta, dados)

    return maior, menor

def saldo_total():
    contas = acessar_contas()

    if not contas:
        print("Nenhuma conta cadastrada!")
        return None
    
    saldos = [dados.get('saldo', 0) for dados in contas.values()]
    return sum(saldos) #evitei usar recursão para caso de teste com muitos dados rs

def saldo_medio():
    contas = acessar_contas()
    
    if not contas:
        print("Nenhuma conta cadastrada!")
        return None
    
    total = saldo_total() #chama a outra função
    quantidade = len(contas)
    
    return total / quantidade


#Parte Final que conecta tudo
@agencia.route("/relatorios")
def relatorios():
    if "cliente_logado" not in session:
        flash("Faça login para ver os relatórios do sistema.", "warning")
        return redirect(url_for("index"))
    
    total_clientes = numero_de_clientes()
    total_contas = numero_de_contas()
    maior, menor = maior_menor_saldo()
    total_saldos = saldo_total()
    media_saldos = saldo_medio()

    return render_template(
        "relatorios.html",
        total_clientes=total_clientes,
        total_contas=total_contas,
        total_saldos=total_saldos,
        media_saldos=media_saldos,
        contas=acessar_contas(),
        clientes= acessar_clientes(),
        agencias = lista_de_agencias(),
        maior_saldo = maior,
        menor_saldo = menor
    )