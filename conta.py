from biblioteca import *
# contas = []

def Saldo(saldo):
    print(f'Saldo = R${saldo}.')

def Depósito(saldo):
     
        valor = int(input('Digite o valor para depositar: '))
        if float(valor) != None:
            saldo += valor
            print('Seu depósito foi concluído com sucesso! Saldo atual: R${saldo}')
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
            

def AdicionarConta(cpf):
    contas = acessar_lista("dados json/contas.json")
    conta = "001" + f"{cpf%1000}"
    contas.append(conta)
    salvar_json(contas,"dados json/contas.json")
    print(conta)
        
'''print('Conta Cadastrada com Sucesso!')
    #Primeiro Depósito
    valor = float(input('Digite o valor a ser depositado: '))
    if valor >= 50.00:
        saldo = valor
        print('Depósito feito com sucesso! Conta Desbloqueada!')
        return saldo
    else:
        saldo = valor
        print(f'Saldo = R${saldo}.')
        return saldo'''