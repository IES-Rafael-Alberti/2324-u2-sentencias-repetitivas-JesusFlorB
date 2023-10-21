from src.ejercicio5 import calcular_interes_compuesto

def test_calcular_interes_compuesto():
    assert calcular_interes_compuesto(1000, 5, 2) == ['Año 1: 1050.00', 'Año 2: 1102.50']