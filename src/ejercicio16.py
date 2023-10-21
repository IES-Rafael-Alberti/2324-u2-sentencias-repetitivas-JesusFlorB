"""Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado."""

#Define la funcion llamada 'encontrar_mayor' que no toma argumentos.
def encontrar_mayor():
    mayor = 0  #Inicializa la variable 'mayor' para rastrear el numero mas grande.
    numero = -1  #Inicializa la variable 'numero' con un valor no cero para comenzar el bucle.

    while numero != 0:  #Inicia un bucle que se ejecuta mientras 'numero' no sea cero.
        entrada = input("Ingresa un numero entero positivo (o ingresa 0 para terminar): ")

        if entrada.isdigit():  #Verifica si la entrada es un numero entero.
            numero = int(entrada)  #Convierte la entrada en un numero entero y lo asigna a la variable 'numero'.

            if numero > 0:
                if numero > mayor:  #Compara el numero con el actual 'mayor'.
                    mayor = numero  #Si el numero es mayor que el actual 'mayor', lo actualiza.
                else:
                    print(f"{numero} no es mayor que {mayor}.")

        else:
            print("Por favor, ingresa solo numeros enteros positivos.")

    if mayor != 0:  #Verifica si se ingresaron numeros positivos.
        print(f"El mayor numero ingresado fue: {mayor}")
    else:
        print("No se ingresaron numeros positivos.")


if __name__ == "__main__":
    
    encontrar_mayor()  #Llama a la funcion 'encontrar_mayor' para iniciar el proceso.