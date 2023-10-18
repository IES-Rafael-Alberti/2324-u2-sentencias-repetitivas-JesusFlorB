"""Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión."""

def calcular_interes_compuesto(P, r, t):
    resultado = []
    for i in range(1, t+1):
        P *= 1 + r / 100
        resultado.append(f"Año {i}: {P:.2f}")
    return resultado

if __name__ == "__main__":
    
    P = float(input("Ingresa la cantidad a invertir: "))
    r = float(input("Ingresa la tasa de interes anual (porcentaje): "))
    t = int(input("Ingresa el numero de años: "))

    resultados = calcular_interes_compuesto(P, r, t)
    for resultado in resultados:
        print(resultado)