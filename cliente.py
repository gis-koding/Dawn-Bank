from biblioteca import *

#funcao adaptada para adicionar cliente
def AdicionarCliente(nome,cpf,posicao):
    clientes = acessar_lista("dados json/clientes.json")
    cliente = (posicao,nome,cpf) #tupla !
    clientes.append(cliente)
    salvar_json(clientes,"dados json/clientes.json")

def CadastroCliente(): #prestar atenção na ordem da chamada da função
    #o cliente 
    nome = input("Nome:")
    cpf = input("CPF: ")
    cpf = cpf.replace(".","").replace("-","").replace(" ", "")
    #caso o cliente digite um cpf inválido:
    while not ValidarCPF(cpf) and cpf != "SAIR": #pra parar
    #not True: False; not False: True! 
        cpf = input ("CPF: ")
        cpf = cpf.replace(".","").replace("-","").replace(" ", "") #deixa o cpf so digitos !
    return nome,int(cpf) #para servir pra conta

#função testada!
def ValidarCPF(cpf):
    cpf = cpf.replace(".","").replace("-","").replace(" ", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False #não permitido
    #se for permitido, hora de verificar os dígitos
    digitos = []
    for numero in cpf: 
        digitos.append(int(numero))  #coloco os digitos cpf numa lista
    
    tudo_igual = True #flag, para mudar no for
    for inteiro in digitos:
        if digitos[0] != inteiro: 
            tudo_igual = False #checo se tem digitos diferentes; 
    if tudo_igual: 
        return False #não é válido !
    #primeira verificação, digito1
    soma = 0 
    peso = 10 #faz parte da soma, é 10 e decresce;
    for i in range(0,9): #do 1 ao 9
        soma += digitos[i] * peso
        peso -= 1 #para decrescer o 10
    resto1 = soma % 11 #mesma etapa 
    if resto1 < 2:
        digito1 = 0 #primeiro digito verificador
    else:
        digito1 = 11 - resto1
    
    #segunda verificação, para digito2
    soma2 = 0
    peso2 = 11
    for a in range(0,10):
        soma2 += digitos[a] * peso2
        peso2 -= 1
    resto2 = soma2 % 11 
    if resto2 < 2:
        digito2 = 0 #segundo digito verificador
    else:
        digito2 = 11 - resto2
                
    if digito1 == digitos[9] and digito2 == digitos[10]: #digito 10 e 11
        return True #é válido
    else:
        return False #não é válido

def ListarCliente (): #dessa vez ele não recebe listas
    clientes = acessar_lista("dados json/clientes.json")
    if len(clientes) == 0:
        print ("nenhum cliente cadastrado") #só para dizer 
    else:
        for indice in range(len(clientes)):
            posicao = clientes[indice][0] 
            nome = clientes[indice][1] 
            cpf = clientes[indice][2]
            print(f"Posição: {posicao}, Nome do cliente: {nome}, CPF: {cpf}")
    

    #tupla: posicao, nome cpf, 0 1 2
    '''for indice in range(len(listadosnomes)):
        print(f"Posição {indice} | Nome do cliente {listadosnomes[indice]} | CPF do cliente: {listadoscpfs[indice]}""")
        obs: quando a ideia era listas separadas'''
