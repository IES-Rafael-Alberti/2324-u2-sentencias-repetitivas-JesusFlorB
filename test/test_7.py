from src.ejercicio7 import tabla_de_multiplicar

def test_tabla_de_multiplicar():
    resultados = tabla_de_multiplicar()
    assert len(resultados) == 10

    for i, tabla in enumerate(resultados, start=1):
        assert len(tabla) == 11

        for j, multiplicacion in enumerate(tabla[:-1], start=1):
            assert multiplicacion == f"{i} x {j} = {i*j}"

        assert tabla[-1] == ''