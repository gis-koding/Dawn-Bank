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

    if nome_arquivojson == "dados json/contas.json" or nome_arquivojson == "dados json/saldos.json":
        return lista
    #transforma a matriz em tuplas
    else:
        for indice in range(len(lista)):
            if len(lista[indice]) > 0:
                lista[indice] = tuple(lista[indice])
        
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
    if len(saldos) > posicao:
        saldos[posicao] = saldo
        salvar_json(saldos,"dados json/saldos.json")
    else:
        saldos.append(saldo)
        salvar_json(saldos,"dados json/saldos.json")

def NovoCliente():
    clientes = acessar_lista("dados json/clientes.json")
    posicao = len(clientes)
    #se é 0, a posicao é 0
    return posicao


def ListarAgencias():
    clientes = acessar_lista("dados json/clientes.json")
    contas = acessar_lista("dados json/contas.json")
    saldos = acessar_lista("dados json/saldos.json")
    
    agencia = int(input('N° da agência: '))
    if agencia == 1:
        clientes1 = clientes[:3]
        contas1 = contas[:3]
        saldos1 = saldos[:3]
        print('Agência 001')
        for indice in range(len(clientes1)):
            print(f'Cliente N° {indice} | Conta: {contas1[indice]} | Saldo: {saldos1[indice]}')
        
    elif agencia == 2:
        clientes2 = clientes[3:]
        contas2 = contas[3:]
        saldos2 = saldos[3:]
        print('Agência 002')
        for indice in range(len(clientes2)):
            print(f'Cliente N° {indice} | Conta: {contas2[indice]} | Saldo: {saldos2[indice]}')


def Montante(tipo):
    montante = 0
    saldos = acessar_lista("dados json/saldos.json")
    if tipo == "Agencia":
        agencia = int(input('N° da agência: '))
        if agencia == 1:
            saldos1 = saldos[:3]
            for saldo in saldos1:
                montante += saldo
            print(f'Montante da Agência 001 = R${montante}')
        elif agencia == 2:
            saldos2 = saldos[3:]
            for saldo in saldos2:
                montante += saldo
            print(f'Montante da Agência 002 = R${montante}')

            
    elif tipo == "Banco":
        montante = 0
        for saldo in saldos:
            montante += saldo
        print(f'Montante do Banco = R${montante}')
    
