#lista
#listas(list):
# numeros= [1,2,3,4,5,6,7,8,9,10]
# cadenas_caracteres = ["jose","Maria","Pedro"]
# varios_datos=["maria",9,2,5,True,False]
# #Tuplas(tuplas):
# colores=("Rojo","Amarillo","verde","Azul")
#
# numeros.append(23)
# # print(numeros)
#
# numeros.remove(10)
# print("se removio a: ",10)
# print(numeros)
#
# edades={"Ana":22,"Pedro":31,"Carlos":20}
# print(edades["Ana"])
# for e in edades:
#     print(e)
# for m in edades.keys():
#     print(m)
# for n in edades.values():
#     print(n)
# for i in  edades.items():

libros = []


def agregar_libro(agregar):
    if agregar in libros:
        libros.append(agregar)
        print(f"Libro '{agregar}' agregado con éxito.")
    else:
        print("esta vacio. agrega algo")


def vender_libro(vender):
    if vender in libros:
        libros.remove(vender)
        print(f"Libro '{vender}' vendido.")
    else:
        print(f"No se pudo vender porque el libro '{vender}' no está en la lista.")


def mostrar_libros():
    if libros:
        print("Los libros disponibles son:")
        for libro in libros:
            print(f"- {libro}")
    else:
        print("No hay libros en la lista.")


def menuBliblioteca():
    while True:
        print("\nGestor de Venta de Libros")
        print("1- Agregar libro")
        print("2- Vender libro")
        print("3- Mostrar libros")
        print("4- Salir")

        seleccion = input("Selecciona una opción: ")

        if seleccion == "4":
            print("Gracias por utilizar esta app.")
            break  # Sale del bucle

        elif seleccion == "1":
            introduirLibro = input("Introduce el nombre del libro a agregar: ")
            agregar_libro(introduirLibro)

        elif seleccion == "2":
            venderLibro = input("Introduce el nombre del libro a vender: ")
            vender_libro(venderLibro)

        elif seleccion == "3":
            mostrar_libros()

        else:
            print("Opción no válida, por favor selecciona una opción correcta.")


menuBliblioteca()

