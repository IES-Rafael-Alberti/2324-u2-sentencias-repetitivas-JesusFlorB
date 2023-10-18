"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última."""

def mostrar_letras_inverso():
    palabra = input("Por favor, ingresa una palabra: ")
    
    if palabra.isalpha():
        for letra in reversed(palabra):
            print(letra)
    else:
        print("Por favor, ingresa solo letras.")

if __name__ == "__main__":
    
    mostrar_letras_inverso()