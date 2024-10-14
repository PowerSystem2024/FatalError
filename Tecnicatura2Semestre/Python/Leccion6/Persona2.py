class Persona2:
    def __init__(self, nombre, apellido,edad): # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property # Decorador
    def nombre(self): # Metodo Getter
        print("Estamos utilizando el metodo Get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Metodo Setter
        print("Estamos utilizando el metodo Set")
        self._nombre = nombre

    @property # Decorador
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property  # Decorador
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":

    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre) # Llamamos al metodo getter
    persona1.nombre = "Juan Pedro" # Llamamos el metodo setter
    print(persona1.nombre) # Otra vez con el metodo getter
    print(persona1.mostrar_detalles()) # Llamamos el metodo mostrar detalles
    print(persona1.apellido)
    print(persona1.edad)
    # Atributo read-only (solo lectura) seria la edad, por que no tiene el metodo set
    print(persona1.edad)
    # Tarea crear 3 obetos o más, utilizando los metodos Getter and Setter
    # para modificar, y mostrar los cambios

    # Objeto numero 1 de la tarea
    persona2 = Persona2("Matias", "Fuentes", 22)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = "Agustin"
    persona2.apellido = "Cangialosi"
    persona2.edad = 23
    print(persona2.mostrar_detalles())

    # Objeto numero 2 de la tarea
    persona3 = Persona2("Nicolas", "Barrera", 21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = "Ignacio"
    persona3.apellido = "Esquivel"
    persona3.edad = 22
    print(persona3.mostrar_detalles())

    # Objeto numero 3 de la tarea
    persona4 = Persona2("Franco", "Luna", 23)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = "Brian"
    persona4.apellido = "Noriega"
    persona4.edad = 24
    print(persona4.mostrar_detalles())

    print(__name__)