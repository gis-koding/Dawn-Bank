from conta import *
from cliente import *

nome, cpf = CadastroCliente()
validacao = ValidarCPF(cpf)

if validacao:
    saldo = CadastroConta(cliente,cpf)
    
    if saldo >= 50:
        Conta(saldo,cliente)
