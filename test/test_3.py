from src.ejercicio3 import numeros_impares_hasta_n

def test_numeros_impares_hasta_n():
    assert numeros_impares_hasta_n(5) == "Numeros impares desde 1 hasta 5: 1, 3, 5"
    
    assert numeros_impares_hasta_n(0) == "Numeros impares desde 1 hasta 0: "
    
    assert numeros_impares_hasta_n(1) == "Numeros impares desde 1 hasta 1: 1"
    
    assert numeros_impares_hasta_n(10) == "Numeros impares desde 1 hasta 10: 1, 3, 5, 7, 9"