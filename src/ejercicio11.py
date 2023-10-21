"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última."""

#Define la funcion llamada 'mostrar_letras_inverso' que no toma argumentos.
def mostrar_letras_inverso():
    palabra = input("Por favor, ingresa una palabra: ")
    
    if palabra.isalpha():  #Verifica si la 'palabra' contiene solo letras.
        for letra in reversed(palabra):  #Itera a traves de las letras de la palabra en orden inverso.
            print(letra)  #Devuelve cada letra.

    else:
        print("Por favor, ingresa solo letras.")


if __name__ == "__main__":
    
    mostrar_letras_inverso()  #Llama a la funcion 'mostrar_letras_inverso' para iniciar el proceso.