def ProcurarCpf(lista_nomes,lista_cpfs,nome):
    if nome in lista_nomes:
        for posicao_usuario in len(lista_nomes):
            for posicao_cpf in len(lista_cpfs):
                if posicao_usuario == posicao_cpf:
                    return lista_cpfs[posicao_cpf]

def VerificarCliente(lista,nome):
    if nome in lista:
        return True
    else:
        return False
        
def CadastroConta():
    
    print('Conta Cadastrada com Sucesso!')
    #Primeiro Depósito
    valor = float(input('Digite o valor a ser depositado: '))
    if valor >= 50.00:
        saldo = valor
        print('Depósito feito com sucesso! Conta Desbloqueada!')
        return saldo
    else:
        saldo = valor
        print(f'Saldo = R${saldo}.')
        return saldo

def Saldo(saldo):
    print(f'Saldo = R${saldo}.')

def Depósito(saldo):
     
        valor = input('Digite o valor para depositar: ')
        if float(valor) != None:
            saldo += valor
            print('Seu depósito foi concluído com sucesso! Saldo atual: R${saldo}')
        else:
            print('Depósito Cancelado.')
        
def Saque(saldo):
    
        valor = float(input('Qual valor deseja retirar?'))
        if valor < saldo:
           saldo = saldo - valor
           print(f'Saque realizado com sucesso! Saldo atual: R${saldo}')
        else:
           print('Saldo insuficiente ou valor não existe.')
            
def MenuOpcoes(nome,cpf,lista_nomes,lista_saldos):

   # existente = True #ProcurarConta(usuario,conta)
   # if existente:
   # procurar saldos aqui
    menu = (f'''Conta de {nome}
N° da Conta: {cpf}
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
            Depósito(saldo)
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
        elif funcao == 3:
            Saque(saldo)
            print(menu)
            funcao = int(input('Digite o número do serviço: '))
    print('Sessão Finalizada.')
    #Salvar Saldo, Saques e Depósitos
    for posi_usuario in len(lista_nomes):
        for posi_saldo in len(lista_saldos):
            if nome == lista_nomes[posi_usuario] and posi_usuario == posi_saldo:
                lista_saldos[posi_saldo] = saldo
    
            
