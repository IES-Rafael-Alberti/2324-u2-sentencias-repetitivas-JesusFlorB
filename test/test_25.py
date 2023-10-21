from src.ejercicio25 import encontrar_palabra_mas_larga, contar_palabras

def test_encontrar_palabra_mas_larga():
    assert encontrar_palabra_mas_larga("Hola me llamo jesus") == "llamo"
    assert encontrar_palabra_mas_larga("Soy del turno de mañana") == "mañana"
    assert encontrar_palabra_mas_larga("") == ""

def test_contar_palabras():
    assert contar_palabras("Esto es una prueba") == 4
    assert contar_palabras("Una") == 1
    assert contar_palabras("") == 0