# se importan las clases padre
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,lado,color):
        # super().__init__(ancho, alto) = este metodo no se utiliza para herencia multiple
        FiguraGeometrica.__init__(self,lado,lado) # en herencia multiple llamamos al padre
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}' #sobreEscribimos el metodo str dunder
