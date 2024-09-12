# Solicitar al usuario que ingrese una frase  
frase = input("Ingresa una frase: ")  

# Inicializar variables  
frase_sin_espacios = ""  
longitud = 0  

# Recorrer cada carácter en la frase  
for caracter in frase:  
    # Verificar si el carácter no es un espacio  
    if caracter != " ":  
        # Agregar el carácter a la nueva frase  
        frase_sin_espacios += caracter  
        # Incrementar el contador de longitud  
        longitud += 1  

# Mostrar la frase sin espacios y la longitud  
print("Frase final:", frase_sin_espacios)  
print("N° de caracteres:", longitud)