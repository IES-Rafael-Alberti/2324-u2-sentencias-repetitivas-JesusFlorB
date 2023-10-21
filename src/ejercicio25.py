"""Solicitar al usuario que ingrese una frase y luego informar cuál fue 
la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más."""

#Define la funcion llamada 'encontrar_palabra_mas_larga', que toma una 'frase' como argumento.
def encontrar_palabra_mas_larga(frase):
    palabras = frase.split()  #Divide la 'frase' en una lista de palabras.
    palabra_mas_larga = ""  #Inicializa una cadena vacia llamada 'palabra_mas_larga'.
    i = 0  #Inicializa un indice 'i' para iterar sobre las palabras.

    while i < len(palabras):  #Inicia un bucle que se ejecuta mientras 'i' sea menor que la cantidad de palabras.
        if len(palabras[i]) > len(palabra_mas_larga):  #Compara la longitud de la palabra actual con la mas larga encontrada.
            palabra_mas_larga = palabras[i]  #Si la palabra actual es mas larga, actualiza 'palabra_mas_larga'.
        i += 1  #Incrementa el indice 'i' para pasar a la siguiente palabra.

    return palabra_mas_larga

#Define la funcion llamada 'contar_palabras', que toma una 'frase' como argumento.
def contar_palabras(frase):
    palabras = frase.split()  #Divide la 'frase' en una lista de palabras.
    return len(palabras)  #Retorna el numero de palabras en la frase.

#Define la funcion llamada 'main', que no toma argumentos.
def main():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()  #Divide la 'frase' en una lista de palabras.

    if palabras:  #Verifica si hay al menos una palabra en la frase.
        palabra_mas_larga = encontrar_palabra_mas_larga(frase)  #Encuentra la palabra mas larga utilizando la funcion 'encontrar_palabra_mas_larga'.
        cantidad_palabras = contar_palabras(frase)  #Cuenta el numero de palabras utilizando la funcion 'contar_palabras'.
        print(f"La palabra mas larga es: {palabra_mas_larga}")
        print(f"La cantidad de palabras en la frase es: {cantidad_palabras}")
    else:
        print("No se ingresaron palabras en la frase.")


if __name__ == "__main__":
    
    main()  #Llama a la funcion 'main' para iniciar el proceso.