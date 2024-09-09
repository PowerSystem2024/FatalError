'''
EJERCICIO 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
Ejemplo de ejecución: 0,3,6,9

EJERCICIO 2: Crear un rango de numeros de 2 a 6 e imprimelos
Ejemplo de ejecución: 2,3,4,5,6

EJERCICIO 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, 
en lugar de 1 en uno  en 1. Ejemplo de ejecución: 3,5,7,9

'''
#EJERCICIO 1
print("----------------")
print("EJERCICIO 1")
for i in range(10):
    if(i % 3 == 0):
        print(i)
print("----------------")

#EJERCICIO 2
print("----------------")
print("EJERCICIO 2")
for i in range(2,7):
    print(i)
print("----------------")

#EJERCICIO 3
print("----------------")
print("EJERCICIO 3")
for i in range(3,11,2):
     print(i)
print("----------------")






