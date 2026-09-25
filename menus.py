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
3- Saque
4- Transferência''')
    print(menu)
    funcao = int(input('Digite o número do serviço: '))
    while funcao < 5 and funcao >= 0:
        if funcao == 1:
            Saldo(saldo) #so pra mostrar, nao precisa salvar
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 2:
            saldo = Depósito(saldo)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 3:
            saldo = Saque(saldo)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 4:
            saldo = Transferencia(saldo)
            funcao = int(input('Digite o número do serviço: '))
        else:
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
    print('Sessão Finalizada.')
    return saldo #para salvamento no json


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
    
    while opc >= 0 and opc < 6:
    
        if opc == 1:
            ListarClientes() #em clientes.py
            opc = int(input('Digite uma opção: '))
            
        elif opc == 2:
            ListarAgencias() #em biblioteca
            opc = int(input('Digite uma opção: '))

        elif opc == 3:
            ListarContas() #em conta.py
            opc = int(input('Digite uma opção: '))
        elif opc == 4:
            Montante("Agencia") #em biblioteca
            opc = int(input('Digite uma opção: '))
            
        elif opc == 5:
            Montante("Banco") #em biblioteca
            opc = int(input('Digite uma opção: '))

        else:
            print(menug)
            opc = int(input('Digite uma opção: '))
            
    print('Sessão Finalizada.') #nao precisa de salvamento
