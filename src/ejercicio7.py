"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

#Define la funcion llamada 'tabla_de_multiplicar' que no toma argumentos.
def tabla_de_multiplicar():
    #Crea una lista de listas que representa las tablas de multiplicar del 1 al 10.
    return [[f"{i} x {j} = {i*j}" for j in range(1, 11)] + [''] for i in range(1, 11)]


if __name__ == "__main__":
    
    #Llama a la funcion 'tabla_de_multiplicar' y almacena los resultados en la variable 'resultados'.
    resultados = tabla_de_multiplicar()
    
    #Itera a traves de las tablas de multiplicar.
    for tabla in resultados:
        #Imprime cada multiplicacion en una nueva linea.
        print('\n'.join(tabla))
        
        #Imprime una linea en blanco para separar las tablas.
        print()