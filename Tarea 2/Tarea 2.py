#Ejerccios 1: Sumar
print("-----------------------------------------")
print("-------------Suma de 2 Numeros-----------")
primerNumero = int(input("Introduce un Numero: "))
segundoNumero = int(input("Introduce un Otro: "))
resutadoSuma= primerNumero+segundoNumero
print(f'Tu resultado es {resutadoSuma}')

#Ejerccios 2: Suma de 3 numeros
print("-----------------------------------------")
print("-------------Suma de 3 Numeros-----------")
numeroPrimero = int(input("Introduce un Numero: "))
numerosegundo = int(input("Introduce un Otro: "))
numeroTercero = int(input("Introduce Otro: "))
sumatoria= numeroPrimero+numerosegundo+numeroTercero
print(f'Tu resultado es {sumatoria}')

#Ejerccios 3: Resta de 2 numeros
print("-----------------------------------------")
print("-------------Resta de 2 Numeros-----------")
restaPrimera = int(input("Introduce un Numero: "))
restaSegunda = int(input("Introduce un Otro: "))
resta= restaPrimera-restaSegunda
print(f'Tu resultado es {resta}')

#Ejerccios 4: Multiplicacion de 3 Numeros
print("-----------------------------------------")
print("-------------Multiplicar de 3 numeros-----------")
multiplicaPrimera = int(input("Introduce un numero: "))
multiplicaSegunda = int(input("Introduce un otro: "))
multiplicaTercero = int(input("Introduce otro: "))
multiplica= multiplicaPrimera*multiplicaSegunda*multiplicaTercero
print(f'tu resultado es {multiplica}')

#Ejerccios 5: Multiplicacion de 2 Numeros Float
print("-----------------------------------------")
print("-------------Multiplicacion de 2 Numeros Float-----------")
primerFloat = float(input("Introduce un numero: "))
segundoFloat = float(input("Introduce un otro: "))
tercerFloat = float(input("Introduce otro: "))
multiplicacionFloat= primerFloat*segundoFloat*tercerFloat
print(f'tu resultado es {multiplicacionFloat}')

#Ejerccios 6: Division de 2 Numeros
print("-----------------------------------------")
print("-------------Division de 2 Numeros-----------")
x=200
y=500
resultado= x/y
print(f'tu resultado es {resultado}')

#Ejerccios 7: Potencia
print("-----------------------------------------")
print("-------------Potencia--------------------")
basePotencial=20
esponente=5
resultante = basePotencial**esponente
print(f'tu resultado es {resultante}')

#Ejerccios 8: Residuo
print("-----------------------------------------")
print("-------------Residuo---------------------")
primerValor= 350
segundoValor=2
residuo = primerValor%segundoValor
print(f'tu resultado es {residuo}')

#Ejerccios 9: Comparacion Mayor o Menor que
print("---------------------------------------------------------------")
print("-------------Comparacion Mayor o menor que---------------------")
mayor= 100
menor=50
comparacion= mayor>menor
print(f'Mayor {mayor} >Menor{menor}:{comparacion}')

#Ejerccios 10: Comparacion de Igualdad
print("---------------------------------------------------------------")
print("-------------Comparacion de Igualdad---------------------")
primerComparado = int(input("Introduce un numero: "))
segundoComparado = int(input("Introduce un otro: "))
comparacionIgual = primerComparado==segundoComparado
print(f' {primerComparado}=={segundoComparado} es {comparacionIgual}')

#Ejerccios 11:Comparacion de Igualdad opuesto
print("---------------------------------------------------------------")
print("-----------Comparacion de Igualdad opuesto---------------------")
primerComparadoDesigual = int(input("Introduce un numero: "))
segundoComparadoDesigual = int(input("Introduce un otro: "))
comparacionIgualDesigual = primerComparadoDesigual!=segundoComparadoDesigual
print(f' {primerComparadoDesigual}=={segundoComparadoDesigual} es {comparacionIgualDesigual}')

#Ejerccios 12: And y Or Comparacion
print("---------------------------------------------------------------")
print("------------And y Or Comparacion-------------------------------")
valor1= True
valor2 = False
comparacionAnd= valor1 and valor2
comparacionOr= valor1 or valor2
print("La comparacion de ",valor1,"and",valor2," es ",comparacionAnd)
print("La comparacion de ",valor1,"or",valor2," es ",comparacionOr)

#Ejerccios 13: Aritmetica Simple
print("---------------------------------------------------------------")
print("------------Aritmetica Simple----------------------------------")
numero1= int(input("Introduce un numero :"))
numero2= int(input("Introduce otro numero "))
numero3= int(input("Introduce otro numero :"))
numero4= int(input("Introduce otro numero :"))
aritmetica= numero1 + numero2 * numero3 + numero3 / numero4
print("El resultado de ", numero1,"+", numero2,"*",numero3,"+",numero3,"/",numero4,"=",aritmetica)

#Ejerccios 14: Aritmetica Simple 2
print("---------------------------------------------------------------")
print("------------Aritmetica Simple 2-------------------------------")
numero1n= int(input("Introduce un numero: "))
numero2n= int(input("Introduce otro numero: "))
numero3n= int(input("Introduce otro numero: "))
aritmetica2= numero1n - numero2n / numero3n * (numero3n + numero1n)
print("El resultado de ", numero1n,"-", numero2n,"/",numero3n,"*","(",numero3n,"+",numero1n,")","=",aritmetica2)

#Ejerccios 15: Aritmetica Simple 3
print("---------------------------------------------------------------")
print("------------Aritmetica Simple 3-------------------------------")
numero1l= int(input("Introduce un numero: "))
numero2l= int(input("Introduce otro numero: "))
numero3l= int(input("Introduce otro numero: "))
comparaciones= (numero1l>numero2l) and (numero3l>numero1l)
print("El resultado de ","(",numero1l,">",numero2l,")","and","(",numero3l,">",numero1l,")","=",comparaciones)
