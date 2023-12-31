"""Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú 
y el programa finalizará."""

#Define la funcion llamada 'comenzar_programa'.
def comenzar_programa():
    print("El programa ha comenzado. Este es el texto asociado a la opcion 1.")

#Define la funcion llamada 'imprimir_listado'.
def imprimir_listado():
    print("Se ha impreso el listado. Este es el texto asociado a la opcion 2.")

if __name__ == "__main__":
    
    continuar = True  #Inicializa la variable 'continuar' como True.

    while continuar:  #Inicia un bucle que se ejecuta mientras 'continuar' sea True.
        print("Menu:")
        print("1- Comenzar programa")
        print("2- Imprimir listado")
        print("3- Finalizar programa")

        opcion = input("Elige una opcion (1, 2 o 3): ")

        if opcion.isdigit():  #Verifica si la opcion es un numero.
            opcion = int(opcion)  #Convierte la opcion a entero.

            if opcion == 1:
                comenzar_programa()
            elif opcion == 2:
                imprimir_listado()
            elif opcion == 3:
                print("Programa finalizado.")
                continuar = False  #Cambia el valor de 'continuar' a False para salir del bucle.
            else:
                print("Opcion incorrecta. Por favor, elige 1, 2 o 3.")
        else:
            print("Por favor, ingresa solo numeros.")