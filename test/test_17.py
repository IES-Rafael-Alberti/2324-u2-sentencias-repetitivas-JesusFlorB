from src.ejercicio17 import suma_digitos

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(9876) == 30
    assert suma_digitos(0) == 0
    assert suma_digitos(1) == 1
    assert suma_digitos(999999) == 54