#Ejercicio 2 : operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas y que a continuacion
#Cree las siguientes listas (en las que no deben haber elementos repetidos)
#1 Lista de palabras que aparecen en las listas
#2 Lista de palabras que aparecen en la primera lista pero no en la segunda
#3 Lista de palabras que aparecen en la segunda lista pero no en la primera
#4 Lista de palabras que aparecen en ambas listas

#Creamos las listas
lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [6,7,8,9,10,9,8,7,6,6,7]

#Convertimos las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) #Union
solo1 = list(conjunto1 - conjunto2) #Diferencia solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) #Diferencia solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) #Interseccion mostramos ambas listas

print("Union: ",union)
print("Solo en la primera: ",solo1)
print("Solo en la segunda: ",solo2)
print("Interseccion: ",interseccion)
