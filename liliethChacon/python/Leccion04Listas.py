# lista = Ariel, Lliliana, Natalia, Osvaldo

nombres = ["Naty","Osvaldo","Lily","Ariel"]

print(nombres) # accedemos a la lista de manera general
print(nombres[0]) #accedemos a la lista de manera individual
print(nombres[1]) #accedemos a la lista de manera individual
print(nombres[3]) #accedemos a la lista de manera individual
print(nombres[-1]) #Para recorrer del ultimo numero en adelante podemos utilizar los numeros negativos
print(nombres[-2]) #Para recorrer del ultimo numero en adelante podemos utilizar los numeros negativos
print()
#RECUPERAR UN RANGO DE LA LISTA

print(nombres[0:2]) #Recorre desde el indice 0 hasta el 1
print(nombres[ :3]) #Recorre desde el indice 0 hasta el 2
print(nombres[1: ]) #Recorre desde el indice 1 hasta el final
print()
#MODIFICAMOS UN VALOR
print()
nombres[2] = "Liliana" #Modificamos lili por liliana
nombres[0] = "Natalia" #modificamos nati por natalia
print(nombres)
print()

#ITERAR UNA LISTA

for nombre in nombres: #nombre es singular, la lista es plural 
    print(nombre)
else:
    print("Se acabaron los nombres de la lista")
    print()

#PREGUNTAMOS CUANTOS ELEMENTOS TIENE

print(len(nombres))
print()

#AGREGAMOS UN ELEMENTO AL FINAL DE LA LISTA

nombres.append("lilieth")
print(nombres)
print()

#AGREGAMOS UN ELEMENTO EN UN INDICE ESPECIFICO DE LA LISTA
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)
print()

#ELIMINAMOS UN ELEMENTO DE NUESTRA LISTA
nombres.remove("Alberto")
print(nombres)
print()

#ELIMINAMOS EL ÚLTIMO ELEMENTO DE LA LISTA
nombres.pop()
print(nombres)
print()

#ELIMINAMOS UN INDICE ESPECIFICO
del nombres[2] #Eliminamos a Debora
print(nombres) 
print()

#ELIMINAMOS TODOS LOS ELEMENTOS
nombres.clear()
print(nombres)
print()

#ELIMINAMOS LA LISTA
del nombres
# print(nombres) nos dirá que "nombres" no está definido a modo de error

print("****************************************************")
print("              DEFINIMOS TUPLAS")
print("****************************************************")
print()
cocina = ("cuchara","cuchillo","tenedor")
print(cocina)
print(len(cocina))#Muestra la cantidad de elementos

#ACCEDEMOS A UN ELEMENTO 
print(cocina[0])#el elemento 0 es "cuchara"
print(cocina[-1])#el elemento -1 es "tenedor"

#ACCEDER A UN RANGO 
print(cocina[0:2]) #nos mostrará solo dos elementos

#EJEMPLO
verduras = ("papa",) # en la tupla se necesita aunque sea un elemento y la coma ","
print()
#RECORREMOS ELEMENTOS EN LA TUPLA
for cocinar in cocina:
    print(cocinar, end=" ") #para la funcion print finaliza con un espacio en vez de un salto de linea

#Es una mala práctica pero se pueden modificar las tuplas, pasandolas a listas y a tuplas nuevamente
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print(cocina)
print()

#ELIMINAMOS LA TUPLA
del cocina
print(cocina)
