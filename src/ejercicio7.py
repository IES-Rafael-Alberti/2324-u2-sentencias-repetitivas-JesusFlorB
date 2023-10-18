"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

def tabla_de_multiplicar():
    resultados = []
    for i in range(1, 11):
        tabla = []
        for j in range(1, 11):
            resultado = i * j
            tabla.append(f"{i} x {j} = {resultado}")
        resultados.append(tabla)
        resultados.append([''])
    return resultados

if __name__ == "__main__":
    
    resultados = tabla_de_multiplicar()
    for tabla in resultados:
        for multiplicacion in tabla:
            print(multiplicacion)
        print()