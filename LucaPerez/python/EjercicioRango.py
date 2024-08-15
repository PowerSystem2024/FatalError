# Ejercicio 1 :Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
Rango = [0,1,2,3,4,5,6,7,8,9,10]
print("Rango de 0 a 10 con numeros divisibles entre 3")

print(Rango[0])
print(Rango[3])
print(Rango[6])
print(Rango[9])


# Ejercicio 2 : crear un rango de numeros de 2 a 6 e imprimelos

Rango1 = [2,3,4,5,6]
print("Rango con valores de inicio = 2 y fin 6")
print(Rango1[0])
print(Rango1[1])
print(Rango1[2])
print(Rango1[3])
print(Rango1[4])

# Ejercicio 3 : Crear un rango de valores de 3 a 10 pero con incremento 2 en 2

rango2= [3,5,7,9]
print("Rango con valores de inicio = 3 , fin 10, incremento = 2")
print(rango2[0])
print(rango2[1])
print(rango2[2])
print(rango2[3])

# Ejercicio 1 :Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2 : crear un rango de numeros de 2 a 6 e imprimelos
print("Rango con valores de inicio = 2 y fin 6")
rango = range (2,7)
for i in rango:
    print(i)

# Ejercicio 3 : Crear un rango de valores de 3 a 10 pero con incremento 2 en 2
print("Rango con valores de inicio = 3 , fin 10, incremento = 2")
for i in range(3,11,2):
    print(i)

#Probando rama python

#Definimos una tupla
cocina =('cuchara','cuchillo' , 'tenedor')
print(len(cocina))