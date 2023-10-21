from unittest.mock import patch
from src.ejercicio9 import verificar_contraseña

def test_verificar_contraseña_correcta():
    with patch('builtins.input', return_value="contraseña"):
        assert verificar_contraseña() is None

def test_verificar_contraseña_incorrecta():
    with patch('builtins.input', side_effect=["incorrecta", "contraseña"]):
        assert verificar_contraseña() is None
