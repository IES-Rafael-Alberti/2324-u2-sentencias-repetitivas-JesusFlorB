"""Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución."""

#Define la función llamada 'buscar_letra' que toma dos argumentos: 'frase' y 'letra'.
def buscar_letra(frase, letra):
    i = 0  #Inicializa una variable 'i' para rastrear la posicion en la frase.

    while i < len(frase):  #Inicia un bucle que se ejecuta mientras 'i' sea menor que la longitud de la frase.
        if frase[i] == letra:  #Verifica si el caracter en la posicion 'i' de la frase es igual a la 'letra'.
            return f"Se encontro la letra '{letra}' en la posicion {i + 1}."
        else:
            i += 1  #Si no encuentra la letra, incrementa 'i' para revisar el siguiente caracter.

    return f"No hay coincidencia en la frase."


if __name__ == "__main__":

    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")

    if len(letra) == 1:  #Verifica si la 'letra' tiene una longitud de 1.
        resultado = buscar_letra(frase, letra)  #Llama a la funcion 'buscar_letra' para buscar la letra en la frase.
        print(resultado)  #Imprime el resultado.
    else:
        print("Por favor, ingresa solo una letra.")