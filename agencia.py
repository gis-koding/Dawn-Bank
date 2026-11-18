'''novo agencia.py refatorado:'''

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from biblioteca import *
from cliente import Cliente
from conta import Conta_Corrente, Conta_Poupança

agencia = Blueprint('agencia', __name__)

#obs: as funções agora começam por minusculo por padronização
#Seção: Cadastramento

class Agencia:
    def __init__(self): #agencia unica
        self.numero = "01"
        self.clientes = [] #lista dos clientes
        self.contas = [] #lista das contas

    #parte de validar o cpf
    #os créditos vão para como a Receita Federal valida e cria cpfs.
    def validar_cpf(self, cpf):
        #Verifica se o cpf está no formato padrão.
        #formatação de cpf adicionada na biblioteca
        if len(cpf) != 11 or not cpf.isdigit():
            return False #não permitido
        #se for permitido, hora de verificar os dígitos
        digitos = []
        for numero in cpf:
            digitos.append(int(numero))

        tudo_igual = True #flag, para mudar no for
        for inteiro in digitos:
            if digitos[0] != inteiro:
                tudo_igual = False #checo se tem digitos diferentes;
        if tudo_igual:
            return False #não é válido !
        #primeira verificação, digito1
        soma = 0
        peso = 10 #faz parte da soma, é 10 e decresce;
        for i in range(0,9):
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

    #poo -> json; importante para transformar os objetos em json
    def carregar_json(self):
        #Lê os JSON
        self.clientes = []
        self.contas = []

        for cpf, dados in acessar_clientes().items():
            self.clientes.append(Cliente(dados["nome"], cpf))

        #dicionário só para achar o titular rápido
        por_cpf = {cliente.cpf: cliente for cliente in self.clientes}
        #factory method: pega o objeto a partir do json
        for numconta, dados in acessar_contas().items():
            titular = por_cpf.get(dados["titular"])
            if titular is None: #conta sem dono no json, ignora
                continue
            ##Convertendo o dicionário do JSON em um objeto de Conta
            conta = self._dict_para_conta(numconta, dados, titular)
            if conta is None: #tipo inválido no json, ignora
                continue
            #'dados' do json do numero de conta associado ao titular
            self.contas.append(conta)
            titular.contas.append(conta)

    def salvar_json(self):
        '''Grava tudo nos JSON. O to_dict transforma em dicionario para salvar no json, só isso'''
        salvar_clientes({cliente.cpf: cliente.to_dict() for cliente in self.clientes})
        salvar_contas({conta.numconta: self.conta_para_dict(conta) for conta in self.contas})

    def _dict_para_conta(self, numconta, dados, titular):
        '''Do JSON para o objeto: escolhe o tipo de conta, corrente ou poupança!'''
        tipo = dados["tipo"]
        if tipo == "corrente":
            return Conta_Corrente(titular, numconta, dados["saldo"], dados.get("especial", 200))
        elif tipo in ("poupança", "poupanca"):
            return Conta_Poupança(titular, numconta, dados["saldo"])
        else:
            print(f"Conta {numconta} ignorada: tipo desconhecido '{tipo}'.")
            return None

    def conta_para_dict(self, conta):
        '''Do objeto para o JSON.'''
        dados = {"titular": conta.titular.cpf, "numconta": conta.numconta, "saldo": conta.saldo, "tipo": conta.tipo}
        if conta.tipo == "corrente":
            dados["especial"] = conta.especial #o cheque especial também precisa ser guardado
        return dados

    def adicionar_cliente(self, nome, cpf):
        '''Adiciona cliente. Devolve o Cliente, ou None se já existia.'''
        if self.buscar_cliente(cpf) is not None:
            print("Cliente já cadastrado") #evita cliente repetido
            return None

        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        return cliente

    #cadastroclientes direto no html
    #obs: o abrir_conta é o antigo CriarConta, preciso para definir se corrente ou poupança !
    def abrir_conta(self, cliente, tipo, saldo_inicial=0.13):
        '''Abre uma conta (corrente ou poupança) usando a regra de CPF da equipe.'''

        tipo = tipo.lower() #deixa tudo minusculo
        num_base = str(int(cliente.cpf) // 100000)
        if tipo == "corrente":
            numconta = "02" + num_base
        elif tipo in ("poupanca", "poupança"):
            numconta = "03" + num_base
        else:
            # qlq tipo de conta !
            print(f"Tipo de conta '{tipo}' não é permitido.")
            return None
        while len(numconta) < 8:
            numconta = numconta + "5"
        # colocando em POO:
        if tipo == "corrente":
            nova_conta = Conta_Corrente(cliente, numconta, saldo_inicial)
        else:
            nova_conta = Conta_Poupança(cliente, numconta, saldo_inicial)
        #guardamos em agencia e cliente.
        self.contas.append(nova_conta)
        cliente.contas.append(nova_conta)

        return nova_conta

    #MÉTODO: apaga o cliente e as contas dele das listas
    def excluir_cliente(self, cpf):
        '''Remove o cliente e todas as contas dele. Devolve True se excluiu.'''
        cliente = self.buscar_cliente(cpf)
        if cliente is None:
            return False

        for conta in cliente.contas:
            self.contas.remove(conta)
        self.clientes.remove(cliente)
        return True

    #Seção: Buscas / Consulta

    #MÉTODO: procura o cliente na lista
    def buscar_cliente(self, cpf):
        '''Devolve o Cliente com esse cpf, ou None.'''
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    #MÉTODO: procura a conta na lista
    def buscar_conta(self, numconta):
        '''Devolve a Conta com esse número, ou None.'''
        for conta in self.contas:
            if conta.numconta == numconta:
                return conta
        return None

    #Seção: Listagem

    #listagem de clientes e contas automatica no html

    def lista_de_agencias(self): #etapa4
        '''Só existe 1 agência.'''
        return [self.numero]

    '''observação importante para essa sessão: as funções ~antigas~ voltam como objetos da classe Agencia para deixar a classe
    com mais controle com os dados, não só depender do html'''

    #Seção: Avaliação de Clientes

    def numero_de_clientes(self):
        return len(self.clientes)

    #etapa 4
    def numero_de_contas(self):
        return len(self.contas)

    def contas_saldo_positivo(self):
        return [conta for conta in self.contas if conta.saldo > 0]
    #cada conta é um objeto Conta; o saldo vem de conta.saldo

    def maior_menor_saldo(self):
        if not self.contas:  # se a lista estiver vazia
            print("Nenhuma conta cadastrada!")
            return None

        saldos = [conta.saldo for conta in self.contas] #extraio os saldos

        maior_saldo = max(saldos)
        menor_saldo = min(saldos)

        for conta in self.contas:
            if conta.saldo == maior_saldo:
                maior = conta
            if conta.saldo == menor_saldo:
                menor = conta

        return maior, menor

    def saldo_total(self):
        if not self.contas:
            print("Nenhuma conta cadastrada!")
            return None

        saldos = [conta.saldo for conta in self.contas]
        return sum(saldos) #evitei usar recursão para caso de teste com muitos dados rs

    def saldo_medio(self):
        if not self.contas:
            print("Nenhuma conta cadastrada!")
            return None

        total = self.saldo_total() #chama a outra função
        quantidade = len(self.contas)

        return total / quantidade


#agencia unica !
agencia_unica = Agencia()

#Seção: HTML !
#Rotas (cada uma só recebe o pedido, chama a Agencia e responde)

#ROTA (HTML): recebe o pedido, chama o método excluir_cliente e responde
@agencia.route("/excluir_cliente", methods=["POST"])
def excluir_cliente():
    # dados do cliente
    cpf = request.form.get("cpf")

    # verifica se o cliente existe e já exclui
    if agencia_unica.excluir_cliente(cpf):
        agencia_unica.salvar_json() # adicionado
        flash(f"Cliente (CPF: {cpf}) foi excluído com sucesso!", "success")
    else:
        flash("Cliente não encontrado para exclusão.", "danger")

    return redirect(url_for("agencia.relatorios"))

#Seção: Buscas / Consulta

#ROTA (HTML): recebe o pedido, chama o método buscar_cliente e responde
@agencia.route("/buscar_cpf", methods=["POST"])
def buscar_por_cpf():
    consultar_cpf = cpf_com_pontinhos(request.form.get("cpf"))
    cliente = agencia_unica.buscar_cliente(consultar_cpf)

    if cliente is not None:
        flash(f"CPF encontrado! Dados: {cliente.to_dict()}", "success")
    else:
        flash("CPF não encontrado na lista de clientes!", "danger")

    return redirect(url_for("agencia.relatorios"))


#ROTA (HTML): recebe o pedido, chama o método buscar_conta e responde
@agencia.route("/buscar_conta", methods=["POST"])
def buscar_por_conta():
    consultar_conta = request.form.get("numconta")
    conta = agencia_unica.buscar_conta(consultar_conta)

    if conta is not None:
        flash(f"Conta encontrada! Dados: {agencia_unica.conta_para_dict(conta)}", "success")
    else:
        flash("Conta não encontrada na lista de contas!", "danger")

    return redirect(url_for("agencia.relatorios"))


#Parte Final que conecta tudo
#ROTA (HTML): pega os dados da Agencia e manda para o relatorios.html
@agencia.route("/relatorios")
def relatorios():
    if "cliente_logado" not in session:
        flash("Faça login para ver os relatórios do sistema.", "warning")
        return redirect(url_for("index"))

    resultado = agencia_unica.maior_menor_saldo()
    if resultado is None: #sem contas
        maior, menor = None, None
    else:
        maior, menor = resultado

    return render_template(
        "relatorios.html",
        total_clientes=agencia_unica.numero_de_clientes(),
        total_contas=agencia_unica.numero_de_contas(),
        total_saldos=agencia_unica.saldo_total(),
        media_saldos=agencia_unica.saldo_medio(),
        contas=agencia_unica.contas,
        clientes=agencia_unica.clientes,
        agencias=agencia_unica.lista_de_agencias(),
        maior_saldo=maior,
        menor_saldo=menor
    )





'''antigo agencia.py:

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from biblioteca import *

agencia = Blueprint('agencia', __name__)


#Seção: Cadastramento


def AdicionarCliente(nome,cpf):
    #Adiciona cliente no banco de dados.

    clientes = acessar_clientes()
    if cpf in clientes:
        print("Cliente já cadastrado") #evita sobrescrever dados no dicionário
    else:
        clientes[cpf] = {'nome': nome, 'cpf': cpf}
        salvar_clientes(clientes)

#cadastroclientes direto no html

def ValidarCPF(cpf):
    #Verifica se o cpf está no formato padrão.

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
    #Verifica as agências existentes. Sem cliente, sem agência.
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
    ''' 