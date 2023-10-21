"""Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. 
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares."""

#Define la funcion llamada 'suma_digitos' que toma el argumento 'numero'.
def suma_digitos(numero):
    suma = 0  #Inicializa la variable 'suma' para acumular la suma de los digitos.

    #Itera a traves de cada digito en el numero convertido a cadena.
    for digito in str(numero):
        suma += int(digito)  #Convierte el digito de vuelta a entero y lo suma a la variable 'suma'.

    return suma

#Define la funcion llamada 'analizar_numero' que toma el argumento 'entrada'.
def analizar_numero(entrada):
    if entrada.isdigit() and int(entrada) >= 0:  #Verifica si la entrada es un numero entero positivo.
        numero = int(entrada)  #Convierte la entrada en un numero entero.
        resultado = suma_digitos(numero)  #Llama a la funcion 'suma_digitos' para obtener la suma.
        print(f"La suma de los digitos de {numero} es: {resultado}")
        return numero % 2 == 0  #Retorna True si el numero es par, False si es impar.
    else:
        print("Por favor, ingresa solo numeros enteros positivos.")
        return False  #Retorna False para indicar que el numero no es par.

#Define la funcion llamada 'analizar_numeros'.
def analizar_numeros():
    numeros_pares = 0  #Inicializa una variable para rastrear la cantidad de numeros pares.
    entrada = None  #Inicializa la entrada como None.

    while entrada != "-1":  #Inicia un bucle que se ejecuta mientras la entrada no sea "-1".
        entrada = input("Ingresa un numero entero positivo (o -1 para terminar): ")
        
        if entrada != "-1":  #Verifica si la entrada no es "-1".
            if analizar_numero(entrada):  #Llama a la funcion 'analizar_numero' para verificar y analizar el numero.
                numeros_pares += 1  #Si el numero es par, incrementa el contador de numeros pares.

    print(f"Se ingresaron {numeros_pares} numeros pares.")


if __name__ == "__main__":
    
    analizar_numeros()  #Llama a la funcion 'analizar_numeros' para iniciar el proceso.