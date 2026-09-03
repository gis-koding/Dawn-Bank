def CadastroConta(nome,cpf):
    
    print("""Conta Cadastrada com Sucesso!
Deseja realizar um depósito de R$50,00 para acessar sua conta? 
s/n""")
    resposta = input() #confirmação da ação

    #Confirmado
    if resposta == "s":
        print("Digite o valor a ser depositado:")
        valor = float(input())

        #Para saber se o valor digitado está correto
        if valor >= 50.00:
            saldo = valor
            print("""Depósito feito com sucesso!
Entrando na conta...""")
            return saldo
        else:
            saldo = valor
            print("""Depósito feito com sucesso!
Não foi possível entrar na conta pois o valor é inferior ao mínimo.""")

    #Cancelado
    elif resposta == "n":
        print("Conta Bloqueada!")
        
    #Qualquer outra resposta 
    else:
        print("Resposta inválida.")



#Lembrar: no lugar do cpf incluir numero aleatorio
def Conta(saldo,nome,cpf):

    #Menu de escolha
    print(f"""  Conta de {nome}
    N° da Conta: {cpf}    
Menu de Serviços:
1- Saldo
2- Depósito
3- Saque
4- Sair""")
    funcao = int(input("Digite o número do serviço: "))

    #Saldo
    if funcao == 1:
        print(f"Saldo = R${saldo}")

    #Depósito
    elif funcao == 2:
    
        print("Digite o valor para depositar: ")
        valor = float(input())
        print(f"""Deseja depositar o valor de R${valor} na sua conta?
s/n""") #sim ou não, confirmar ou cancelar

        confirmacao = input()
        #Confirmado
        if confirmacao == "s":
            saldo += valor
            print("Seu depósito foi concluído com sucesso!")
            print(f"Saldo atual: R${saldo}")
        #Cancelado
        elif confirmacao == "n":
            print("Depósito Cancelado")
        #QR
        else: 
            print("Resposta inválida.")

    #Saque
    elif funcao == 3:
    
        print("Qual valor deseja retirar?")
        valor = float(input())
        print(f"""Deseja retirar o valor de R${valor}?
s/n""")

        confirmacao = input()
        if confirmacao == "s":
            if valor < saldo:
                saldo = saldo - valor
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R${saldo}")
            else:
                print("Saldo insuficiente ou valor não existe.")
        elif confirmacao == "n":
            print("Saque não realizado.")
        else:
            print("Resposta inválida.")
            
    #Sair
    elif funcao == 4:
        print("Saindo da conta...")
        
    #QR
    else:
        print("Resposta inválida.")
            
