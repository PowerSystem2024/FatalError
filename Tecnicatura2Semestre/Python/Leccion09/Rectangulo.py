from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color): #Creamos la clase
    def __init__(self, ancho, alto, color): #metodo dunder init
        FiguraGeometrica.__init__(self, ancho, alto) #traemos los atributos del padre, al ser herencia multimple no se utiliza super
        Color.__init__(self,color) # traemos los atributos del padre, al ser herencia multiple no se utiliza super

    def calcular_area(self): #metodo que calcula el area 
        return self.alto * self.ancho
    
    def __str__(self): # sobre-carga dunder str, crea una cadena con los otros dundrs padres
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'