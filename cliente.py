from biblioteca import *

#ADAPTAÇÃO: dicionário
def AdicionarCliente(nome,cpf):
    clientes = acessar_dados("clientes")
    clientes[cpf] = [nome]
    salvar_dados(clientes,"clientes")

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
    return nome,cpf #para servir pra criar a conta - f: AdicionarConta()

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

#ATUALIZAÇÃO: dicionario
def ListarClientes():
    clientes = acessar_dados("clientes")
    if clientes == {}:
        print ("nenhum cliente cadastrado") #só para dizer 
    else:
        #"cpf": [nome,conta]
        cpfs = clientes.keys()
        contador = 0
        for cpf in cpfs:
            contador += 1
            dados = clientes.get(cpf)
            nome = dados[0]
            conta = dados[1]
            
            print(f"Cliente N°: {contador} | Nome do cliente: {nome} | CPF: {cpf} | N° da Conta: {conta}")
    


#tupla: posicao, nome cpf, 0 1 2
'''for indice in range(len(listadosnomes)):
        print(f"Posição {indice} | Nome do cliente {listadosnomes[indice]} | CPF do cliente: {listadoscpfs[indice]}""")
        obs: quando a ideia era listas separadas'''
