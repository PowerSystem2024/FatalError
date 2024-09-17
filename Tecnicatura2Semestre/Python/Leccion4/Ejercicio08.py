#Ejerciio 8: Menu interactivo - cajero aumatico
#Hacer un programa que simule un cajero autmatico con un saldo 
# inicial de 1000$ y tendra el siguiente menu de opciones
#1. Ingresar dinero en la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dinero disponible
#4. Salir

saldo = 1000
while True:
    print("\t Menu de opciones")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion: "))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar en la cuenta: "))
        saldo += extra
        print(f"Dinero en la cuenta: {saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar: "))
        if retirar > saldo:
            print("No tiene suficiente dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta: {saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta: {saldo}")
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")