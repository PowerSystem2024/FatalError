class Cubo:
    """
    Crear la clase cubo con los atributos , ancho , alto y profundidad , con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valroes
    """

    def __init__(self,ancho,altura,profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad


ancho = int(input("Digite el ancho de el cubo"))
altura=int(input("DIgite la altura de el cubo"))
profundidad = int(input("Digite la profundidad de el cubo"))

cubo1 = Cubo(ancho,altura,profundidad)
print(f"El volumen de el cubo es: {cubo1.calcular_volumen()}")

