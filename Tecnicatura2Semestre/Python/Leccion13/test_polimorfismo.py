from Empleado import Empleado 
from Gerente import Gerente

def imprimir_detalles(objeto):
   # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
     print(objeto.departamento)

empleado = Empleado ("Toribio", 888)
imprimir_detalles(empleado)

gerente = Gerente("Morena", 888888, "Sistemas")
imprimir_detalles(gerente)