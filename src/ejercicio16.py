"""Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado."""

def encontrar_mayor():
    mayor = 0
    numero = -1

    while numero != 0:
        entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)

            if numero > 0:
                if numero > mayor:
                    mayor = numero
                else:
                    print(f"{numero} no es mayor que {mayor}.")
        else:
            print("Por favor, ingresa solo numeros enteros positivos.")

    if mayor != 0:
        print(f"El mayor numero ingresado fue: {mayor}")
    else:
        print("No se ingresaron numeros positivos.")

if __name__ == "__main__":
    
    encontrar_mayor()