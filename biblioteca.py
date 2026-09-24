import json
#nao precisa importar

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

def apagar_json():
    #apagar dados 
    salvar_json([],"dados json/clientes.json")
    salvar_json([],"dados json/contas.json")
    salvar_json([],"dados json/saldos.json")
    print("Todos os dados excluídos com sucesso!")

def ApagarConta(posicao):
    contas = acessar_lista("dados json/contas.json")
    contas.delete(posicao)
    salvar_json(contas,"dados json/contas.json")
    print("Conta excluída!")
    
def ProcurarCpf(cpf):
    #pega a posicao que o cpf esta na lista
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return indice
       
    #lembrando: tupla (posicao, nome cpf) 0 1 2

def VerificarCliente(cpf):
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return True
    return False #não existe
    
    #porque o loop sendo que só o 'in' resolve?

def SalvarSaldo(saldo,posicao):
    saldos = acessar_lista("dados json/saldos.json")
    saldos[posicao] = saldo
    salvar_json(saldos,"dados json/saldos.json")

def NovoCliente():
    clientes = acessar_lista("dados json/clientes.json")
    posicao = len(clientes)
    #se é 0, a posicao é 0
    return posicao

def SalvarAgencia():
    contas = acessar_lista("dados json/contas.json")
    agencia1 = acessar_lista("dados json/agencia1.json")
    agencia2 = acessar_lista("dados json/agencia2.json")

    for conta in contas:
        if int(conta)%100 == 001:
            agencia1.append(conta)
        else:
            agencia2.append(conta)
    salvar_json(agencia1,"dados json/agencia1.json")
    salvar_json(agencia2,"dados json/agencia2.json")
