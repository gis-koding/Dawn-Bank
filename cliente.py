def CadastroCliente():
    nome = input()
    cpf = input()
    return nome,cpf 

def ValidarCPF(cpf):
    cpf = cpf.replace(".","").replace("-","").replace(" ", "")
    if len(cpf) != 11 or not cpf.isdigit():
    	return False
    
    d1 = int(cpf[0]); d2 = int(cpf[1]); d3 = int(cpf[2])
    d4 = int(cpf[3]); d5 = int(cpf[4]); d6 = int(cpf[5])
    d7 = int(cpf[6]); d8 = int(cpf[7]); d9 = int(cpf[8])
    d10 = int(cpf[9]); d11 = int(cpf[10])
        
    if not (d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8 == d9 == d10 == d11): 
        soma1 = ((d1*10) + (d2*9) + (d3*8) + (d4*7) + (d5*6) + (d6*5) + (d7*4) + (d8*3) + (d9*2)) 
        resto1 = soma1 % 11 
        if resto1 < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto1
        
        soma2 = ((d1*11) + (d2*10) + (d3*9) + (d4*8) + (d5*7) + (d6*6) + (d7*5) + (d8*4) + (d9*3) + (d10*2)) 
        resto2 = soma2 % 11
        if resto2 < 2:
        	digito2 = 0
        else:
        	digito2 = 11 - resto2
        
        if digito1 == d10 and digito2 == d11:
        	return True
        else:
        	return False
    else:
        return False
