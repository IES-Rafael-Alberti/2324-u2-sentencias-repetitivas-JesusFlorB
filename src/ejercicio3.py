"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas."""

def numeros_impares_hasta_n(n):
    impares = [str(i) for i in range(1, n+1, 2)]
    resultado = ", ".join(impares)
    return f"Numeros impares desde 1 hasta {n}: {resultado}"

if __name__ == "__main__":
    
    n = int(input("Por favor, ingresa un numero entero positivo: "))
    print(numeros_impares_hasta_n(n))