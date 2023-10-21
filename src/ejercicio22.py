"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, 
informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

#Define la funcion llamada 'contar_digitos_pares_impares' que toma un 'numero' como argumento.
def contar_digitos_pares_impares(numero):
    pares = 0  #Inicializa una variable 'pares' para contar los digitos pares.
    impares = 0  #Inicializa una variable 'impares' para contar los digitos impares.

    for digito in str(numero):  #Itera a traves de los digitos del numero, convertidos a cadenas.
        if int(digito) % 2 == 0:  #Verifica si el digito convertido a entero es par.
            pares += 1  #Si es par, incrementa el contador de digitos pares.
        else:
            impares += 1  # Si no es par, incrementa el contador de digitos impares.

    return pares, impares


if __name__ == "__main__":
    
    pares_totales = 0  #Inicializa una variable para el total de digitos pares leidos.
    impares_totales = 0  #Inicializa una variable para el total de digitos impares leídos.
    terminado = False  #Inicializa una variable 'terminado' como False para controlar el bucle.

    while not terminado:  #Inicia un bucle que se ejecuta mientras 'terminado' sea False.
        entrada = input("Ingresa un numero entero positivo (o 0 para terminar): ")

        if entrada.isdigit():  #Verifica si la entrada es un numero.
            numero = int(entrada)  #Convierte la entrada en un entero.

            if numero == 0:
                terminado = True  #Cambia el valor de 'terminado' a True para salir del bucle.
            elif numero < 0:
                print("El numero debe ser positivo.")
            else:
                pares, impares = contar_digitos_pares_impares(numero)  #Llama a la funcion para contar digitos pares e impares.

                print(f"El numero {numero} tiene {pares} digitos pares y {impares} digitos impares.")

                pares_totales += pares  #Actualiza el total de digitos pares leidos.
                impares_totales += impares  #Actualiza el total de digitos impares leidos.
        else:
            print("Por favor, ingresa solo numeros.")

    print(f"En total, se leyeron {pares_totales} digitos pares y {impares_totales} digitos impares.")