#Lista = Ariel , Liliana, Luca,Osvaldo
#Colecciones en python

#Las istas son colecciones de elementos que pueden ser de diferentes tipos
#
nombres = ['Luca' , 'Fiorella','Mariano', 'Bianca']
print(nombres)
#print(nombres[0]) #Mostrando Elemento que queramos
#print(nombres[1])
#print(nombres[3]) 
#print(nombres[-1]) # mostramos el ultimo numero
#print(nombres[-2]) # Mostramos el penultimo

#Recuperar un rango de la lista

print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, 1, 2

#desde el indice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor 
nombres[3] = 'Gustavo'
nombres[0] = 'Lucas'
print(nombres)

#Iterar una lista

for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')


#Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo') # funcion append que agrega un elemento a la lista
nombres.append('Mariano')
nombres.append(True)
nombres.append(10)
print(nombres)

# insetar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] # del significa delete(Eliminar)
print(nombres)

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres

#Definimos una tupla
cocina =('cuchara','cuchillo' , 'tenedor')
print(len(cocina))

#Acceder a un elemento , para esto utilizamos corchetes no parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ('papa',) # una tupla nesecita aunque sea de un elemento la coma
# de lo contrario solo eria un tipo str cadena

#Recorremos los elemento de la tupla
for cocinar in cocina:#Print esta usando \n para saltos de lineas
    print(cocinar, end=' ')  # usamos end= para eliminar los saltos de linea


#NO ES BUENA PRACTICA ESTA CONVERSION DE TUPLA  A LISTA
cocinaLista = list(cocina) # conversion de tupla a lista
cocinaLista[0] = 'plato' # modificacion
cocina = tuple(cocinaLista) # conversion de lista a tupla
print('\n',cocina) 

# del cocina esto elimina la tupla

# tipo set // cambia el orden de impresion
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) # cantidad de elementos

#Revisar si un elemento existe dentro del set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') # solo agrega un elemento
print(planetas)

#Eliminar un elemento, puede generar un error si no existe
planetas.remove('Venus')
print(planetas)
planetas.discard('Tierra') # no genera error si no existe

#limpiar el set
planetas.clear()
print(planetas)

#Eliminar el set
#del planetas

#Diccionarios
#maradona : 10 un dicionario esta compuesto por dos elementos
#una llave y un valor
#dict = {'llave':'valor'}(key:value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistemas de Base de Datos'
}

print(diccionario)

#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print (diccionario)

#Acceder a un elemento con la llave 
print(diccionario['IDE'])   #IDE es la llave

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD')) 


#Modificar elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Recorrer los elementos del diccionario
for termino in diccionario:
    print(termino) # solo imprime las llaves

#nesecitamos una funcion para mostrar los valores
for termino , valor in diccionario.items():
    print(termino,valor) 

#otras maneras de recorrer un diccionario
for termino in diccionario.keys(): # keys() solo imprime las llaves
    print(termino) # solo imprime las llaves

for valor in diccionario.values():
    print(valor) # solo imprime los valores

#Comprobar si existe un elemento
print('IDE' in diccionario) # True

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('PK')
print(diccionario)

#Limpiar el diccionario
#diccionario.clear()
#print(diccionario)

#Eliminar el diccionario
#del diccionario

#concatenar Listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2 #concatenacion de listas
print(lista3)

lista1.extend([7,8,9,1]) #funcion extend para agregar elementos a una lista
print(lista3)

print(lista3.index(5))#Saber que numero hay en cierta posicion
#print(lista3.index(5,1,7)) #buscar un elemento en un rango

#como saber cuantas veces se repite un elemento
print(lista3.count(1)) #cuenta cuantos valores iguales hay de la lista

#para poner al reves una lista
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitiendo sus elementos
lista = lista3* 2
print(lista)

# metodo de ordenamiento en python en una funcion
lista3.sort() # ordena la lista
print(lista3)
lista3.sort(reverse=True) # ordena la lista de manera inversa
print(lista3)

tupla = (1,"Hola", 6.78,[1,2,78, "Hola"]) #Puede tener diferentes tipos de datos
print(tupla)

print(4 in tupla) # False
#Lo que podemos usar dentro de tuplas son : index , count ,len
#en  tuplas se puede convertir de tupla a lista y viceversa

#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'Bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('HOLA')
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 no esta en el conjunto1 True


#Como hacer la igualda de dos conjuntos
print(conjunto2 == conjunto1) #False

#Operaciones en conjuntos
#Union
conjunto3 = conjunto1 | conjunto2 #union de conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #elementos que estan en conjunto1 pero no en conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1 #elementos que estan en conjunto2 pero no en conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que estan en conjunto1 o conjunto2 pero no en ambos
print(conjunto3)


