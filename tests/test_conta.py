import pytest
from a_ser_testado import decimal_ao_jeito_brasileiro


'''dois testes nesse arquivo: 
teste 1. se digitar str ao usar a função decimal ao jeito brasileiro, 
retorna ValueError porque só devemos aceitar digitos; então vamos colocar valores "invalidos"'''
@pytest.mark.parametrize("texto", ["abc", "", "   ", "R$10", "10,5,3", "1.000,50"]) #testando o parametrize sendo uma lista

def test_confere_se_input_invalido_levanta_value_error(texto):
    with pytest.raises(ValueError): #tem no colab, para verificar exceções
        decimal_ao_jeito_brasileiro(texto)

'''teste 2: se a função decimal ao jeito brasileiro funciona mesmo e transforma os números com vírgula em decimais com ponto e
também conferir se vai tirar os espaços digitados, deixando só os dígitos'''
@pytest.mark.parametrize("texto, esperado", [
    ("50",   50.0),
    ("50,00", 50.0),
    ("50.5", 50.5),
    ("50,5", 50.5),
    (" 50 ", 50.0),
    ("0",    0.0),
    ("-10", -10.0),
])

def test_decimal_valido_converte(texto, esperado):
    assert decimal_ao_jeito_brasileiro(texto) == pytest.approx(esperado) 
#approx do colab de Yoshiaki: importante para quando trabalhar com float