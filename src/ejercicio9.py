"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

#Define la funcion llamada 'verificar_contraseña' que no toma argumentos.
def verificar_contraseña():
    contraseña_correcta = "contraseña"

    while True:  #Inicia un bucle infinito.
        contraseña_ingresada = input("Por favor, ingresa la contraseña: ")

        if contraseña_ingresada == contraseña_correcta:  #Compara la contraseña ingresada con la contraseña correcta.
            print("¡Contraseña correcta! Acceso concedido.")
            return
        else:
            print("Contraseña incorrecta. Por favor, intentalo de nuevo.")


if __name__ == "__main__":
    
    verificar_contraseña()  #Llama a la funcion 'verificar_contraseña'.