conjunto3 = conjunto1 | conjunto2 #union de conjuntos
print(conjunto1.issubset(conjunto3)) #True si conjunto1 es subconjunto de conjunto3
print(conjunto2.issubset(conjunto3)) #True si conjunto2 es subconjunto de conjunto3
print(conjunto3.issubset(conjunto1)) #False si conjunto3 es subconjunto de conjunto1
print(conjunto3.issubset(conjunto2)) #False si conjunto3 es subconjunto de conjunto2


print(conjunto3.issuperset(conjunto1)) #True si conjunto3 es superconjunto de conjunto1
print(conjunto3.issuperset(conjunto2)) #True si conjunto3 es superconjunto de conjunto
print(conjunto2.issuperset(conjunto3)) #True si conjunto2 es superconjunto de conjunto3

#COmo saber si ambos conjuntos son disconexos , esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

#convertir un conjunto totalmente inmutable
conjunto1 = frozenset # no se puede modificar
# no se puede agregar elementos

#repaso diccionarios
diccionarioNuevo = {'azul':'blue','rojo':'red','verde':'green'}
print(diccionarioNuevo)

#Como eliminar
del diccionarioNuevo['azul']
print(diccionarioNuevo)

#los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Luca":{"Edad": 20, "Estatura": 1.75}, "Fiorella": [22,1.65]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre":"Lionel Messi", "Edad": 35, "Posicion":"Delantero","Precio" : "100 Millones"},
    11: {"Nombre":"Angel Di Maria", "Edad": 33, "Posicion":"Delantero","Precio" : "50 Millones"},
    12: {"Nombre":"Nicolas Otamendi", "Edad": 33, "Posicion":"Defensa","Precio" : "30 Millones"},
    13: {"Nombre":"Gonzalo Montiel", "Edad": 25, "Posicion":"Defensa","Precio" : "20 Millones"},
    14: {"Nombre":"Emiliano Martinez", "Edad": 29, "Posicion":"Arquero","Precio" : "40 Millones"},
    15: {"Nombre":"Leandro Paredes", "Edad": 27, "Posicion":"Mediocampista","Precio" : "60 Millones"},
    16: {"Nombre":"Rodrigo De Paul", "Edad": 27, "Posicion":"Mediocampista","Precio" : "70 Millones"},
    17: {"Nombre":"Lautaro Martinez", "Edad": 24, "Posicion":"Delantero","Precio" : "80 Millones"},
    18: {"Nombre":"Guido Rodriguez", "Edad": 27, "Posicion":"Mediocampista","Precio" : "50 Millones"},
    19: {"Nombre":"Julian Alvarez", "Edad": 21, "Posicion":"Delantero","Precio" : "30 Millones"},
    20: {"Nombre":"Nahuel Molina", "Edad": 23, "Posicion":"Defensa","Precio" : "20 Millones"},
    21: {"Nombre":"Lucas Alario", "Edad": 28, "Posicion":"Delantero","Precio" : "40 Millones"},
    22: {"Nombre":"German Pezzella", "Edad": 30, "Posicion":"Defensa","Precio" : "30 Millones"},
    23: {"Nombre":"Juan Musso", "Edad": 27, "Posicion":"Arquero","Precio" : "40 Millones"},
    24: {"Nombre":"Alejandro Gomez", "Edad": 33, "Posicion":"Mediocampista","Precio" : "60 Millones"},
    25: {"Nombre":"Nicolas Tagliafico", "Edad": 28, "Posicion":"Defensa","Precio" : "40 Millones"},
    26: {"Nombre":"Agustin Marchesin", "Edad": 33, "Posicion":"Arquero","Precio" : "50 Millones"},
    27: {"Nombre":"Alexis Mac Allister", "Edad": 23, "Posicion":"Mediocampista","Precio" : "30 Millones"}
}

for llave in seleccionArgentina.items():
    print(llave)

print("Tenemos cargados en la seleccion Argentina a la cantidad de jugadores", end=' ')
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1,2,3]

#Agregar elementos a la pila
pila.append(4)
pila.append(5)
print(pila)

#Sacar elementos de la pila desde el final
elementoBorrado = pila.pop() #sacamos el ultimo elemento
print(f"salio el elemento {elementoBorrado}")
print(f"la pila ahora quedo asi:{pila}")

#Colas con listas
#Estructuras de datos tipo fifo(First input / First Output)
cola = ["Luca","Fiorella","Mariano","Bianca"]

#Agregar elementos a la cola
cola.append("Alberto")
cola.append("Debora")
print(cola)

#Sacar elementos de la cola desde el inicio
seRetira = cola.pop(0) #sacamos el primer elemento
print(f"salio el elemento {seRetira}")
print(f"la cola ahora quedo asi:{cola}")

seRetira = cola.pop(1)
print(f"salio el elemento {seRetira}")
print(f"la cola ahora quedo asi:{cola}") 

#Recorremos el diccionario seleccion argentina
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')



