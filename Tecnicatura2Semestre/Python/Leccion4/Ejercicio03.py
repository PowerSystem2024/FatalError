# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en una lista, cuando el usuario
# Introduzca un numero 0, nuestro programa dejaria de insertar.
# por ultimo, mostrar los numeros ordenados de menor a mayor.
lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # la lista esta ordenada con esta funcion
print(f"Lista ordenada: {lista}")
