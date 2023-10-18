"""Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados."""

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    
    cantidad_primos = 0
    terminado = False
    
    while not terminado:
        entrada = input("Ingresa un numero mayor que 1 (o 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)

            if numero == 0:
                terminado = True
            elif numero <= 1:
                print("El numero debe ser mayor que 1.")
            else:
                if es_primo(numero):
                    cantidad_primos += 1
        else:
            print("Por favor, ingresa solo numeros.")

    print(f"Se ingresaron {cantidad_primos} numeros primos.")
