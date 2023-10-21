"""Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, 
si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento."""

#Define la funcion llamada 'calcular_total_compra' que toma una lista de 'compras' como argumento.
def calcular_total_compra(compras):
    total = sum(compras)  #Calcula el total de las compras sumando todos los elementos de la lista 'compras'.
    if total > 1000:
        total *= 0.9  #Si el total es mayor que 1000, aplica un descuento del 10% (multiplicando por 0.9).
    return total


if __name__ == "__main__":
    
    compras = []  # Inicializa una lista vacaa llamada 'compras' para almacenar los costos.
    terminado = False  #Inicializa una variable 'terminado' como False para controlar el bucle.

    while not terminado:  #Inicia un bucle que se ejecuta mientras 'terminado' sea False.
        entrada = input("Ingresa el coste de la compra (o 0 para terminar): ")

        if entrada.isdigit():  #Verifica si la entrada es un número.
            monto = float(entrada)  #Convierte la entrada en un float.

            if monto == 0:
                terminado = True  #Cambia el valor de 'terminado' a True para salir del bucle.
            elif monto < 0:
                print("El coste debe ser positivo.")
            else:
                compras.append(monto)  #Agrega el monto a la lista 'compras'.
        else:
            print("Por favor, ingresa solo numeros.")

    total = calcular_total_compra(compras)  #Llama a la funcion 'calcular_total_compra' con la lista de compras y guarda el resultado en 'total'.

    print(f"El total a pagar es: ${total}")