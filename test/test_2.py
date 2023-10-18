from src.ejercicio2 import mostrar_años_cumplidos

def test_mostrar_años_cumplidos(capsys):
    mostrar_años_cumplidos(5)

    captured = capsys.readouterr()
    assert captured.out == "Años cumplidos:\n"

def test_mostrar_años_cumplidos_lista():
    assert mostrar_años_cumplidos(5) == [1, 2, 3, 4, 5]

    assert mostrar_años_cumplidos(0) == []

    assert mostrar_años_cumplidos(1) == [1]