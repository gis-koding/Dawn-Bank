from biblioteca import *
from cliente import *
from conta import *
from menus import *

def Cadastro():
    opcao = input('Entrar ou Cadastrar-se: ')
    saldos = acessar_lista("dados json/saldos.json")
    if opcao == 'E':
        nome,cpf = CadastroCliente()
        existente = VerificarCliente(cpf)
        if existente:
            posicao = ProcurarCpf(cpf)
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
    
    

