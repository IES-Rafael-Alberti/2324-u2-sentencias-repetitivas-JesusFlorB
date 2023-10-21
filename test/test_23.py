from src.ejercicio23 import contar_digitos

def test_contar_digitos():
    assert contar_digitos("Libro123") == 3
    assert contar_digitos("Libro4567") == 4
    assert contar_digitos("NoDigitos") == 0
    assert contar_digitos("") == 0
    assert contar_digitos("999999999") == 9