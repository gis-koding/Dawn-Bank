'''
import json 
from biblioteca import *

clientes = ["kalil","andré"]

'''salvar_json(clientes,"agencia01.json")
clientes = carregar_json("agencia01.json")'''

clientes.append("giovanny")

salvar_json(clientes,"agencia01.json")
clientes = carregar_json("agencia01.json")
print(clientes)

l = ['1','2']

for i in l:
    print(int(i))
'''