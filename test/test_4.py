from src.ejercicio4 import cuenta_atras_desde_n

def test_cuenta_atras_desde_n():
    assert cuenta_atras_desde_n(3) == "Cuenta atras desde 3 hasta 0: 3, 2, 1, 0"
    
    assert cuenta_atras_desde_n(0) == "Cuenta atras desde 0 hasta 0: 0"
    
    assert cuenta_atras_desde_n(5) == "Cuenta atras desde 5 hasta 0: 5, 4, 3, 2, 1, 0"