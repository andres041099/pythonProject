#Ejercicio de funciones Funciones parte 2
#Calculadora de Potencias y Raíces
import math
#Ejercicio 1: Calculadora de Potencias y Raíces
def potencia(bases,exponente):
    return  round(math.pow(bases,exponente))
def raiceCuadrada(nuemeroRaiz):
    return round(math.sqrt(nuemeroRaiz))
def ejercicio1():
    print("--------------------------------------------------------")
    print("Bienvenido a la Calculadora de Exponente y Raiz Cuadrada")
    print("1-Potencia")
    print("2-raiz cuadrada")
    opcion= int(input("Que deseas hacer: "))
    if opcion == 1:
        introducir= int(input("Introduce un numero: "))
        introducir2 = int(input("Introduce un numero: "))
        print(f'El resultado de la potencia que deceas hacer de {introducir} a la {introducir2}='
              f'{potencia(introducir,introducir2)}')
    elif opcion == 2:
        introducir = int(input("Introduce un numero"))
        print(
            f'El resultado de la Raiz Cuadrada que deceas hacer de {introducir} es igual a = {raiceCuadrada(introducir)}')
    else:
        print(f'no existe{opcion} usa otro')
#Ejercicio 2: Conversor de Unidades de Longitud
def metroAKilometros(metros):
    KilometrosEquivalentes= 1000
    unKilometro= 1
    return (metros*unKilometro) /KilometrosEquivalentes
def kilometrosAMillas(kilometros):
    millaEquivalente=1.60934
    return  round(kilometros/millaEquivalente)
def millasAMetros(millas):
    metrosEquivalente = 1609.34
    return round(millas*metrosEquivalente)
def ejercicio2():
    print("--------------------------------------------------------")
    print("Bienvenido a Calculadora la Longitud")
    print("1- De Metro a Kilometros")
    print("2- De Kilometros a milla")
    print("3-Millas a Metros")
    opcion = int(input("Que deseas hacer: "))
    if opcion == 1:
        introducir = int(input("Introduce un numero: "))
        print(f'El resultado de {introducir}= {metroAKilometros(introducir)} km')
    elif opcion == 2:
        introducir = int(input("Introduce un numero: "))
        print(f'El resultado de {introducir}= {kilometrosAMillas(introducir)} MI')
    elif opcion == 3:
        introducir = int(input("Introduce un numero: "))
        print(f'El resultado de {introducir}= {millasAMetros(introducir)} Mtr')
    else:
        print(f'no existe{opcion} usa otro')
#Ejercicio 3: Cálculo del Perímetro de un Rectángulo
def calcular_perimetro_rectangulo(largo, ancho):
    lados = 2
    return lados*(largo+ancho)
def ejercicio3():
    print("--------------------------------------------------------")
    print("Bienvenido a Calculadora el Perímetro de un Rectángulo")
    largo = int(input("Introduce un Largo: "))
    ancho = int(input("Introduce un Ancho: "))
    print(f'El resultado de {largo}= {calcular_perimetro_rectangulo(largo,ancho)}')
#Ejercicio 4: Contador de Consonantes
def contar_consonantes(texto):
    contador = 0
    consonantes = "cdfghjklmnñpqrstvxyz"
    for caracter in texto.lower():
        if caracter in consonantes:
            contador += 1
    return contador
def ejercicio4():
    print("---------------------------")
    print("Bienvenido a Contador Consonantes")
    contadorConsonantes = input("Ingresa una palabra: ")
    print(f"La palabra ingresada es: { contadorConsonantes} y la cantidad de consonantes es: {contar_consonantes(contadorConsonantes)}")
#Ejercicio 5: Generador de Serie Fibonacci
def serieFibonacci(n):
    a = 0
    b = 1
    contador = 0
    while contador <= n:
        print(a, end=", ",)
        r = a + b
        a = b
        b = r
        contador += 1

# for d in range(n):
#     print(serieFibonacci(n))
def ejercicio5():
    print("---------------------------")
    print("Bienvenido a La Serie Fibonacci")
    introducirNumeroSerie = int(input("Ingresa un numero de la Serie  Fibonacci: "))
    serieFibonacci(introducirNumeroSerie)
    # for d in range(introducirNumeroSerie):
        # print("Numero de la seria que pusite fue: ", introducirNumeroSerie)
        # print("La serie es", serieFibonacci(introducirNumeroSerie),end=",")
#Menu Principal para acceder a las demas Funciones
while True:
    print(" Bienvenidos a Control Menu de la Tarea")
    print("1-Calculadora de Potencias y Raíces")
    print("2-Conversor de Unidades de Longitud")
    print("3-Cálculo del Perímetro de un Rectángulo")
    print("4-Contador de Consonantes")
    print("5-Generador de Serie Fibonacci")
    print("6-Salir")
    selecciona = int(input("¿Qué deseas realizar?: "))
    if selecciona == 1:
        ejercicio1()
    elif selecciona == 2:
        ejercicio2()
    elif selecciona == 3:
        ejercicio3()
    elif selecciona == 4:
         ejercicio4()
    elif selecciona == 5:
        ejercicio5()
    elif selecciona == 6:
        print("Gracias por usar mi software. desarrollado y probado por Andres Rodriguez Liberato")
        print("----------------------------------------------------------------------------")
        break
    else:
        print(f"Error. {selecciona} no existe como opción. Por favor, usa las opciones del 1-6")
        print("----------------------------------------------------------------------------")
