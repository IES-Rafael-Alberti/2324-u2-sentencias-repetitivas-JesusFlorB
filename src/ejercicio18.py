"""Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. 
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares."""

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

def analizar_numero(entrada):
    if entrada.isdigit() and int(entrada) >= 0:
        numero = int(entrada)
        resultado = suma_digitos(numero)
        print(f"La suma de los digitos de {numero} es: {resultado}")
        return numero % 2 == 0
    else:
        print("Por favor, ingresa solo numeros enteros positivos.")
        return False

def analizar_numeros():
    numeros_pares = 0
    entrada = None

    while entrada != "-1":
        entrada = input("Ingresa un numero entero positivo (o -1 para terminar): ")
        
        if entrada != "-1":
            if analizar_numero(entrada):
                numeros_pares += 1

    print(f"Se ingresaron {numeros_pares} numeros pares.")

if __name__ == "__main__":
    
    analizar_numeros()