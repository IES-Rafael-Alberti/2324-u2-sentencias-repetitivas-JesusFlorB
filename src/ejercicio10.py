"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

#Define la funcion llamada 'es_primo' que toma el argumento 'numero'.
def es_primo(numero):
    if numero < 2:  #Si el numero es menor que 2, no es primo.
        return False
    for i in range(2, int(numero**0.5) + 1):  #Itera a traves de los numeros desde 2 hasta la raiz cuadrada de 'numero'.
        if numero % i == 0:  #Si 'numero' es divisible por 'i', no es primo.
            return False
    return True  #Si no se encontraron divisores, 'numero' es primo.


if __name__ == "__main__":
    
    num = int(input("Ingresa un numero entero: "))

    if es_primo(num):  #Llama a la funcion 'es_primo' con el numero ingresado y verifica el resultado.
        print(f"{num} es un numero primo.")
    else:
        print(f"{num} no es un numero primo.")