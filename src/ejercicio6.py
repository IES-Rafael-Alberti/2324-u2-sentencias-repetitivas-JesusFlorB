"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.
*
**
***
****
***** """

#Define la funcion llamada 'imprimir_triangulo_rectangulo' que toma el argumento 'altura'.
def imprimir_triangulo_rectangulo(altura):
    for i in range(1, altura+1):  #Itera desde 1 hasta 'altura'.
        print('*' * i)  #Imprime '*' repetido 'i' veces.

#Define la funcion llamada 'main'.
def main():
    altura = int(input("Ingresa la altura del triangulo (un numero entero): "))
    imprimir_triangulo_rectangulo(altura)  #Llama a la funcion 'imprimir_triangulo_rectangulo' con la altura ingresada.


if __name__ == "__main__":
    
    main()  #Llama a la funcion 'main'.