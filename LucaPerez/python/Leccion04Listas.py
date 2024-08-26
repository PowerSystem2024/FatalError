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
