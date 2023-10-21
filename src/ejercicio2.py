"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

#Define la funcion 'mostrar_años_cumplidos' que toma el argumento 'edad'.
def mostrar_años_cumplidos(edad):
    print("Años cumplidos:")
    años_cumplidos = []  #Inicializa una lista vacia llamada 'años_cumplidos'.
    
    for i in range(1, edad + 1):  #Itera desde 1 hasta la edad ingresada por el usuario, incluyendo la edad.
        años_cumplidos.append(i)  #Agrega cada numero a la lista 'años_cumplidos'.
    
    return años_cumplidos

if __name__ == "__main__":

    edad = int(input("Por favor, ingresa tu edad: "))
    
    # Llama a la funcion 'mostrar_años_cumplidos' pasando la edad ingresada.
    print(mostrar_años_cumplidos(edad))