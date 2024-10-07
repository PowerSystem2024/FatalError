class Cubo: 
    """
    Crear la clase cubo con los atributos, ancho,alto y profundidad con un metodo
    calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad 
    que el usuario ingrese los valores
    """
    
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundiad = profundidad
        
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundiad
    
ancho = int(input('Digite el ancho del cubo: '))
alto = int(input('Digite el alto del cubo: '))
profundiad = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(ancho,alto,profundiad)

print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')
    
    
    