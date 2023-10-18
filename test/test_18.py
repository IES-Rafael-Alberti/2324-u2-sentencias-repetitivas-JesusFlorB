from src.ejercicio18 import suma_digitos, analizar_numero

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(9876) == 30
    assert suma_digitos(0) == 0

def test_analizar_numero():
    assert analizar_numero("-123") == False
    assert analizar_numero("abc") == False