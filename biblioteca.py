import json

#Lembrete: Alterar todo acessar_lista por acessar_dados
#Já que agora podemos usar dicionário e digitar "clientes" ou cliente estava causando problema:

caminhos = {
    "clientes": "dados json/clientes.json",
    "contas": "dados json/contas.json"
}

def salvar_dados(dicti,nome_arquivo):
    if nome_arquivo not in caminhos:
        print(f"Erro: '{nome_arquivo} não é um arquivo reconhecido")
        return 
    #sao dois arquivos, verifico no dicionário
        
    with open(caminhos[nome_arquivo], "w", encoding="utf-8") as arquivo: 
        #o w é write: escrever e o utf mantem a formatação
        json.dump(dicti, arquivo, ensure_ascii=False)
        #o dump escreve
        #o ensure ascii mantém acentos e formatação no arq json q será criado
        #a lógica usada: para evitar erros, coloco o caminho no dicionário e pegamos o valor dessa chave em específico


def acessar_dados(nome_arquivo): #antigo acessar_lista, p/ carregar json
    if nome_arquivo not in caminhos:
        print(f"Erro: '{nome_arquivo}' não é um arquivo reconhecido")
        return {}
    #carregar dicionario 
    with open(caminhos[nome_arquivo], "r",encoding="utf-8") as arquivo:
        return json.load(arquivo) #load = le o arqv json



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
    
