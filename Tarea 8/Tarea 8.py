#Ejercicio 1: Calculadora con Funciones, Bucle while, y Diccionario
def suma(a,b):
    return  a+b
def restar(a,b):
    return  a-b
def multiplicacion(a, b):
    return  a*b
def division(a,b):
    if b == 0:
        return "la division entre cero no es posible"
    else:
        return a/b
operaciones={'1': suma, '2': restar, '3':multiplicacion, '4': division}

def menuCalculadoraFunciones():
    while True:
        print("Calculadora de Funciones")
        print("1-Sumar: ")
        print("2-Restar: ")
        print("3-Multiplicar")
        print("4-dividir")
        print("5-salir")
        seleccion= (input("Selecciona 1: "))
        if seleccion == "5":
            print("Gracias por poder utilizar esta app")
            break
        elif seleccion in operaciones:
            introducir1= int(input("introduce un numero: "))
            introducir2= int(input("introduce otro numero: "))
            resultado = operaciones[seleccion](introducir1, introducir2)
            print("El resultado es", resultado)
        else:
            print(f'{seleccion}esta opcion no existe intentlo otra vez')
#Ejercicio 2:  Gestión de Venta de Libros
libros=[]
def agregar_libro(agregar):
    if agregar not in libros:
         libros.append(agregar)
         print(f"Libro '{agregar}' agregado con éxito.")
    else:
        print("esta vacio. agrega algo")
def vender_libro(vender):
    if vender in libros:
        libros.remove(vender)
        print(f"Libro '{vender}' se vendio exitosamente con éxito.")
    else:
        print(f'no se pudo vender porque no existe nada en {vender}')
def mostrar_libros():
    if libros:
        print(" Los libros actuales son:")
        for libro in libros:
            print(libro)
    else:
        print("No hay libros disponibles")
def menuBliblioteca():
    while True:
        print("Gestor de Venta de Libros")
        print("1-Agregar: ")
        print("2-Vender: ")
        print("3-Mostrar Libros: ")
        print("4-salir")
        seleccion = input("Selecciona: ")
        if seleccion =="4":
            break
            print("Gracias por poder utilizar esta app")
        elif seleccion == "1":
            introduirLibro= input("Agrega un Libro: ")
            agregar_libro(introduirLibro)
        elif seleccion == "2":
            comprarLibro = input("Compra un Libro: ")
            vender_libro(comprarLibro)
        elif seleccion == "3":
             mostrar_libros()
        else:
            print(f'{seleccion} no existe esta opcion. vuelve intentarlo otra vez')

#Menu Principal del control la programa
while True:
     print("Tarea Estudiante 8")
     print("1-Calculadora de Funciones:")
     print("2-Gestor de Venta de Libros:")
     print("3-salir")
     elegir = int(input("Selecciona 1 de ellas: "))
     if elegir == 3:
         break
         print("Gracias por usar mi software. desarrollado y probado por Andres Rodriguez Liberato")
     elif elegir==1:
         menuCalculadoraFunciones()
     elif elegir==2:
         menuBliblioteca()
     else:
         print(f'{elegir} no existe esta opcion. vuelve intentarlo otra vez')
