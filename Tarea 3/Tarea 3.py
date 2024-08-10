#Ejercicio 1: Par o Impar
print("Ejercicio Par o Impar")
numeroAIntroduir = int(input("Introduce un numero entero: "))
if numeroAIntroduir % 2 == 0:
    print("el numero es para")
else:
    print("es impar")
# Ejercicio 2: Comparar Tres Números
print("Ejercicio Comparar Tres Números")
numeroIntroducir = input("Introduce un numero: ")
numeroIntroducir2 = input("Introduce otro numero: ")
numeroIntroducir3 = input("Introduce otro numero: ")
if numeroIntroducir>numeroIntroducir2:
    print("el Primer numero introducido es mayor")
elif numeroIntroducir2>numeroIntroducir3:
    print("El segundo numero es Mayor")
else:
    print("El tercer numero es mayor")

# Ejercicio 3: Verificar Positividad
print("Ejercicio Verificar Positividad")
numeroVerificar = int(input("Introduce un numero: "))
if numeroVerificar < 0:
    print("El numero que introdujiste es negativo")
elif numeroVerificar >0:
    print("El numero que introdujiste es positivo")
else:
    print("El numero que introdujiste es 0")

# Ejercicio 4: Clasificación de Edad
print("Ejercicio Clasificaciónes de Edad")
edad = int(input("Introduce tu Edad: "))

if edad <= 12 :
    print(edad," tu edad es de un niño")
elif edad >=13 and edad == 17 :
    print(edad," tu edad es de un adolescente")
elif edad >= 18 and edad == 64:
    print(edad, " tu edad es de un adulto")
else:
    print(edad," tu edad es de un adulto mayor")

# Ejercicio 5: Calificación Escolar
print("Ejercicio Calificación Escolar")
calificacion = int(input("Introduce una sola calificacion Final y Unica: "))

if calificacion<= 49:
    print(f'su calificacion es {calificacion} lo cual es insuficiente')
elif calificacion >=50 and calificacion == 69:
    print(f'su calificacion es {calificacion} lo cual es regular')
elif calificacion >=70 and calificacion == 89:
    print(f'su calificacion es {calificacion} lo cual es Buena')
elif calificacion >=90 and calificacion == 100:
    print(f'su calificacion es {calificacion} lo cual es Excelente')

else:
    print("Calificacion no valida en en este programa")




