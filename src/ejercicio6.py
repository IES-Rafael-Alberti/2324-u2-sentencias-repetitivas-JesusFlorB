"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.
*
**
***
****
***** """

def imprimir_triangulo_rectangulo(altura):
    for i in range(1, altura+1):
        print('*' * i)

def main():
    altura = int(input("Ingresa la altura del triangulo (un numero entero): "))
    imprimir_triangulo_rectangulo(altura)

if __name__ == "__main__":
    
    main()