def CadastroConta(nome,cpf):
    print("Conta Cadastrada com Sucesso!")
    print("Deseja realizar um depósito de R$50,00 para acessar sua conta?")
    resposta = input()
    if resposta == "Sim":
        print("Digite o valor a ser depositado:")
        valor = float(input())
        if valor > 50.00:
            saldo = valor
            print("Depósito feito com sucesso!")
            print("Entrando na conta...")
            print("O Banco Dawn agradece a preferência :)")
            print("Aguarde...")
        else:
            saldo = valor
            print("Depósito feito com sucesso!")
            print("Não foi possível entrar na conta pois o valor é inferior ao mínimo.")
            print("Dirija-se a uma agência para desbloquear sua conta.")
    elif resposta == "Não":
        print("Conta Bloqueada!")
    else:
        print("Resposta inválida.")

def Conta(saldo):
    print(f"""Conta de {nome}
    Menu de Funções:
    Consultar Saldo
    Realizar Depósito
    Realizar Saque""")
    Funcao = input("Digite uma função do menu: ")
    if funcao == "Consultar Saldo":
        print("Saldo = {saldo}")
    elif funcao == "Realizar Depósito":
        print("Digite o valor para depositar: ")
        valor = float(input())
        print(f"Deseja depositar o valor de {valor} na sua conta?")
        confirmacao = input()
        if confirmacao == "Sim":
            saldo = saldo +  valor
            print("Seu depósito foi concluído com sucesso!")
            print(f"Saldo Atual: R${saldo}")
        elif confirmacao == "Não":
            print("Depósito Cancelado")
        else: 
            print("Resposta inválida.")
    elif funcao == "Realizar Saque":
        print("Qual valor deseja retirar?")
        valor = float(input())
        print(f"Deseja retirar o valor de {valor}?")
        confirmacao = input()
        if confirmacao == "Sim":
            saldo = saldo - valor
            print("Saque realizado com sucesso!")
        elif confirmacao == "Não":
            print("Saque não realizado.")
        else:
            print("Resposta inválida.")
            
