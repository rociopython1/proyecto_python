from excepciones import ClienteInvalidoError
from logs import registrar_log


class Cliente:
    def __init__(self, nombre, correo, telefono):
        try:
            if not nombre or len(nombre.strip()) < 2:
                raise ClienteInvalidoError("El nombre del cliente no es válido")

            if not correo or "@" not in correo:
                raise ClienteInvalidoError("El correo del cliente no es válido")
            
            if not telefono.isdigit() or len(telefono) < 10:
               raise ClienteInvalidoError("El teléfono del cliente no es válido")

            # Encapsulación
            self.__nombre = nombre.strip()
            self.__correo = correo.strip()
            self.__telefono = telefono.strip()
            
        except ClienteInvalidoError as e:
            registrar_log("ERROR", str(e), "clientes")
            print("Error:", e)

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo
    
    def get_telefono(self):
        return self.__telefono

    # Mostrar información
    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo} | Telefono: {self.__telefono}"
    
    