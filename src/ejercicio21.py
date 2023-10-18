"""Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, 
si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento."""

def calcular_total_compra(compras):
    total = sum(compras)
    if total > 1000:
        total *= 0.9  
    return total

if __name__ == "__main__":
    
    compras = []
    terminado = False
    
    while not terminado:
        entrada = input("Ingresa el coste de la compra (o 0 para terminar): ")

        if entrada.isdigit():
            monto = float(entrada)

            if monto == 0:
                terminado = True
            elif monto < 0:
                print("El coste debe ser positivo.")
            else:
                compras.append(monto)
        else:
            print("Por favor, ingresa solo numeros.")

    total = calcular_total_compra(compras)

    print(f"El total a pagar es: ${total}")