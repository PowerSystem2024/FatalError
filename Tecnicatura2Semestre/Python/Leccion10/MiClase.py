class MiClase:

    variable_clase = "Esta es una variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
MiClase1 = MiClase("Esta es una variable de instancia")
print(MiClase1.variable_instancia)
print(MiClase1.variable_clase)

MiClase2 = MiClase("Esta es otra prueba de variable de instancia")
print(MiClase2.variable_instancia)
print(MiClase2.variable_clase)