"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados."""
    
#Define la funcion llamada 'sumatoria_numeros_positivos' que no toma argumentos.
def sumatoria_numeros_positivos():
    suma = 0  # Inicializa la variable 'suma' para acumular la suma de los numeros positivos.
    numero = -1  #Inicializa la variable 'numero' con un valor no cero para comenzar el bucle.

    while numero != 0:  #Inicia un bucle que se ejecuta mientras 'numero' no sea cero.
        entrada = input("Ingresa un número entero (o ingresa 0 para terminar): ")

        if entrada.isdigit():  #Verifica si la entrada es un numero entero.
            numero = int(entrada)  #Convierte la entrada en un numero entero y lo asigna a 'numero'.

            if numero > 0:
                suma += numero  #Si el numero es positivo, lo suma a la variable 'suma'.
        else:
            print("Por favor, ingresa solo números enteros.")

    return suma


if __name__ == "__main__":
    
    #Llama a la funcion 'sumatoria_numeros_positivos' e imprime el resultado.
    print(f"La sumatoria de los números positivos ingresados es: {sumatoria_numeros_positivos()}")