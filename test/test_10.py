# Importa la función que quieres probar
from src.ejercicio10 import es_primo

def test_es_primo_primo():
    assert es_primo(17) == True

def test_es_primo_compuesto():
    assert es_primo(20) == False

def test_es_primo_negativo():
    assert es_primo(-7) == False

def test_es_primo_cero():
    assert es_primo(0) == False

def test_es_primo_uno():
    assert es_primo(1) == False