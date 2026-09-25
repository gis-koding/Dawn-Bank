from biblioteca import *
from cliente import *
from conta import *
from menus import *

def Cadastro():
    opcao = input('Entrar ou Cadastrar-se: ')
    saldos = acessar_lista("dados json/saldos.json")
    contas = acessar_lista("dados json/contas.json")
    if opcao == 'E':
        nome,cpf = CadastroCliente()
        existente = VerificarCliente(cpf)
        if existente:
            posicao = ProcurarCpf(cpf)
            saldo = saldos[posicao]
            conta = contas[posicao]
            saldo = MenuCliente(nome,conta,saldo)
            SalvarSaldo(saldo,posicao)
        else:
            print('Cliente Inexistente!')
            
    elif opcao == 'C':
        nome,cpf = CadastroCliente()
        posicao = NovoCliente()
        AdicionarCliente(nome,cpf,posicao)
        conta = AdicionarConta(cpf)
        saldo = PrimeiroAcesso()
        SalvarSaldo(saldo,posicao)
        if saldo > 0:
            saldo = MenuCliente(nome,conta,saldo)
            SalvarSaldo(saldo,posicao)
        
    elif opcao == 'G':
        MenuGerente()
        
    
    

