from conta import *
from cliente import *

#cliente 374.443.990-93
#listas com os dados dos clientes
nomes = []
cpfs = []

nome, cpf = CadastroCliente()
validacao = ValidarCPF(cpf)
AdicionaCliente(nomes, cpfs, nome, cpf) #cliente validado e adicionados nas listas
existente = VerificarCliente(nomes,nome) #verifica se cliente existe na base de dados

#Se não existe, adiciona os dados pela primeirs vez
if validacao and not existente:
    saldo = CadastroConta()
    lista_saldos.append(saldo)
    
    if saldo >= 50:
        Conta(saldo,nome,cpf)

#Se existe, pula pro menu de opcoes
elif validacao and existente:
    MenuOpcoes(nome,cpf,lista_nomes,lista_saldos)
        

