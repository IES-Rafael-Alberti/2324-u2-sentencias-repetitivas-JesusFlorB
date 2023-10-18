import builtins
from src.ejercicio14 import sumatoria_numeros

def test_sumatoria_numeros(monkeypatch):
    input_values = ['4', '3', '2', '0']
    monkeypatch.setattr(builtins, 'input', lambda _: input_values.pop(0))

    assert sumatoria_numeros() == 9