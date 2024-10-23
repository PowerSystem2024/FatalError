from Cuadrado import Cuadrado # importamos las clases
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

print('Creacion de objeto clase Cuadrado'.center(50, '_')) # separador
cuadrado1 = Cuadrado(8,'Azul') #creamos el objeto
cuadrado1.alto = 7
#cuadrado1.ancho = 7
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f'Calculo del área del cuadrado: {cuadrado1.calcular_area()}')

#MRO = METHOD RESOLUTION ORDER
#print(Cuadrado.mro()) #nos muestra el orden en el que fuimos utilizando las clases

print(cuadrado1)
print('Creacion de objeto clase Rectangulo'.center(50,'_')) #separador
rectangulo1 = Rectangulo(3,9,'verde')
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica() no se puede instanciar, es abstracta
print(Cuadrado.mro())