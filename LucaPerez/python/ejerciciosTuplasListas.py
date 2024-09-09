import math# importamos la libreria math




#Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8)
#crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]

lista = [] # definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento<5:
        lista.append(elemento)
print(lista)

#Ejercicio de matematicas
#Para sacar la  raiz cuadrada de un numero positivo
#usamos la funcion math.sqrt(numero)

numero = int(input("Ingrese un numero positivo: ")) # pedimos al usuario que ingrese un numero positivo
while numero<0: # mientras el numero sea negativo
    numero = int(input("deberia ingresar un numero positivo: ")) # pedimos al usuario que ingrese un numero positivo
    numero = int(input("Ingrese un numero positivo: ")) # pedimos al usuario que ingrese un numero positivo
print("La raiz cuadrada de ",numero," es: ",math.sqrt(numero)) # mostramos la raiz cuadrada del numero ingresado
