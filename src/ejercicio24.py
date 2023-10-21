"""Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados."""

#Define la funcion llamada 'es_primo', que toma un 'numero' como argumento.
def es_primo(numero):
    if numero < 2:  #Si el numero es menor que 2, no es primo.
        return False
    for i in range(2, int(numero**0.5) + 1):  #Itera sobre los numeros desde 2 hasta la raiz cuadrada del numero + 1.
        if numero % i == 0:  #Si el numero es divisible por 'i', no es primo.
            return False
    return True  #Si el bucle termina sin encontrar un divisor, el numero es primo.

if __name__ == "__main__":
    
    cantidad_primos = 0  #Inicializa la variable 'cantidad_primos' para contar la cantidad de numeros primos.
    terminado = False  #Inicializa la variable 'terminado' como False para controlar el bucle.

    while not terminado:  #Inicia un bucle que se ejecuta mientras 'terminado' sea False.
        entrada = input("Ingresa un numero mayor que 1 (o 0 para terminar): ")

        if entrada.isdigit():  #Verifica si la entrada es un numero.
            numero = int(entrada)  #Convierte la entrada en un entero y lo asigna a 'numero'.

            if numero == 0:  #Si el numero es cero, termina el bucle.
                terminado = True
            elif numero <= 1:  #Si el numero es menor o igual a uno, no es primo.
                print("El numero debe ser mayor que 1.")
            else:
                if es_primo(numero):  #Verifica si el número es primo utilizando la función 'es_primo'.
                    cantidad_primos += 1  #Si es primo, incrementa el contador de numeros primos.
        else:
            print("Por favor, ingresa solo numeros.")

    print(f"Se ingresaron {cantidad_primos} numeros primos.")