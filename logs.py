# Registrar errores del sistema en un archivo de texto
def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(mensaje + "\n")
        
        