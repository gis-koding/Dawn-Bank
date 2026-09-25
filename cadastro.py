from biblioteca import *
from cliente import *
from conta import *
from menus import *

#menu de login
def Cadastro():
    opcao = input('Entrar ou Cadastrar-se: ')
    #inicializa os dados json
    saldos = acessar_lista("dados json/saldos.json")
    contas = acessar_lista("dados json/contas.json")

    #Entrar
    if opcao == 'E':
        nome,cpf = CadastroCliente() #Pega o nome e cpf
        existente = VerificarCliente(cpf) #Verifica se existe
        if existente:
        #se existe, pega a posicao, saldo e conta
        #posicao: para atualizar atraves das listas
            posicao = ProcurarCpf(cpf) 
            saldo = saldos[posicao] 
            conta = contas[posicao]
            saldo = MenuCliente(nome,conta,saldo)
            SalvarSaldo(saldo,posicao)
        else:
            print('Cliente Inexistente!')
            
    elif opcao == 'C':
        nome,cpf = CadastroCliente()
        posicao = NovoCliente() #calcula a posicao do cliente novo
        #e ja deixa salvo pra atualizar em seguida
        AdicionarCliente(nome,cpf,posicao) #adiciona o cliente nos dados
        #cria a conta, salva e cria o primeiro saldo
        conta = AdicionarConta(cpf) 
        saldo = PrimeiroAcesso()
        SalvarSaldo(saldo,posicao)
        saldo = MenuCliente(nome,conta,saldo)
        SalvarSaldo(saldo,posicao)
        
    elif opcao == 'G': 
        MenuGerente()
        #Acesso a relatorio, listagem, etc
        
    
    

