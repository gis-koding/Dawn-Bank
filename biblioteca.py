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
    with open(nome_arquivojson, "r",encoding="utf-8") as arquivo: #ajuste aqui para acessar a pasta
        lista = json.load(arquivo) #load = le o arqv json
    return lista
    
def ProcurarCpf(cpf):
    #pega a posicao que o cpf esta na lista
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return indice  
       

    '''if str(cpf) in clientes:
        for outros_cpf in clientes:
            if str(cpf) in outros_cpf:
                return outros_cpf[0]'''
    #lembrando: tupla (posicao, nome cpf) 0 1 2

def VerificarCliente(cpf):
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return True
    return False #não existe

def SalvarSaldo(saldo,posicao):
    saldos = acessar_lista("dados json/saldos.json")
    saldos[posicao] = saldo
    salvar_json(saldos,"dados json/saldos.json")