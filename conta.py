from biblioteca import *

def decimal_ao_jeito_brasileiro(numero): #zero criatividade para criar essa func
    return float(numero.replace(",",".")) #decimal com virgula -> decimal com ponto

#Consultar Saldo
def Saldo(saldo):
    print(f'Saldo = R${saldo:.2f}.')


def Depósito(saldo):
        valor = decimal_ao_jeito_brasileiro(input('Digite o valor para depositar: '))
        if valor > 0:
            saldo += valor
            print(f'Depósito concluído! Saldo atual: R${saldo:.2f}')
        else:
            print('Depósito cancelado.')

        return saldo


def Saque(saldo):
        valor = decimal_ao_jeito_brasileiro(input('Digite o valor para sacar: '))
        if valor < saldo:
           saldo = saldo - valor
           print(f'Saque concluído! Saldo atual: R${saldo:.2f}')       
        else:
           print('Saque cancelado.')        

        return saldo


def CriarConta(nome,cpf):
    tipo = input('Escolha o tipo da conta: ')
    #conjuntos pra facilitar as condicionais
    salario = {'salario','Salario','sa'}
    corrente = {'corrente','Corrente','co'}
    #6 ultimos digitos do cpf
    numconta = (int(cpf)//100000)

    #definindo o tipo de conta // agencia
    if tipo in salario:
        conta = "01" + f'{numconta}'
        tipo = "salario"
    elif tipo in corrente:
        conta = "02" + f'{numconta}'
        tipo = "corrente"
    else:
        conta = "03" + f'{numconta}'
        tipo = "poupança"
        
    while len(conta) < 8:
        conta = conta + "5"
        print(tipo,conta)
        
    #N° da conta = agencia/tipo da conta + 6 dig do cpf

    #adicionando os dados necessarios no json
    AdicionarConta(nome,cpf,conta,tipo)
    
    #cliente[cpf] = "cpf": [nome,conta]
    #contas[conta] = "conta": [nome ou (nome1,nome2),str(cpf),saldo,int(conta)]


def AdicionarConta(nome,cpf,conta,tipo):
    clientes = acessar_dados("clientes")
    contas = acessar_dados("contas")
    
    dados_cliente = clientes.get(cpf) #lista com os dados do cliente
    dados_cliente.append(conta) #adiciona a conta na lista do cliente
    saldo = PrimeiroAcesso() #adiciona o 1ro  saldo na conta do cliente

    contas[conta] = [nome,cpf,tipo,saldo]
    clientes[cpf] = dados_cliente
    salvar_dados(clientes,"clientes")
    salvar_dados(contas,"contas")


def PrimeiroAcesso():
    print('Conta Cadastrada com Sucesso!')
    #Primeiro Depósito
    saldo = decimal_ao_jeito_brasileiro(input('Digite o valor a ser depositado: '))
    print("Lembrete: Total mínimo de R$50.00")
    
    while saldo < 50:
    #so entra na conta se o valor juntado for >= 50
    
        print("Saldo insuficiente")
        saldo += float(input('Digite o valor a ser depositado: '))
        
    return saldo


#atualizado!

def ListarContas():
    contas = acessar_dados("contas")
    chaves = contas.keys()
    contador = 0
    #"conta": [nome,cpf,tipo,saldo]
    for conta in chaves:
        contador += 1
        dados = contas.get(conta)
        
        nome = dados[0]
        cpf = dados[1]
        tipo = dados[2]
        saldo = dados[3]
        
        print(f'''Cliente N°: {contador} | Nome: {nome} | CPF: {cpf}
Conta: {conta} | Tipo de Conta: {tipo} | Saldo: R${saldo:.2f}
''')


# transferencia por meio do n° da conta
# e cpf
def PIXeTED(saldo):
#LEMBRAR: fazer funcao para os blocos de busca e transferencia
# loop e validacao de conta, cpf

    # "cpf": [nome,conta]
    def porCPF(saldo):
        cpfdestino = input('Digite um cpf: ')
        #validacao de cpf aqui

        #pegar o nunero da conta destino
        clientes = acessar_dados("clientes")
        dados_destino = clientes.get(cpfdestino)
        contadestino = dados_destino[1]
        nomedestino = dados_destino[0]

        #pegar o saldo destino a partir da conta
        contas = acessar_dados("contas")
        dados_conta = contas.get(contadestino)
        saldodestino = dados_conta[3]

        print(f'Transferindo para {nomedestino}')
        #transferencia
        valordestino = decimal_ao_jeito_brasileiro(input('Digite o valor a transferir: '))
        if saldo >= valordestino:
            saldodestino += valordestino
            saldo -= valordestino
            print(f'Transferência concluída! Saldo atual: R${saldo:.2f}')

            #salvarsaldo do destino
            salvar_saldo(contadestino,saldodestino)
        else:
            print('Saldo insuficiente.')
        
        return saldo   

    #'conta': [nome,cpf,tipo,saldo]
    def porConta(saldo):
        contadestino = input('Digite N° da conta: ')
        #validacao de conta aqui

        #pegando o saldo destino apartir da conta
        contas = acessar_dados("contas")
        dados_conta = contas.get(contadestino)
        saldodestino = dados_conta[3]
        nomedestino = dados_conta[0]
        
        #transferencia
        print(f'Transferindo para {nomedestino}')
        valordestino = decimal_ao_jeito_brasileiro(input('Digite o valor a transferir: '))
        if saldo >= valordestino:
            saldodestino += valordestino
            saldo -= valordestino
            print(f'Transferência concluída! Saldo atual: R${saldo:.2f}')
            salvar_saldo(contadestino,saldodestino)
        else:
            print('Saldo insuficiente.')

        
        return saldo
        

    print(f'''Como deseja transferir? 
[1]CPF [2]N° da Conta''')

    escolha = int(input())
    if escolha == 1:
        saldo = porCPF(saldo)
    elif escolha == 2:
        saldo = porConta(saldo)
    return saldo    
    
