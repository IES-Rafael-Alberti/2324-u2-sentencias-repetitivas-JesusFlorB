from src.ejercicio6 import imprimir_triangulo_rectangulo

def test_imprimir_triangulo_rectangulo(capfd):
    imprimir_triangulo_rectangulo(3)
    out, _ = capfd.readouterr()
    assert out == '*\n**\n***\n'

    imprimir_triangulo_rectangulo(5)
    out, _ = capfd.readouterr()
    assert out == '*\n**\n***\n****\n*****\n'