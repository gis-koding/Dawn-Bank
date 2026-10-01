from biblioteca import *
from conta import *
from cliente import *
from agencia import *

def MenuCliente(conta,dadosconta):

    #"conta" = [nome,cpf,tipo,saldo]
    nome = dadosconta[0] #print
    cpf = dadosconta[1] #para fazer pix
    saldo = dadosconta[3] #para fazer as operacoes

    menu = (f'''Olá, {nome}! | {conta}
Serviços:
[1]Consultar Saldo  [2]Depósito [3]Saque [4]Pix e TED''')

    print(menu)
    opcao = int(input('Digite um serviço: '))

    #finaliza digitando negativo ou de 5 em diante
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
            saldo = PIXeTED(saldo)

        opcao = int(input('Digite um serviço: '))
        
    print('Sessão Finalizada.')
    salvar_saldo(conta,saldo)


def MenuGerente():

    menug = (f'''Serviços: 
[1]Listar Clientes [2]Listar Agências [3]Listar Contas
[4]Montante Agência [5]Montante Banco''')

    print(menug)
    opcao = int(input('Digite um serviço: '))

    #se digitar de 6 pra cima ou negativo finaliza a sessao
    while opcao >= 0 and opcao < 6:
    
        if opcao == 0:
            print(menug)
        elif opcao == 1:
            ListarClientes()
        elif opcao == 2:
            ListarAgencias()
        elif opcao == 3:
            ListarContas()
        elif opcao == 4:
            Montante("Agencia")
        elif opcao == 5:
            Montante("Banco")
            
        opcao = int(input('Digite um serviço: '))
            
    print('Sessão Finalizada.') 
    #nao precisa de salvamento
