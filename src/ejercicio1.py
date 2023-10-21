"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

#Funcion que imprime una palabra 10 veces.
def imprimir_palabra_10_veces(palabra):
    for _ in range(10):
        print(palabra)

if __name__ == "__main__":
    
    palabra_usuario = input("Por favor, ingresa una palabra: ")
    
    #Llama a la funcion para imprimir la palabra ingresada por el usuario 10 veces.
    imprimir_palabra_10_veces(palabra_usuario)