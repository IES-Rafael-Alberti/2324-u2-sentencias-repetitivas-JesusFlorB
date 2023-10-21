"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
hasta que el usuario escriba “salir” que terminará."""

#Define la función llamada 'eco' que no toma argumentos.
def eco():
    entrada = ""  #Inicializa una variable 'entrada' como una cadena vacía.
    while entrada.lower() != "salir":  #Inicia un bucle que se ejecuta mientras el valor de 'entrada' no sea "salir".
        entrada = input("Escribe algo (o escribe 'salir' para terminar): ")
        if entrada.lower() != "salir":  #Verifica si el usuario no ha ingresado "salir".
            print(entrada)  # Si no ha ingresado "salir", imprime el contenido de 'entrada'.


if __name__ == "__main__":
    
    eco()  # Llama a la funcion 'eco' para iniciar el proceso.