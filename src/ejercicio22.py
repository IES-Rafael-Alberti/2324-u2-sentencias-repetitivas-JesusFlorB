"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, 
informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

def contar_digitos_pares_impares(numero):
    pares = 0
    impares = 0

    for digito in str(numero):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

if __name__ == "__main__":
    
    pares_totales = 0
    impares_totales = 0
    terminado = False
    
    while not terminado:
        entrada = input("Ingresa un numero entero positivo (o 0 para terminar): ")

        if entrada.isdigit():
            numero = int(entrada)

            if numero == 0:
                terminado = True
            elif numero < 0:
                print("El numero debe ser positivo.")
            else:
                pares, impares = contar_digitos_pares_impares(numero)

                print(f"El numero {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")
                
                pares_totales += pares
                impares_totales += impares
        else:
            print("Por favor, ingresa solo numeros.")

    print(f"En total, se leyeron {pares_totales} digitos pares y {impares_totales} digitos impares.")