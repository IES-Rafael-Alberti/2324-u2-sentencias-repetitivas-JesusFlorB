"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números ingresados."""

def sumatoria_numeros():
    suma = 0
    numero = -1

    while numero != 0:
        entrada = input("Ingresa un numero entero (o ingresa 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)
            suma += numero
        else:
            print("Por favor, ingresa solo numeros.")
    return suma

if __name__ == "__main__":
    
    print(f"La sumatoria de los numeros ingresados es: {sumatoria_numeros()}")