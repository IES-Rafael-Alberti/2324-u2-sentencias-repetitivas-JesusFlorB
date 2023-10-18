"""Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución."""

def buscar_letra(frase, letra):
    for i, caracter in enumerate(frase):
        if caracter == letra:
            print(f"Se encontro la letra '{letra}' en la posicion {i + 1}.")
            return
        else:
            print(f"No hay coincidencia en la posicion {i + 1}.")

if __name__ == "__main__":
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")

    if len(letra) == 1:
        buscar_letra(frase, letra)
    else:
        print("Por favor, ingresa solo una letra.")