import json

#Lembrete: Alterar todo acessar_lista por acessar_dados

def salvar_dados(dicti,nome_arquivo):

    #sao dois arquivos, logo, se nao for um é outro
    if nome_arquivo == "clientes":
        arquivo_json = "dados json/clientes.json"
    else:
        arquivo_json = "dados json/contas.json"
        
    with open(arquivo_json, "w", encoding="utf-8") as arquivo: 
        #o w é write: escrever e o utf mantem a formatação
        json.dump(dicti, arquivo, ensure_ascii=False)
        #o dump escreve
        #o ensure ascii mantém acentos e formatação no arq json q será criado



def acessar_dados(nome_arquivo): #antigo acessar_lista, p/ carregar json

    #para nao escrever o caminho toda hora
    if nome_arquivo == "clientes":
        arquivo_json = "dados json/clientes.json"
    else:
        arquivo_json = "dados json/contas.json"

    #carregar dicionario
    with open(arquivo_json, "r",encoding="utf-8") as arquivo: #ajuste aqui para acessar a pasta
        dicti = json.load(arquivo) #load = le o arqv json
    return dicti



def apagar_dados():
    #botao de autodestruicao do banco de dados inteiro :D
    clientes = acessar_dados("clientes")
    contas = acessar_dados("contas")
    clientes.clear()
    contas.clear()
    
    salvar_dados(clientes,"clientes")
    salvar_dados(contas,"contas")
    #deixa uma estrutura vazia pra nao dar erro
    print("Todos os dados excluídos com sucesso!")
    


'''def ProcurarCpf(cpf):
    #pega a posicao que o cpf esta na lista
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return indice
       
    #lembrando: tupla (posicao, nome cpf) 0 1 2'''



'''def VerificarCliente(cpf):
    clientes = acessar_lista("dados json/clientes.json") #json dos clientes
    for indice in range(len(clientes)):
        if clientes[indice][2] == cpf:
            return True
    return False #não existe'''


#salva o saldo no json
def salvar_saldo(conta,saldo):
    contas = acessar_dados("contas") #retorna o dicionario c as contas
    dadosconta = contas.get(conta) #lista com os dados da conta
    dadosconta[3] = saldo #apaga o saldo anterior e substitui pelo novo
    contas[conta] = dadosconta
    salvar_dados(contas,"contas")
    

'''def ListarAgencias():
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
            print(f'Cliente N° {indice} | Conta: {contas2[indice]} | Saldo: {saldos2[indice]}')'''


'''def Montante(tipo):
    montante = 0
    saldos = acessar_lista("dados json/saldos.json")

    #montante da agencia
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
            
    #montante geral
    elif tipo == "Banco":
        montante = 0
        for saldo in saldos:
            montante += saldo
        print(f'Montante do Banco = R${montante}')'''
    
