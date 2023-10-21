from src.ejercicio22 import contar_digitos_pares_impares

def test_contar_digitos_pares_impares():
    assert contar_digitos_pares_impares(12345) == (2, 3)
    assert contar_digitos_pares_impares(24680) == (5, 0)
    assert contar_digitos_pares_impares(11111) == (0, 5)
    assert contar_digitos_pares_impares(0) == (1, 0)
    assert contar_digitos_pares_impares(13579) == (0, 5)