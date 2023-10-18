"""Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen."""

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

if __name__ == "__main__":
    
    entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

    while not (entrada.isdigit() and int(entrada) >= 0):
        print("Por favor, ingresa solo numeros enteros positivos.")
        entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

    numero = int(entrada)

    if numero > 0:
        resultado = suma_digitos(numero)
        print(f"La suma de los digitos de {numero} es: {resultado}")
    else:
        print("No se ingresaron numeros positivos.")