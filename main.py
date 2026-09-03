from conta import *
from cliente import *

#cliente 374.443.990-93

nome, cpf = CadastroCliente()
validacao = ValidarCPF(cpf)

if validacao:
    saldo = CadastroConta(nome,cpf)
    
    if saldo >= 50:
        Conta(saldo,nome,cpf)
