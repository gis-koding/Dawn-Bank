import json

DADOS = 'clients.json'

def salvar_dados(clientes):
    with open(DADOS, "w", encoding="utf-8") as arquivo: 
        #o w é write: escrever e o utf mantem a formatação
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
        #o dump escreve
        #o ensure ascii mantém acentos e formatação no arq json q será criado
        #o indent deixa o json elegante para visualização


def acessar_dados(): #antigo acessar_lista, p/ carregar json
    if DADOS == {}:
        return {}
    #carregar lista 
    with open(DADOS, "r",encoding="utf-8") as arquivo:
        return json.load(arquivo) #load = le o arqv json


