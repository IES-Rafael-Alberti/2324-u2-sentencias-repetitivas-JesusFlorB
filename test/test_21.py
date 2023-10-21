from src.ejercicio21 import calcular_total_compra

def test_calcular_total_compra():
    assert calcular_total_compra([500, 300, 200]) == 1000
    assert calcular_total_compra([100, 200, 300]) == 600
    assert calcular_total_compra([]) == 0