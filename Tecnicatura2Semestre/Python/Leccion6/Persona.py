class Persona: #Creamos una clase
    
    def __init__(self, nombre, apellido,dni, edad,*args,**kwargs): #Metodo para inicializar objetos se lo llama metodo init dunder
        #*args agrega tupla
        #**kwargs agrega diccionario
        #atributos de metodo = variable
        self.nombre = nombre    
        self.apellido = apellido
        self._dni = dni # este atributo está encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        
    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son {self.kwargs}')
        
persona1 = Persona('Ariel','Betancud',999999,40) #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo','Giordanini',999999,45)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} {persona2.edad}')
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Modificamos los datos del objeto 1
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Los atributos son: caracteristicas
#Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) - no es comun de utilizar 

persona1.telefono = '123456789'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

persona3 = Persona('Rogelio','Romero',999999,22,'Telefno','2614445557','Calle Lopez',823,'Manzana',77,'Casa',18,Altura=1.83,Peso=185,CFavorito='Azul',Auto='Citroen',Modelo = 2021)

persona3.mostrar_detalle()
#print(persona3._dni) #esto no se debe utilizar (está encapsulado), esto dice que desconocemos python