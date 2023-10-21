"""Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen."""

#Define la funcion llamada 'suma_digitos' que toma el argumento 'numero'.
def suma_digitos(numero):
    suma = 0  #Inicializa la variable 'suma' para acumular la suma de los digitos.

    #Itera a traves de cada digito en el numero convertido a cadena.
    for digito in str(numero):
        suma += int(digito)  #Convierte el digito de vuelta a entero y lo suma a la variable 'suma'.

    return suma


if __name__ == "__main__":
    
    entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

    #Verifica si la entrada es un numero entero positivo.
    while not (entrada.isdigit() and int(entrada) >= 0):
        print("Por favor, ingresa solo numeros enteros positivos.")
        entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

    numero = int(entrada)  #Convierte la entrada a un número entero.

    if numero > 0:
        resultado = suma_digitos(numero)  #Llama a la funcion 'suma_digitos' para obtener la suma de los digitos.
        print(f"La suma de los digitos de {numero} es: {resultado}")
    else:
        print("No se ingresaron numeros positivos.")