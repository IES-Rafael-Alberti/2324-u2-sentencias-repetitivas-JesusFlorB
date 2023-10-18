"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase."""

def contar_letras(frase, letra):
    return frase.count(letra)

if __name__ == "__main__":
    
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")

    if len(letra) == 1:
        resultado = contar_letras(frase, letra)
        print(f'La letra "{letra}" aparece {resultado} veces en la frase.')
    else:
        print("Por favor, ingresa solo una letra.")