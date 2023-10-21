from src.ejercicio1 import imprimir_palabra_10_veces

def test_imprimir_palabra_10_veces(capsys):
    imprimir_palabra_10_veces("Hola")

    captured = capsys.readouterr()
    assert captured.out == "Hola\n" * 10