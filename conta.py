from biblioteca import *
# contas = []

def Saldo(saldo):
    print(f'Saldo = R${saldo}.')

def Depósito(saldo):
     
        valor = int(input('Digite o valor para depositar: '))
        if float(valor) != None:
            saldo += valor
            print(f'Seu depósito foi concluído com sucesso! Saldo atual: R${saldo}')
        else:
            print('Depósito Cancelado.')
        return saldo 
        
def Saque(saldo):
    
        valor = float(input('Qual valor deseja retirar?'))
        if valor < saldo:
           saldo = saldo - valor
           print(f'Saque realizado com sucesso! Saldo atual: R${saldo}')
           
        else:
           print('Saldo insuficiente ou valor não existe.')
        return saldo

def AdicionarConta(cpf):
    contas = acessar_lista("dados json/contas.json")
    clientes = acessar_lista("dados json/clientes.json")
    if len(clientes) < 4:
        conta = "001" + f"{cpf//1000}"
        contas.append(conta)
        salvar_json(contas,"dados json/contas.json")
        print(conta)
        return conta
    else:
        conta = "002" + f"{cpf//1000}"
        contas.append(conta)
        salvar_json(contas,"dados json/contas.json")
        print(conta)
        return conta

#funcao a ser trabalhada mais tarde
def PrimeiroAcesso():
    print('Conta Cadastrada com Sucesso!')
    #Primeiro Depósito
    valor = float(input('Digite o valor a ser depositado: '))
    if valor >= 50.00:
        saldo = valor
        print('Depósito suficiente!')
        return saldo
    else:
        saldo = valor
        print(f'Saldo insuficiente. Conta não cadastrada.')
        return saldo

def AdicionarSaldo(saldo):
    saldos = acessar_lista("dados json/saldos.json")
    saldos.append(saldo)
    salvar_json(saldos,"dados json/saldos.json")
