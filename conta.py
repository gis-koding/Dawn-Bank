from biblioteca import *

def Saldo(saldo):
    print(f'Saldo = R${saldo}.')
    

def Depósito(saldo):
        valor = float(input('Digite o valor para depositar: '))
        
        if valor > 0:
            saldo += valor
            print(f'Seu depósito foi concluído com sucesso! Saldo atual: R${saldo}')

        else:
            print('Depósito Cancelado.')
            
        return saldo 

    
def Saque(saldo):
    
        valor = float(input('Digite o valor para sacar: '))
        
        if valor < saldo:
           saldo = saldo - valor
           print(f'Saque realizado com sucesso! Saldo atual: R${saldo}')
           
        else:
           print('Saldo insuficiente ou valor não existe.')
        return saldo
    

def AdicionarConta(cpf):
    contas = acessar_lista("dados json/contas.json")
    clientes = acessar_lista("dados json/clientes.json")
    
    if len(clientes) < 4: #limite de clientes por agencia
        conta = "001" + f"{cpf//1000}" #se estiver dentro do limite, esta cadastrado na agencia 1
        contas.append(conta)
        salvar_json(contas,"dados json/contas.json")
        print(conta)
        return conta
    else:
        #se nao, esta cadastrado na 2 / limite alteravel
        conta = "002" + f"{cpf//1000}"
        contas.append(conta)
        salvar_json(contas,"dados json/contas.json")
        print(conta)
        return conta

def PrimeiroAcesso():
    print('Conta Cadastrada com Sucesso!')
    #Primeiro Depósito
    valor = float(input('Digite o valor a ser depositado: '))
    print("Lembrete: Total mínimo de R$50.00")
    while valor < 50: #so entra na conta se o valor juntado for >= 50
        print("Saldo insuficiente")
        valor += float(input('Digite o valor a ser depositado: '))
    return valor

''' #a funcao salvarsaldo ja faz isso
def AdicionarSaldo(saldo):
    saldos = acessar_lista("dados json/saldos.json")
    saldos.append(saldo)
    salvar_json(saldos,"dados json/saldos.json")'''

def ListarContas():
    contas = acessar_lista("dados json/contas.json")
    for posicao in range(len(contas)):
        print(f'Posição: {posicao} | Conta: {contas[posicao]}')

# transferencia por meio do n° da conta
def Transferencia(saldo):
    contas = acessar_lista("dados json/contas.json")
    saldos = acessar_lista("dados json/saldos.json")
    
    destino = int(input('Digite o N° da conta: '))
    valordestino = float(input('Valor: '))
    
    for indice in range(len(contas)):
        if destino == int(contas[indice]):
            saldos[indice] += valordestino
            saldo -= valordestino
            print(f'Transferência bem sucedida!Saldo: R${saldo}')
    return saldo
            
    
