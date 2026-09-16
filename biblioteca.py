import json

def salvar_json(lista, nome_arquivojson):
    with open(nome_arquivojson, "w", encoding="utf-8") as arquivo: 
        #o w é write: escrever e o utf mantem a formatação
        json.dump(lista, arquivo, ensure_ascii=False)
        #o dump escreve
        #o ensure ascii mantém acentos e formatação no arq json q será criado

def carregar_json(nome_arquivojson):
    with open(nome_arquivojson, "r",encoding="utf-8") as arquivo:
        lista = json.load(arquivo) #load = le o arqv json
    return lista