"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números ingresados."""

#Define la función llamada 'sumatoria_numeros' que no toma argumentos.
def sumatoria_numeros():
    suma = 0  #Inicializa una variable 'suma' con el valor 0 para acumular la suma.
    numero = -1  #Inicializa una variable 'numero' con el valor -1 para iniciar el bucle.

    while numero != 0:  #Inicia un bucle while que se ejecuta mientras 'numero' sea diferente de 0.
        entrada = input("Ingresa un numero entero (o ingresa 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)
            suma += numero  #Acumula la suma con el numero ingresado.
        else:
            print("Por favor, ingresa solo numeros.")

    return suma  #Retorna la suma total de los numeros ingresados.


if __name__ == "__main__":
    
    print(f"La sumatoria de los numeros ingresados es: {sumatoria_numeros()}")