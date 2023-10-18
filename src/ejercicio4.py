"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

def obtener_numero_entero_positivo():
    while True:
        try:
            num = int(input("Por favor, ingresa un numero entero positivo: "))
            if num >= 0:
                return num
            else:
                print("El numero debe ser positivo o cero.")
        except ValueError:
            print("Por favor, ingresa un numero entero valido.")

def cuenta_atras_desde_n(n):
    cuenta_atras = [str(i) for i in range(n, -1, -1)]
    resultado = ", ".join(cuenta_atras)
    return f"Cuenta atras desde {n} hasta 0: {resultado}"

if __name__ == "__main__":
    
    num = obtener_numero_entero_positivo()
    print(cuenta_atras_desde_n(num))