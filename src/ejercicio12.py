"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase."""

#Define una funcion llamada 'contar_letras' que toma dos argumentos: 'frase' y 'letra'.
def contar_letras(frase, letra):
    return frase.count(letra)  #Usa el metodo 'count' para contar cuantas veces aparece 'letra' en 'frase'.


if __name__ == "__main__":
    
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")

    if len(letra) == 1:  #Verifica si 'letra' es solo un carácter.
        resultado = contar_letras(frase, letra)  #Llama a la funcion 'contar_letras' con 'frase' y 'letra' y almacena el resultado en 'resultado'.
        print(f'La letra "{letra}" aparece {resultado} veces en la frase.')
    else:
        print("Por favor, ingresa solo una letra.")