"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

#Define la funcion llamada 'obtener_numero_entero_positivo' que no toma argumentos.
def obtener_numero_entero_positivo():
    while True:  #Inicia un bucle infinito.
        try:  #Intenta ejecutar el siguiente bloque de codigo segun unas condiciones.
            num = int(input("Por favor, ingresa un numero entero positivo: "))
            if num >= 0:
                return num
            else:
                print("El numero debe ser positivo o cero.")
        except ValueError:
            print("Por favor, ingresa un numero entero valido.")

#Define una funcion llamada 'cuenta_atras_desde_n' que toma el argumento 'n'.
def cuenta_atras_desde_n(n):
    cuenta_atras = [str(i) for i in range(n, -1, -1)]  #Crea una lista de numeros en cuenta regresiva desde 'n' hasta 0, como cadenas de texto.
    resultado = ", ".join(cuenta_atras)  #Convierte la lista en una cadena, separando los elementos por comas.
    return f"Cuenta atras desde {n} hasta 0: {resultado}"


if __name__ == "__main__":
    #Llama a la funcion 'obtener_numero_entero_positivo' y almacena el resultado en 'num'.
    num = obtener_numero_entero_positivo()
    
    #Llama a la funcion 'cuenta_atras_desde_n' pasando 'num' y luego imprime el resultado.
    print(cuenta_atras_desde_n(num))