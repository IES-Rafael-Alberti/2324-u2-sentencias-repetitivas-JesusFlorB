"""Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string 
de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas."""

#Define la funcion llamada 'contar_digitos', que toma un 'titulo' como argumento.
def contar_digitos(titulo):
    return sum(1 for caracter in titulo if caracter.isdigit())  #Cuenta el numero de digitos en el 'titulo'.

#Define la funcion llamada 'main', que no toma argumentos.
def main():
    lineas_completas = 0  #Inicializa una variable 'lineas_completas' para contar el numero de lineas completas.
    terminado = False  #Inicializa una variable 'terminado' como False para controlar el bucle.
    titulos = ""  #Inicializa una cadena de texto vacia llamada 'titulos' para almacenar los titulos.

    while not terminado:  #Inicia un bucle que se ejecuta mientras 'terminado' sea False.
        titulo = input("Libro: ")  #Pide al usuario que ingrese un titulo y almacena la entrada en 'titulo'.

        if titulo == "*":
            terminado = True  #Si el titulo es "*", cambia el valor de 'terminado' a True para salir del bucle.
        else:
            if titulo == "/":
                if lineas_completas > 0:  #Verifica si hay lineas completas.
                    print(f"Linea completa. Aparecen {contar_digitos(titulos)} digitos numericos.")
                else:
                    print("No hay titulos en esta linea.")

                lineas_completas += 1  #Incrementa el contador de lineas completas.
                titulos = ""  #Reinicia la variable 'titulos' para la siguiente linea.
            else:
                titulos += titulo  # Si el titulo no es "*" ni "/", añade el título a la cadena 'titulos'.

    print(f"Fin. Se leyeron {lineas_completas} lineas completas.")


if __name__ == "__main__":
    
    main()  #Llama a la funcion 'main' para iniciar el proceso.