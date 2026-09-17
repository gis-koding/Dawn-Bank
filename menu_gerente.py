def RelatorioGeral(SaquesTotais,SaldosTotais,DepositosTotais):
    print(f'Saques: {SaquesTotais}, Saldos: {SaldosTotais}, Depositos: {DepositosTotais}')



Saques = 0
Saldos = 0
Depositos = 0

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
