#Ejercicio 7: Juego adivina el numero
# Realizar el juego para adivinar un numero . para ello se debe
# generar un numero aleatorio entre 1-100, y luego ir pidiendo que
# numeros indicando "Es mayor" o "Es menor" segun sea mayor o menor
# con respecto a N . El proceso termina cuando el usuario acierta y
#alli se debe mostrar el numero de intentos

import random
print("\t JUEGO ADIVINA EL NUMERO")
aleatorio = random.randint(1,100) # toma el 0 a 100 literal , generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("Ingrese un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\t no es el numero , digite un numero menor")
    elif numero < aleatorio:
        print("\t no es el numero , digite un numero mayor")
    else:
        print("FELICIDADES, adivinaste el numero {aleatorio}")
        break # rompe el ciclo

print(f"Numero de intentos: {contador}") # imprime el numero de intentos
