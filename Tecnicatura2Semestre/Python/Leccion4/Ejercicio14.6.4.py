# Comenzamos con funciones
# mi funcion() #No se puede llamar antes de definir a una funcion
# Definimos una funcion
def mi_funcion(): #Para identificar a la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la tecnicatura")

mi_funcion()
mi_funcion()

# Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Bentancud"]
show(person[0], person[1])
show(*person)
person2 = ("Morena","Ruiz")
show(*person2)
person3 = {"lastName": "Lucero", "name": "natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print("Esto se termino")

# List comprension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"]
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "mx"},
           {"name": "Stella Artois", "country": "belgium"},
           ]
Arg = [b for b in bottleC if b["country"]== "arg"]
print(Arg)
print(bottleC)

#Paso de argumentos
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de YT")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge","Lucero")
mi_funcion2("Analia","Pedrosa")
mi_funcion2("Ariel","Bentancud")

def sumar(a,b):
  return a + b 
print(f"El resultado de la suma es: {sumar(55, 45)}")