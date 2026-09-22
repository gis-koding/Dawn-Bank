from biblioteca import *

def Cadastro():
    opcao = input('Entrar ou Cadastrar-se: ')
    if opcao == 'E':
        nome,cpf = CadastroCliente()
        existente = VerificarCliente(cpf)
        if existente:
            posicao = posicao_fulaninho(cpf)
            saldo = saldos[posicao]
            saldo = MenuOpcoes(nome,conta,saldo)
            SalvarSaldo(saldo)
        else:
            opcao == 'C'
    elif opcao == 'C':
        nome,cpf = CadastroCliente()
        posicao = NovoCliente()
        AdicionarCliente(nome,cpf,posicao)
        AdicionarConta(cpf)
    
    

