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