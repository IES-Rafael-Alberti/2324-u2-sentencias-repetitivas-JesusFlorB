"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados."""
    
def sumatoria_numeros_positivos():
    suma = 0
    numero = -1

    while numero != 0:
        entrada = input("Ingresa un número entero (o ingresa 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)

            if numero > 0:
                suma += numero
        else:
            print("Por favor, ingresa solo números enteros.")

    return suma

if __name__ == "__main__":
    print(f"La sumatoria de los números positivos ingresados es: {sumatoria_numeros_positivos()}")