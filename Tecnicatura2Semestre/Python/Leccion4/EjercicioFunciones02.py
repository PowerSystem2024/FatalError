# Ejercicio 2: Función con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parametro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos

# Definimos la función para multiplicar
def multiplicar_valores(*numeros):
    resultado = 1 
    for numero in numeros:
        resultado *= numero
    return resultado


# Llamamos la función
print(multiplicar_valores(3, 5, 15, 3)) # Le pasamos los argumentos