#Ejercicio 1: Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
print("------Programa para introducir palabras-------")
tuPalabra= input("introduce una palabra: ")
for i in range(1,11):
    print("Tu palabra es",tuPalabra)
print("---------------------------------------------")

#Ejercicio 2: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
print("------Programa para introducir Tu Edad------")
tuEdad= int(input("introduce tu edad: "))
contador = 1
while contador <tuEdad:
    contador+=1
    print("tu Cumpliste: ",contador)
print("---------------------------------------------")
#Ejercicio 3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas..
print("------Programa para introducir un numero positivo------")
tuNumeroPositivo= int(input("introduce numero positivo: "))
for i in range(1,tuNumeroPositivo,2):
    print(i,end=",")
#Ejercicio 4: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas..
print("------Programa para introducir un numero positivo pares------")
tuNumeroPositivoPar= int(input("introduce numero positivo: "))
contadorPar= 1
while contadorPar<tuNumeroPositivoPar:
    contadorPar+=1
    if contadorPar%2==0:
        print(contadorPar, end=",")

#Ejercicio 5: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
print("------Programa para introducir un numero positivo para presentar hacia atras------")
numeroEnteroPositivo= int(input("introduce numero entero positivo:"))
cuenta_atras = ""
while numeroEnteroPositivo >=0:
    cuenta_atras += str(numeroEnteroPositivo)
    if numeroEnteroPositivo > 0:
        cuenta_atras += ", "
    numeroEnteroPositivo -= 1
print(cuenta_atras)
#Ejercicio 6: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
print("------Programa tabla de multiplicar------")
numeroMultiplicable= int(input("introduce numero de la Tabla:"))
for i in range(1, 11):
    print(f"{numeroMultiplicable} x {i} = {numeroMultiplicable * i}")
#Ejercicio 7: Escribir un programa que almacene la cadena de caractere contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
print("------Programa Verificacion de Contraseñas------")
contraseña_correcta = "contraseña123"
contraseña_introducida = input("Introduce la contraseña: ")
while contraseña_introducida != contraseña_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contraseña_introducida = input("Introduce la contraseña: ")
print("¡Contraseña correcta!")
#Ejercicio Alterno: Escribir un programa que utilice la librería random de Python crear un numero random del 1 al 100 y pedirle al usuario que adivine el numero e indicarle cuando esta demasiado lejos o demasiado cerca del numero hasta que lo encuentre.
import random

print("------Adivina el numero------")
numero_aleatorio = random.randint(1, 100)
adivinanza = int(input("Adivina el número (entre 1 y 100): "))
while adivinanza != numero_aleatorio:
    diferencia = abs(numero_aleatorio - adivinanza)
    if diferencia > 20:
        print("Estás muy lejos.")
    elif diferencia > 10:
        print("Estás lejos.")
    elif diferencia > 5:
        print("Estás cerca.")
    else:
        print("¡Estás muy cerca!")
    adivinanza = int(input("Inténtalo de nuevo: "))
print("¡Felicidades! Has adivinado el número.")