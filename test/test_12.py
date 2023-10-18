from src.ejercicio12 import contar_letras

def test_contar_letras():
    assert contar_letras("Hello World", "l") == 3

def test_contar_letras_letra_no_presente():
    assert contar_letras("Hola", "x") == 0