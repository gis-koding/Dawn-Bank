from conta import *
from cliente import *

#cliente 374.443.990-93
#listas com os dados dos clientes
lista_nomes = []
lista_cpfs = [] 

nome, cpf = CadastroCliente()
validacao = ValidarCPF(cpf)
AdicionaCliente(lista_nomes, lista_cpfs, nome, cpf) #cliente validado e adicionados nas listas

if validacao:
    saldo = CadastroConta(nome,cpf)
    
    if saldo >= 50:
        Conta(saldo,nome,cpf)
        

