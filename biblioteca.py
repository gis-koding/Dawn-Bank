import json

#importar todas as funçoes para cá
from cliente import *
from conta import *

def salvar_json(lista, nome_arquivojson):
    with open(nome_arquivojson, "w", encoding="utf-8") as arquivo: 
        #o w é write: escrever e o utf mantem a formatação
        json.dump(lista, arquivo, ensure_ascii=False)
        #o dump escreve
        #o ensure ascii mantém acentos e formatação no arq json q será criado

def acessar_lista(nome_arquivojson):
    #carregar json
    with open(nome_arquivojson, "r",encoding="utf-8") as arquivo:
        lista = json.load(arquivo) #load = le o arqv json
    return lista
    
def ProcurarCpf(cpf):
    #pega a posicao que o cpf esta na lista
    cpfs = acessar_lista("clientes")
    if str(cpf) in cpfs:
        for outros_cpf in cpfs:
            if str(cpf) in outros_cpf:
                return outros_cpf[0]

def VerificarCliente(cpf):
    lista = acessar_lista("clientes")
    if str(cpf) in lista:
        return True
    else:
        return False

def SalvarSaldo(saldo,posicao):
        saldos = acessar_lista("saldos")
        saldos[posicao] = saldo
        salvar_json(saldos,"saldos")


