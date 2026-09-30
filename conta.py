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
    saldo = float(input('Digite o valor a ser depositado: '))
    print("Lembrete: Total mínimo de R$50.00")
    
    while saldo < 50:
    #so entra na conta se o valor juntado for >= 50
    
        print("Saldo insuficiente")
        saldo += float(input('Digite o valor a ser depositado: '))
        
    return saldo






#ATUALIZAR:

'''def ListarContas():
    contas = acessar_lista("dados json/contas.json")
    for posicao in range(len(contas)):
        print(f'Posição: {posicao} | Conta: {contas[posicao]}')

# transferencia por meio do n° da conta
def PIXeTED(conta,saldo):
    contas = acessar_dados("dados json/contas.json")
    dados_conta = contas.get(conta)
    saldo = dados_conta[3]
    
    destino = int(input('Digite o N° da conta: '))
    valordestino = float(input('Valor: '))
    
    dados_contadestino = contas.get(conta,0)
    if dados_contadestino == 0:
        print("Conta não encontrada")
    else:
        saldodestino = dados_contadestino[3]
        saldodestino += valordestino
        saldo -= valordestino
        
        Salvar(saldodestino)
        print(f'Transferência bem sucedida!Saldo: R${saldo}')

    return saldo'''
            
    
