"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

def verificar_contraseña():
    contraseña_correcta = "contraseña"
    
    while True:
        contraseña_ingresada = input("Por favor, ingresa la contraseña: ")
        
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta! Acceso concedido.")
            return
        else:
            print("Contraseña incorrecta. Por favor, intentalo de nuevo.")

if __name__ == "__main__":
    
    verificar_contraseña()