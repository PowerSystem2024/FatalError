#Ejercicio1 : ELiminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos , por ultimo mostrar la lista

#Creamos la lista
lista = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

#Convertimos la lista en un conjunto para eliminar los duplicados
conjunto = set(lista)
print(conjunto)

#Convertimos el conjunto en una lista
lista = list(conjunto)

#Mostramos la lista

print(lista)