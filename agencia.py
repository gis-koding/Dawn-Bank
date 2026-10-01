from biblioteca import *

def separar():
    #inicializando os dicts
    agencia01 = {}
    agencia02 = {}
    agencia03 = {}
    contas = acessar_dados("contas") #pegando o dict das contas
    chaves = contas.keys() #pegando as chaves
      
    for conta in chaves:
    #pegando os 2 primeiros digitos q definem qual a agencia
        agencia = int(conta)//1000000
    
        #adiciona as contas da agencia x ao dicionario da agencia x
        if agencia == 1: #zero nao aparece no resultado
            agencia01[conta] = contas.get(conta)
        elif agencia == 2:
            agencia02[conta] = contas.get(conta)
        elif agencia == 3:
            agencia03[conta] = contas.get(conta)
            
    
    return agencia01, agencia02, agencia03


def ListarAgencias():

    #"conta": [nome,cpf,tipo,saldo]
    def imprimir(agencia):
        contas = agencia.keys()
        contador = 0 #posicao do cliente pra printar
        #contador de clientes
        
        for conta in contas:
            contador += 1
            dados = agencia.get(conta) #uma lista

            #pegando os dados necessarios
            nome = dados[0]
            cpf = dados[1]
            tipo = dados[2]
            saldo = dados[3]
            
            print(f'''
Cliente N°{contador} 
Nome: {nome}   | Cpf: {cpf}
Conta: {conta} | Tipo de conta: {tipo}
Saldo: R${saldo:.2f} |
''')
        print(f'Clientes Totais: {contador}')

    
    print(f'''[1]Agência 01 
[2]Agência 02
[3]Agência 03 ''')
    escolha = input('Qual agência gostaria de acessar? ')
    agencia01, agencia02, agencia03 = separar()

    if escolha == "1":
        print("Agência 01 — Conta Salário")
        imprimir(agencia01)
    elif escolha == "2":
        print("Agência 02 — Conta Corrente")
        imprimir(agencia02)
    elif escolha == "3":
        print("Agência 03 — Conta Poupança")
        imprimir(agencia03)
        
def Montante(tipo):
    def montante(agencia):
        total = 0
        chaves = agencia.keys()
        for chave in chaves:
            conta = agencia.get(chave)
            saldo = conta[3]
            total += saldo
        return total

    #chamar antes da condicional pq os dois usam
    agencia01, agencia02, agencia03 = separar()
    if tipo == "Agencia":
        print(f'Montante Agência 01: R${montante(agencia01):.2f}')
        print(f'Montante Agência 02: R${montante(agencia02):.2f}')
        print(f'Montante Agência 03: R${montante(agencia03):.2f}')
            
    elif tipo == "Banco":
        total = 0
        total += montante(agencia01)
        total += montante(agencia02)
        total += montante(agencia03)
        print(f'Montante: R${total:.2f}')
            
