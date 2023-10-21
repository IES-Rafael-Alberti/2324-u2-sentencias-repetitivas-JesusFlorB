import sys
from io import StringIO
from src.ejercicio13 import eco

def simular_entrada(entrada):
    sys.stdin = StringIO(entrada)

def capturar_salida():
    captura = StringIO()
    sys.stdout = captura
    return captura.getvalue().strip()

def test_eco_sin_entrada():
    simular_entrada("salir\n")
    eco()
    assert capturar_salida() == ""