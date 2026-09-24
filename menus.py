from biblioteca import *

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
    while funcao < 4 and funcao > 0:
        if funcao == 1:
            Saldo(saldo)
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 2:
            saldo = Depósito(saldo)
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 3:
            saldo = Saque(saldo)
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
    print('Sessão Finalizada.')
    return saldo


def MenuGerente():
    menug = f'''Serviços:
1 - Relatório do Banco
2 - Listar Clientes
3 - Sair'''


    print(menug)
    opc = int(input('Digite uma opção: '))
    while opc > 0 and opc < 3:
        if opc == 1:

            return RelatorioGeral(Saques,Saldos,Depositos)
            print(menug)
            opc = int(input('Digite uma opção: '))
            
        elif opc == 2:
            return ListarClientes(lista_nomes,lista_cpfs)
            print(menug)
            opc = int(input('Digite uma opção: '))
    print('Sessão Finalizada.')