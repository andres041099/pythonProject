# Tarea Funciones o metodos en Python
import math
def sumar(a,b):
    sumatoria= a + b
    print("El resultado es: ", sumatoria)
def restar(a, b):
    restador= a - b
    print("El resultado es: ", restador)
def multiplicar(a,b):
    multiplicacion = a * b
    print("El resultado es: ", multiplicacion)
def dividir(a,b):
    if b != 0:
       division = a - b
       print("El resultado es: ", division)
def pantallaAritmetica():
    print("--------------------------------")
    print("Bienvenido a Calculadora Basica")
    print("1-Calcular Suma: ")
    print("2-Calcular resta: ")
    print("3-Calcular multiplicacion: ")
    print("4-Calcular division: ")
    opcion=int(input("Que quieres Hacer: "))
    primerNumero= int(input("Introduce un Primer Numero: "))
    segundoNumero = int(input("Introduce un Segundo Numero: "))
    numero_flotante1 = primerNumero
    nuumero_flotante2 = segundoNumero
    if opcion == 1:
        sumar(primerNumero,segundoNumero)
    elif opcion== 2:
        restar(primerNumero,segundoNumero)
    elif opcion == 3:
        multiplicar(primerNumero,segundoNumero)
    elif opcion == 4:
        dividir(numero_flotante1,nuumero_flotante2)
    else:
        print(f"Error. {opcion} no existe como opcion. porfavor usa las opciones del 1-7")
        print("--------------------------------")
# Ejercicio 2: Convertidor de Temperaturas
def celcuisAFarenheit(celsius):
    return round(celsius * 1.8 +32)
def farerenheitACelcuis(farenheit):
    return round((farenheit-32)/1.8 )
def celsiusAKelvin(celcius):
    return  round(celcius + 273.15)
def pantallaTemperatura():
    print("---------------------------------------------")
    print("Bienvenido a Convertidor de Grados F, C, K.\n")
    print("1-Convertir de Celcius a Fahrenheit\n")
    print("2-Convertir de Fahrenheit a Celcius \n")
    print("3-Convertir de Celcius a Kelvin \n")
    selecionar = int(input("Selecciona tu opcion: "))
    if selecionar == 1:
        numeroGrado = float(input("Ingrese una temperatura: "))
        print("La temperatura es: ", celcuisAFarenheit(numeroGrado), "F")
    elif selecionar == 2:
        numeroGrado = float(input("Ingrese una temperatura: "))
        print("La temperatura es: ", farerenheitACelcuis(numeroGrado), "c")
    elif selecionar == 3:
            numeroGrado = float(input("Ingrese una temperatura: "))
            print("La temperatura es: ", celsiusAKelvin(numeroGrado), "k")
    else:
        print(f"Error. {selecionar} no existe como opcion. porfavor usa las opciones del 1-3")
        print("-----------------------------------------------------------------------------")
#Ejercicio 3: Calculadora Promedio
def calcular_promedio(a, b, c):
    return  (a+b+c)/3
def pantallaPromedio():
    print("-----------------------")
    print("Bienvenido a Calculadore de Promedio")
    calcularPromedio1= int(input("Introduce un numero: "))
    calcularPromedio2 = int(input("Introduce otro numero: "))
    calcularPromedio3 = int(input("Introduce un ultimo numero: "))
    print("Los numeros Introducidos son: ",calcularPromedio1, calcularPromedio2,calcularPromedio3,end=",")
    print(f"la Formula de los Datos es: ({calcularPromedio1}+{calcularPromedio2}+{calcularPromedio3})/3")
    print("El Promedio es: ", calcular_promedio(calcularPromedio1,calcularPromedio2,calcularPromedio3))
    print("------------------------------------------------------------------------------------------")
#Ejercicio 4: Cálculo del Área de un Círculo
def calcular_area_circulo(radio):
    return math.pi*math.pow(radio,2)
def patallaCálculoCírculo():
    print("---------------------------")
    print("Bienvenido a Cálculo del Área de un Círculo")
    calcularCirculo = int(input("Introduce un numero radio: "))
    resultadoFlotante= float(calcularCirculo)
    print(f"Formula de este programa es: π*{calcularCirculo}^2")
    print("El área del círculo es: ", math.floor(calcular_area_circulo(resultadoFlotante)))
#Ejercicio 5: Contador de Vocales
def contar_vocales(texto):
    contador = 0
    vocales = "aeiou"
    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1
    return contador
def pantallaContadorVocales():
    print("---------------------------")
    print("Bienvenido a ContadorVocales")
    contadorVocales = input("Ingresa una palabra: ")
    print(f"La palabra ingresada es: {contadorVocales} y la cantidad de vocales es {contar_vocales(contadorVocales)}")
    print("---------------------------------------------------------------------------------------------------------")
#Ejercicio 6: Tabla de Multiplicar
def tabla_de_multiplicar(n):
    for numeroMultiplicador in range(1,11):
        resultadoTabla= n*numeroMultiplicador
        print(f'{n}*{numeroMultiplicador}={resultadoTabla}')
def pantallaTablaMultiplicar():
    print("---------------------------")
    print("Bienvenido a Tabla de Multiplicar")
    numeroMultiplicar = int(input("Ingresa una palabra: "))
    print(f'El numero que Escogiste: {numeroMultiplicar}')
    tabla_de_multiplicar(numeroMultiplicar)
    print("-------------------------------------------")
while True:
    print("----------------------------------------------")
    print("Bienvenido a Programa de Práctica 5 Estudiante")
    print("1-Calculadora Básica")
    print("2-Convertidor de Temperaturas")
    print("3-Calculadora de Promedio")
    print("4-Cálculo del Área de un Círculo")
    print("5-Contador de Vocales")
    print("6-Tabla de Multiplicar")
    print("7-Salir")
    selecciona = int(input("¿Qué quieres hacer? "))

    if selecciona == 1:
        pantallaAritmetica()
    elif selecciona == 2:
        pantallaTemperatura()
    elif selecciona == 3:
        pantallaPromedio()
    elif selecciona == 4:
        patallaCálculoCírculo()
    elif selecciona == 5:
        pantallaContadorVocales()
    elif selecciona == 6:
        pantallaTablaMultiplicar()
    elif selecciona == 7:
        print("Gracias por usar mi software. desarrollado y probado por Andres Rodriguez Liberato")
        print("----------------------------------------------------------------------------")
        break
    else:
        print(f"Error. {selecciona} no existe como opción. Por favor, usa las opciones del 1-7")
        print("----------------------------------------------------------------------------")