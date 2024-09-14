#Practica Final Hecha por Andres Rodriguez Liberato y Zoar Reyes Tolentino
tareas ={}
def añadir(): #Metodo para añadir nuevos usuarios
    #Condicion para añadir nuevas tareas y claves.
    anadido = input("Añadir usuario: ")
    if anadido not in tareas:
        claveAnadida = input("Agregar tarea: ")
        tareas[anadido]=claveAnadida
        print("Fueron agregados con éxito.")
    else:
        print("Esta tarea Existe. Escribe otra")
def modTarea(): #Metodo para modificar tarea.
    #Condicion para modificar las tareas.
    usuario = input("Ingrese usuario: ")
    if usuario in tareas:
        print("Tarea Existente. puedes modificarlo")
        tareaModificada = input("Modificar Tarea: ")
        tareas[usuario] = tareaModificada
        print(f'La tarea anterior fue modificada por "{tareaModificada}" exitosamente')
    else:
        print("Usuario no existente. Usar otro")
def tareaRealizada(): #Metodo para Realizar una Tarea.
    #Condicion para realizar una tarea.
    usuarioTarea = input("Ingrese usuario: ")
    if usuarioTarea in tareas:
        print("La tarea fue realizada")
        del tareas[usuarioTarea]
    else:
        print("La tarea no existe.")

def mostrarListaTarea(): #Metodo para Mostrar Lista De Tarea.
    #Condicion para Mostrar Lista de Tarea.
    if tareas:
        print("Tareas Actuales son: ")
        for tarea in tareas:
            print(f'Usuario: {tarea} y Tarea: {tareas[tarea]}')
    else:
        print("No hay tareas disponibles")
        #Menu Principal para desplegar todas las funciones.
while True:
    print("----------Gestión de Tareas---------")
    print("1. Agregar Tarea")
    print("2. Modificar Tarea")
    print("3. Marcar Tarea como realizada")
    print("4. Mostrar Lista de Tareas")
    print("5. Salir")
    seleccion= int(input("Que desea ejecutar: "))
    if seleccion ==5:
        print("Gracias por usar nuestro software. Desarrollado por Andres Rodriguez L. y Zoar Reyes T.")
        break
    elif seleccion == 1:
        agregar = añadir()
    elif seleccion ==2:
        modificar= modTarea()
    elif seleccion == 3:
        realizada = tareaRealizada()
    elif seleccion==4:
        mostrar=mostrarListaTarea()
    else:
        print(f'{seleccion} No existe. Intenta otra')