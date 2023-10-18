"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Ingresa un numero entero: "))

    if es_primo(num):
        print(f"{num} es un numero primo.")
    else:
        print(f"{num} no es un numero primo.")