"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
hasta que el usuario escriba “salir” que terminará."""

def eco():
    entrada = ""
    while entrada.lower() != "salir":
        entrada = input("Escribe algo (o escribe 'salir' para terminar): ")
        if entrada.lower() != "salir":
            print(entrada)

if __name__ == "__main__":
    
    eco()