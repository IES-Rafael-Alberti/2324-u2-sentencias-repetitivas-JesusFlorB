"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

def mostrar_años_cumplidos(edad):
    print("Años cumplidos:")
    años_cumplidos = []
    for i in range(1, edad + 1):
        años_cumplidos.append(i)
    return años_cumplidos

if __name__ == "__main__":
    
    edad = int(input("Por favor, ingresa tu edad: "))
    print(mostrar_años_cumplidos(edad))