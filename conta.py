def CadastroConta(nome,cpf):
    
    print('Conta Cadastrada com Sucesso!')
    resposta = input('Deseja realizar um depósito de R$50,00 para acessar sua conta?  ') 
    
    #confirmação da ação
    if resposta == "s":
        valor = float(input('Digite o valor a ser depositado: '))
        if valor >= 50.00:
            saldo = valor
            print('Depósito feito com sucesso!')
            return saldo
        else:
            saldo = valor
            print('Depósito feito com sucesso! Conta Bloqueada pois valor menor que mínimo.')
    elif resposta == "n":
        print('Conta Bloqueada!')
    else:
        print('Inválido.')

def Saldo(saldo):
    return print(f'Saldo = R${saldo}')

def Depósito(saldo):
     
        valor = float(input('Digite o valor para depositar: '))

        #confirmação da ação
        print(f'Deseja depositar o valor de R${valor} na sua conta?') #sim ou não, confirmar ou cancelar
        confirmacao = input()
        if confirmacao == "s":
            saldo += valor
            return print('Seu depósito foi concluído com sucesso! Saldo atual: R${saldo}')
        elif confirmacao == "n":
            return print('Depósito Cancelado.')
        else: 
            return print('Inválido.')
        
def Saque(saldo):
    
        valor = float(input('Qual valor deseja retirar?'))

        #confirmação da ação
        confirmacao = input(f'Deseja retirar o valor de R${valor}?')
        if confirmacao == "s":
            if valor < saldo:
                saldo = saldo - valor
                print(f'Saque realizado com sucesso! Saldo atual: R${saldo}')
            else:
                print('Saldo insuficiente ou valor não existe.')
        elif confirmacao == "n":
            print('Saque não realizado.')
        else:
            print('Inválido.')
            
#Lembrar: no lugar do cpf incluir numero aleatorio
def Conta(saldo,nome,cpf):

    print(f'''Conta de {nome}
N° da Conta: {cpf}    
Menu de Serviços:
1- Saldo
2- Depósito
3- Saque''')
    funcao = int(input('Digite o número do serviço: '))

    if funcao == 1:
        Saldo(saldo)
    elif funcao == 2:
        Depósito(saldo)
    elif funcao == 3:
        Saque(saldo)
    else:
        print('Inválido.')

        
