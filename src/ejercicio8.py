"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1 """

#Define la funcion llamada 'imprimir_triangulo_rectangulo' que toma el argumento 'n'.
def imprimir_triangulo_rectangulo(n):
    for i in range(1, n+1, 2):  #Itera desde 1 hasta 'n' (incluido) de 2 en 2.
        for j in range(i, 0, -2):  #Itera desde 'i' hasta 0 de 2 en 2 en cada iteracion.
            print(j, end=" ")  #Imprime el valor de 'j' seguido de un espacio en la misma linea.
        print()  #Imprime un salto de linea para pasar a la siguiente fila.


if __name__ == "__main__":
    
    num = int(input("Ingresa un numero entero: "))
    imprimir_triangulo_rectangulo(num)  #Llama a la funcion 'imprimir_triangulo_rectangulo' con el numero ingresado.