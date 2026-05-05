# Importar excepción personalizada y función para registrar errores
from excepciones import ClienteInvalidoError
from logs import registrar_log

# Clase que representa un cliente del sistema
class Cliente:
    def __init__(self, nombre, correo):
        try:
# Validar que el nombre del cliente no esté vacío
            if not nombre:
                raise ClienteInvalidoError("El nombre del cliente no puede estar vacío")

            if not correo:
                raise ClienteInvalidoError("El correo del cliente no puede estar vacío")

            self.nombre = nombre
            self.correo = correo

        except ClienteInvalidoError as e:
            registrar_log(str(e))
            print("Error:", e)
    
    