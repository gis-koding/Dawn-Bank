from biblioteca import *
from cliente import *
from conta import *
from menus import *

#funcionando!
def Entrar():
    print("Entrando na conta.")
    nome, cpf = CadastroCliente()
    clientes = acessar_dados("clientes")
    contas = acessar_dados("contas")

    #adicionar verificacao
    dados_cliente = clientes.get(cpf)
    if dados_cliente == None: #aqui evita que não tenha cpf cadastrado
        print("Cliente não encontrado! É preciso efetuar cadastro.")
    else:
        conta = dados_cliente[1]
        dados_conta = contas.get(conta)
        MenuCliente(conta,dados_conta)

#funcionando!
def Registrar():
    print("Registrando novo cliente.")
    nome, cpf = CadastroCliente()
    AdicionarCliente(nome,cpf)
    CriarConta(nome,cpf)
    Entrar()

#menu de login
def Login():
    opcao = input('Entrar ou Registrar: ')
    if opcao == 'E':
        Entrar()
    elif opcao == 'R':
        Registrar()
    elif opcao == 'G':
        MenuGerente()
    elif opcao == 'A':
        apagar_dados()
    elif opcao == 'B': #o usuário busca seu próprio cpf, como consulta
        BuscarPorCpf()
    else:
        print('Inválido.')