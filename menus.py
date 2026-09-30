from biblioteca import *
from conta import *
from cliente import *

def MenuCliente(conta,dadosconta):

    nome = dadosconta[0]
    saldo = dadosconta[3]

    menu = (f'''Olá, {nome}! | {conta}
Serviços:
[1]Consultar Saldo  [2]Depósito [3]Saque [4]Pix e TED''')

    print(menu)
    opcao = int(input('Digite um serviço: '))
    
    while opcao >=  0 and opcao < 5:
    
        if opcao == 0:
            print(menu)
        elif opcao == 1:
            Saldo(saldo)
        elif opcao == 2:
            saldo = Depósito(saldo)
        elif opcao == 3:
            saldo = Saque(saldo)
        elif opcao == 4:
            saldo = PixeTED(saldo)

        opcao = int(input('Digite um serviço: '))
        
    print('Sessão Finalizada.')
    salvar_saldo(conta,saldo)


def MenuGerente():

    menug = (f'''Serviços: 
[1]Listar Clientes [2]Listar Agências [3]Listar Contas
[4]Montante Agência [5]Montante Banco''')

    print(menug)
    opcao = int(input('Digite um serviço: '))
    
    while opcao >= 0 and opcao < 6:
    
        if opcao == 0:
            print(menug)
        elif funcao == 1:
            ListarClientes()
        elif funcao == 2:
            ListarAgencias()
        elif funcao == 3:
            ListarContas()
        elif funcao == 4:
            Montante("Agencia")
        elif funcao == 5:
            Montante("Banco")
            
        opcao = input('Digite um serviço: ') 
            
    print('Sessão Finalizada.') 
    #nao precisa de salvamento
