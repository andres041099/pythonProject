#     sumar = a + b
#     print("E resultado es: ", sumar)
# def Restar():
#     a = int(input("Introduce un Numero"))
#     b = int(input("Introduce un otro"))
#     restar= a - b
#     print("E resultado es: ", restar)
# def Multiplicar():
#     a = int(input("Introduce un Numero"))
#     b = int(input("Introduce un otro"))
#     multiplicacion = a * b
#     print("E resultado es: ", multiplicacion)
# def Dividir():
#     a = int(input("Introduce un Numero"))
#     b = int(input("Introduce un otro"))
#     division = a - b
#     print("E resultado es: ", division)
# print("Calculadora Basica")
# print("1-Calcular Suma: ")
# print("2-Calcular resta: ")
# print("3-Calcular multiplicacion: ")
# print("4-Calcular division: ")
# opcion=int(input("Que quieres Hacer: "))
# if opcion == 1:
#     Suma()
# elif opcion== 2:
#     Restar()
# elif opcion == 3:
#     Multiplicar()
# elif opcion == 4:
#     Dividir()
# else:
#     print("este numero no existe")

# Ejercicio 2: Convertidor de Temperaturas
def celcuisAFarenheit(celsius):
    return celsius * 1.8 +32
def farerenheitACelcuis(farenheit):
    return (farenheit-32)/1.8
def celsiusAKelvin(celcius):
    return celcius + 273.15

while True:
    print("Convertidor de Grados F, C, K.\n")
    print("1-Convertir de Celcius a Fahrenheit\n")
    print("2-Convertir de Fahrenheit a Celcius \n")
    print("3-Convertir de Celcius a Kelvin \n")
    print("4-Salir")
    seleciona = int(input("Selecciona tu opcion: "))
    if seleciona == 1:
        numeroGrado = float(input("Ingrese una temperatura: "))
        print("La temperatura es: ",celcuisAFarenheit(numeroGrado),"F")
    elif seleciona == 2:
         print("La temperatura es: ",farerenheitACelcuis(numeroGrado), "c")
    elif seleciona == 3:
         print("La temperatura es: ", celsiusAKelvin(numeroGrado), "k")
    elif seleciona == 4:
         print("Gracias por usar este Programa")
         break
    else:
        print(f"Error. Este nuemro {seleciona} no existe. porfavor usa las opciones del 1-4")
