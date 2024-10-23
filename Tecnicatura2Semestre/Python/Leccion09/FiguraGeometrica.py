from abc import ABC, abstractmethod #importamos clase abstracta y un decorador para definir metodos abstractos

class FiguraGeometrica(ABC): #clase padre Hija de ABC
    def __init__(self, ancho, alto): #dunder init
        if  self._validar_valores(ancho):
            self._ancho = ancho # encapsulamos con un guion bajo
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')
    
    @property # metodo get
    def ancho(self):
        return self._ancho
        
    @ancho.setter #metodo set
    def ancho(self,ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'valor erroneo ancho: {ancho}')
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self,alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'valor erroneo alto: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass
    
    def __str__(self): # metodo dunder str, devuelve una representación en cadena
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
    def _validar_valores(self,valor): #Metodo encapsulado
        return True if 0 < valor < 10 else False