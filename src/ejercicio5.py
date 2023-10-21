"""Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión."""

#Define la funcion llamada 'calcular_interes_compuesto' que toma tres argumentos: P, r y t.
def calcular_interes_compuesto(P, r, t):
    resultado = []  #Inicializa una lista vacia llamada 'resultado'.
    i = 1  #Inicializa una variable 'i' con el valor 1.
    while i <= t:  #Inicia un bucle while que se ejecuta mientras 'i' sea menor o igual a 't'.
        P *= 1 + r / 100  #Calcula el capital acumulado usando la formula de interes compuesto.
        resultado.append(f"Año {i}: {P:.2f}")  #Agrega el resultado a la lista 'resultado'.
        i += 1  #Incrementa 'i' en 1 en cada iteracion.
    return resultado


if __name__ == "__main__":

    P = float(input("Ingresa la cantidad a invertir: "))
    r = float(input("Ingresa la tasa de interes anual (porcentaje): "))
    t = int(input("Ingresa el numero de años: "))

    #Llama a la funcion 'calcular_interes_compuesto' con los valores ingresados y almacena los resultados.
    resultados = calcular_interes_compuesto(P, r, t)

    #Itera a traves de los resultados y los imprime uno por uno.
    for resultado in resultados:
        print(resultado)
