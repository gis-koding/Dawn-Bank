import json

DADOSCL = 'clientes.json'
DADOSCO = 'contas.json' #dicionário {"numconta":{}}

def salvar_clientes(REGISTRO):
    '''Salva em clientes.json os dados atualizados.'''
    with open(DADOSCL, "w", encoding="utf-8") as arquivo: 
        json.dump(REGISTRO, arquivo, indent=4, ensure_ascii=False)
              
def acessar_clientes():
    '''Retorna o dicionario mais recente.'''
    if DADOSCL == {}:
        return {}
    with open(DADOSCL, "r",encoding="utf-8") as arquivo:
        return json.load(arquivo) #load = le o arqv json

def decimal_ao_jeito_brasileiro(numero): #zero criatividade para criar essa func
    return float(numero.replace(",",".")) #decimal com virgula -> decimal com ponto

def cpf_com_pontinhos(cpf):
    return cpf.replace(".","").replace("-","").replace(" ", "") #com ponto -> sem ponto, limpissimo

def salvar_contas(REGISTRO):
    '''Salva em contas.json os dados atualizados.'''
    with open(DADOSCO, "w", encoding="utf-8") as arquivo: 
        json.dump(REGISTRO, arquivo, indent=4, ensure_ascii=False)
              
def acessar_contas():
    '''Retorna o dicionário mais recente.'''
    if DADOSCO == {}:
        return {}
    with open(DADOSCO, "r",encoding="utf-8") as arquivo:
        return json.load(arquivo) #load = le o arqv json