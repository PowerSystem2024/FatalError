class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, edad): #Metodo para inicializar objetos se lo llama metodo init dunder
        #atributos de metodo = variable
        self.nombre = nombre    
        self.apellido = apellido
        self.edad = edad
        
persona1 = Persona('Ariel','Betancud',40) #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo','Giordanini',45)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} {persona2.edad}')
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} {persona1.edad}')