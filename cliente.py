def CadastroCliente(): #prestar atenção na ordem da chamada da função
    #o cliente 
    nome = input("Nome:")
    cpf = input("CPF: ")
    #caso o cliente digite um cpf inválido:
    while not ValidarCPF(cpf): #not True: False; not False: True! 
        cpf = input ("CPF: ")
    return nome,cpf 

def AdicionaCliente(listadosnomes, listadoscpfs, nome, cpf):
    listadosnomes.append(nome) #adiciona o nome a lista de nomes
    listadoscpfs.append(cpf) #adiciona o cpf a lista do cpf, na ordem.

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

def ListarCliente (listadosnomes, listadoscpfs):
    for indice in range(len(listadosnomes)):
        print(f"Posição {indice} | Nome do cliente {listadosnomes[indice]} | CPF do cliente: {listadoscpfs[indice]}""")