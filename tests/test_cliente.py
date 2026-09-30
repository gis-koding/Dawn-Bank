import pytest
from cliente import ValidarCPF
from biblioteca import * 
from conta import PrimeiroAcesso
#importando as funções json 
#obs importante: os testes falham quando a função tem input ! o ideal é testar nas funções sem input
     
'''o teste 1 será feito nos casos: numeros repetidos, 
digitos e letras juntos, colocado menos de 11 digitos ou mais que 11 digitos, colocado str vazia
porque não faz sentido testar com os dados do json, todos seriam válidos (True)'''
# o teste já foi testado, os 7 casos passaram
@pytest.mark.parametrize("cpf, esperado", [ 
    ("345.833.790-30", True),
    ("111.111.111-11", False),
    ("123.abc.123-12", False),
    ("1234", False),
    ("123.456.789.101-2", False),
    ("", False),
    ("627.077.475-64", True),
])

def test_Validar_CPF_por_parametrizar(cpf, esperado):
    assert ValidarCPF(cpf) == esperado