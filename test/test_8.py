from src.ejercicio8 import imprimir_triangulo_rectangulo

def test_imprimir_triangulo_rectangulo(capfd):
    imprimir_triangulo_rectangulo(5)
    out, _ = capfd.readouterr()
    assert out == '1 \n3 1 \n5 3 1 \n'

    imprimir_triangulo_rectangulo(7)
    out, _ = capfd.readouterr()
    assert out == '1 \n3 1 \n5 3 1 \n7 5 3 1 \n'

    imprimir_triangulo_rectangulo(1)
    out, _ = capfd.readouterr()
    assert out == '1 \n'