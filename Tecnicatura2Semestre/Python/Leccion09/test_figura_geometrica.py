from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,"azul")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())

