#Lista = Ariel , Liliana, Luca,Osvaldo

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


