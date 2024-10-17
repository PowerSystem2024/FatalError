class Persona : 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    def __str__(self): #Override = sobreescribir


        return f"Persona : [ Nombre: {self.__nombre}, Edad: {self.__edad}]"

class Empleado(Persona) :
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo


    def __str__(self):


        return f"Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}"

emplado1 = Empleado("luca",40,75000)
print(emplado1.edad)
print(emplado1.nombre)
print(emplado1.sueldo)
#Tarea encapsular los atributos y agregar los metodos getters y setters
#Crear otro objeto , pasar los datos para nombre,edad y sueldo
#mostrar estos datos , luego modificar y mostrar nuevamente

empleado2 = Empleado("juan",30,50000)
print(empleado2.edad)
print(empleado2.nombre)
print(empleado2.sueldo)
empleado2.nombre = "juan perez"
empleado2.edad = 35
empleado2.sueldo = 60000
print(empleado2.edad)
print(empleado2.nombre)
print(empleado2.sueldo)

