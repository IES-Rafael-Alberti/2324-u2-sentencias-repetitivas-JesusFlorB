"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas."""

#Define la funcion llamada 'numeros_impares_hasta_n' que toma el argumento 'n'.
def numeros_impares_hasta_n(n):
    #Crea una lista de numeros impares hasta 'n' como cadenas de texto.
    impares = [str(i) for i in range(1, n+1, 2)]
    
    #Convierte la lista de numeros impares en una cadena separada por comas.
    resultado = ", ".join(impares)
    
    #Retorna un mensaje que indica los numeros impares hasta 'n'.
    return f"Numeros impares desde 1 hasta {n}: {resultado}"


if __name__ == "__main__":
    
    n = int(input("Por favor, ingresa un numero entero positivo: "))
    
    #Llama a la funcion 'numeros_impares_hasta_n' pasando 'n' y luego imprime el resultado.
    print(numeros_impares_hasta_n(n))