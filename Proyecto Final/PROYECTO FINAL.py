#Practica Final Hecha por Andres Rodriguez Liberato y Zoar Reyes Tolentino
tareas ={}#Diccionario vacio para luego a{adirle elementos
def agregarTarea(): #Metodo para añadir nuevos usuarios
    print("-------Bienvenido a Agregar Tarea-------")
    try:#Para capturar el error Alfabetico
        cantidadElementos = int(input("¿Cuántos usuarios y tareas deseas agregar?: "))
        for cantidadesAgregar in range(cantidadElementos):#Bucle para añadir la cantidad de usuarios y tareas dentro del diccionario tareas
            anadido = input(f"Añadir usuario {cantidadesAgregar + 1}: ")
            # Condición para añadir nuevas tareas y claves
            if anadido not in tareas:
                claveAnadida = input("Agregar tarea: ")
                tareas[anadido] = claveAnadida
                print(f'El usuario "{anadido}" y su tarea "{claveAnadida}" fueron agregados con éxito a la lista. Pude verlo en Mostrar Lista de Tareas')
            else:#Este mensaje se muestra si el usuario ya existe
                print(f'El usuario "{anadido}" ya existe. Por favor, crea un nuevo usuario.')
    except ValueError:#Para delvolver una solucion al error Alfabetico
        print("Error Alfabetico: Ha introducido una letra o símbolo en lugar de un número. Introduce un numero para establecer la candidad de usuarios y tareas.")
def modificarTarea(): #Metodo para modificar tarea.
    print("-------Bienvenido a Modificar Tarea-------")
    usuario = input("Ingrese usuario: ")
    if usuario in tareas:# Condicion para modificar las tareas.
        print("Tarea Existente. Puedes modificarlo")
        tareaModificada = input("Modificar Tarea: ")
        tareas[usuario] = tareaModificada
        print(f'La tarea anterior fue modificada por "{tareaModificada}" exitosamente en la lista. pude verlo en Mostrar Lista de Tareas')
    else:
        print(f'{usuario} no existente en Lista de Tareas. porfavor introduce uno que exista')
def tareaRealizada(): #Metodo para Realizar una Tarea.
    print("-------Bienvenido a Marcar Tarea como realizada-------")
    usuarioTarea = input("Ingrese usuario: ")
    if usuarioTarea in tareas:#Condicion para realizar una tarea.
        print(f'La tarea del usuario  {usuarioTarea} fue realizada exitozamente')
        del tareas[usuarioTarea]
    else:
        print(f'El usuario {usuarioTarea} no existente en Lista de Tareas. porfavor introduce uno que exista')

def mostrarListaTarea(): #Metodo para Mostrar Lista De Tarea.
    print("-------Bienvenido a Mostrar Lista de Tareas--------")
    if tareas:#Condicion para Mostrar Lista de Tarea.
        print("Tareas Actuales son: ")
        for tarea in tareas:
            print(f'Usuario: {tarea} y tiene como Tarea: {tareas[tarea]}')
    else:
        print("No hay usuarios ni tareas disponibles")
while True: #Menu Principal para desplegar todas las funciones.
    print("----------Gestión de Tareas---------")
    print("1. Agregar Tarea")
    print("2. Modificar Tarea")
    print("3. Marcar Tarea como realizada")
    print("4. Mostrar Lista de Tareas")
    print("5. Salir")
    try:#Funciona como forma de capturar un error en el programa
        seleccion = int(input("Que desea ejecutar: "))
        if seleccion == 5:
            print("Gracias por usar nuestro software. Fue Desarrollado por Andres Rodriguez L. y Zoar Reyes T.")
            break
        elif seleccion == 1:
            agregar = agregarTarea()
        elif seleccion == 2:
            modificar = modificarTarea()
        elif seleccion == 3:
            realizada = tareaRealizada()
        elif seleccion == 4:
            mostrar = mostrarListaTarea()
        else:
            print(f'{seleccion} es una opcion no existente en la opnciones de seleccion. Introdusca una de las opciones dentro del rango del 1 al 5 existentes')
    except ValueError:#Funciona como forma de devolver un mensaje para evitar escribir letras o simbolos en el programa
        print("Error Alfabetico: Ha introducido una letra o símbolo en lugar de un número. Introdusca una de las opciones dentro del rango del 1 al 5 existentes.")