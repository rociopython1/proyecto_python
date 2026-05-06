from excepciones import ErrorDeFormato, ErrorDeRango
from logs import registrar_log

class Validador:
    @staticmethod
    def validar_numero_positivo(valor, nombre_campo, modulo):
        """Asegura que las duraciones y costos sean válidos."""
        try:
            numero = float(valor)
            if numero <= 0:
                raise ErrorDeRango(f"{nombre_campo} no puede ser cero o negativo.")
            return numero
        except ValueError:
            error_msg = f"El valor '{valor}' en {nombre_campo} debe ser un número."
            registrar_log("ERROR", error_msg, modulo)
            raise ErrorDeFormato(error_msg)
        except ErrorDeRango as e:
            registrar_log("WARNING", str(e), modulo)
            raise
