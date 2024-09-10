#sumar los numeros pares dentro de un rango 
a= int(input ("Ingrese desde dondo comienza la suma: "))
b= int(input("Ingrese hasta donde quiere que sea la suma: "))
suma=0
for i in range(a, b+1):
    if i % 2 == 0: #si el numero es par
       suma += i
print(f"La suma de numeros pares dentro del rango es: {suma}")