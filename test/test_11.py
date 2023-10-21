from src.ejercicio11 import mostrar_letras_inverso
from io import StringIO
import sys

def simular_entrada(entrada):
    sys.stdin = StringIO(entrada)

def test_mostrar_letras_inverso_hola():
    simular_entrada("hola\n")
    mostrar_letras_inverso()