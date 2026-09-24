from biblioteca import *
from conta import *
from cliente import *

def MenuCliente(nome,conta,saldo):

   # existente = True
   # if existente:
    menu = (f'''Conta de {nome}
N° da Conta: {conta}
Serviços:
1- Saldo
2- Depósito
3- Saque''')
    print(menu)
    funcao = int(input('Digite o número do serviço: '))
    while funcao < 4 and funcao >= 0:
        if funcao == 1:
            Saldo(saldo)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 2:
            saldo = Depósito(saldo)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 3:
            saldo = Saque(saldo)
            funcao = int(input('Digite o número do serviço: '))
        else:
            print(menu)
    print('Sessão Finalizada.')
    return saldo


def MenuGerente():
    menug = f'''Serviços:
1 - Listar Clientes
2 - Listar Agências
3 - Listar Contas
4 - Montante Agência
5 - Montante Banco
Sair'''


    print(menug)
    opc = int(input('Digite uma opção: '))
    
    while opc >= 0 and opc < 7:
    
        if opc == 1:
            
            opc = int(input('Digite uma opção: '))
            
        elif opc == 2:
            return ListarClientes(lista_nomes,lista_cpfs)
            print(menug)
            opc = int(input('Digite uma opção: '))
    print('Sessão Finalizada.')
