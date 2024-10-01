class Aritmetica:
    """
    el nombre de este tipo de comentario es: doctString
    esto es documentacion de la clase en python
    vamos a hacer algunas operaciones
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        #Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta (self):
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


Aritmetica = Aritmetica(7,9) # Le pasamos los argumentos para los operandos
print(Aritmetica.sumar())
print(f"La resta de los numeros es: {Aritmetica.resta()}")
print(f"La multiplicacion de los numeros es: {Aritmetica.multiplicacion()}")
print(f"La division de los numeros es: {Aritmetica.dividir()}")
