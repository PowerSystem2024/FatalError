class Rectangulo:
    """
    Crear una clase llamada Rectangulo , debe tener 2 atributos : altura y base
    el nombre del metood sera calcular area utilizando la formula:

    area = base * altura . pero la base y la altura deben ser ingresadas por el usuarioy los objetos
    deben ser 3
    """

    def __init__(self,altura,base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.altura * self.base


base = int(input("Digite el numero para la base del rectangulo"))
altura = int(input("Digite el numero para la altura"))
rectangulo1 = Rectangulo(base,altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")


