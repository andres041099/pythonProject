#Ejercicio 1: Filtrar Números Impares
numerosAFiltar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for impares in numerosAFiltar:
    if impares % 2 == 0:
        print(impares)
#Ejercicio 2: Contar la Frecuencia de un Elemento en una Lista
animales= ['perro', 'gato', 'perro', 'pajaro', 'gato', 'perro']
contadorPerro=0
contadorGato=0
contadorPajaro=0
print(f'La lista de animales son:')
for animal in animales:
    print(animal)
    if animal== "perro":
        contadorPerro+=1
    elif animal== "gato":
        contadorGato += 1
    elif animal== "pajaro":
        contadorPajaro += 1
print(f' perro se repite {contadorPerro}')
print(f'gato se repite {contadorGato}')
print(f'pajaro se repite {contadorPajaro}')
#Ejercicio 3: Buscar el Valor Mínimo y Máximo en una Lista
import random
lista_aleatoria = []
print("-------------------Lista Aleatoria------------------------")
numerosIntroducir1 = int(input("Introduce un numero de inicio : "))
numerosIntroducir2 = int(input("Introduce un numero de final : "))
cantidad_numeros = int(input("Introduce la cantidad de números aleatorios que deseas generar: "))
for n in range(cantidad_numeros):
    numeroAleatorio = random.randint(numerosIntroducir1, numerosIntroducir2)
    lista_aleatoria.append(numeroAleatorio)
print(f'La lista es: {lista_aleatoria}')
numeroMinimo = min(lista_aleatoria)
numeroMaximo = max(lista_aleatoria)
print(f'El número mínimo es: {numeroMinimo}')
print(f'El número máximo es: {numeroMaximo}')
#Ejercicio 4: Determinar Si un Valor Existe en una Tupla
colores=('rojo', 'azul', 'verde', 'amarillo')
print("---------------Existe en la Tupla---")
color_usuario = input("Introduce un color: ").lower()
if color_usuario in colores:
    print(f"{color_usuario} Este color existe")

else:
  print(f"{color_usuario} Este color no existe")
#Ejercicio 5: Contar Elementos en una Tupla
print("-------------Contar Elementos en una Tupla")
introducir= int(input("Introduce un valor nuemerico entero que deseas listar: "))
numeros=(1,2,3,4,5,6,7,8,9,10)
for numero in numeros:
     if numero >=introducir:
         print(numero)
#Ejercicio 6: Crear un Diccionario de Precios
print("Diccionario de Precios")
precios={'manzana': 1.5, 'banana': 0.75, 'pera': 2.0}
for fruta in precios:
    print(f'La fruta es {fruta} y el precio es {precios[fruta]}')
#Ejercicio 7: Eliminar Claves con Valores Específicos en un Diccionario
print("Valores Específicos en un Diccionario")
inventario={'lápiz': 0, 'cuaderno': 5, 'borrador': 2, 'regla': 0}
for inventarios in list(inventario.keys()):
    if inventario[inventarios]==0:
        print(f"Eliminando {inventarios} con valor de {inventario[inventarios]}")
        del inventario[inventarios]
print(f"Inventario actualizado son: {inventario}")