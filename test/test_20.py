from src.ejercicio20 import buscar_letra

def test_buscar_letra():
    assert buscar_letra("Hola", "a") == "Se encontro la letra 'a' en la posicion 4."
    assert buscar_letra("Hola", "z") == "No hay coincidencia en la frase."
    assert buscar_letra("", "a") == "No hay coincidencia en la frase."