from clientes import Cliente
from logs import registrar_log
from excepciones import ErrorSistema
from validaciones import Validador

# Intentamos importar Servicio desde el archivo que lo tenga definido.
# Si aún no existe, usamos una clase temporal para no romper el código.
try:
    from servicios import Servicio
except ImportError:
    class Servicio:
        def __init__(self, nombre):
            self.nombre = nombre

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if not isinstance(cliente, Cliente):
                raise ValueError("El objeto proporcionado no es un Cliente válido.")

            self.duracion = Validador.validar_numero_positivo(duracion, "Duración", "reservas")
            self.cliente = cliente        
            self.servicio = servicio      
            self.estado = "Pendiente"    

            registrar_log("INFO", f"Reserva creada para el cliente: {cliente.get_nombre()}", "reservas")

        except (ValueError, ErrorSistema) as e:
            
            registrar_log("ERROR", f"Error al crear la reserva: {str(e)}", "reservas")
            print(f"Error crítico en Reserva: {e}")
            raise

    def confirmar(self):
        try:
            if self.estado == "Cancelada":
                raise Exception("No se puede confirmar una reserva ya cancelada.")

            if self.estado == "Confirmada":
                print("La reserva ya se encuentra confirmada.")
                return

            self.estado = "Confirmada"
            registrar_log("INFO", f"Reserva de {self.cliente.get_nombre()} CONFIRMADA.", "reservas")
            print(f"✔ Reserva confirmada exitosamente. Estado actual: {self.estado}")

        except Exception as e:
            registrar_log("WARNING", f"Fallo al confirmar reserva: {str(e)}", "reservas")
            print(f"Atención: {e}")

    def cancelar(self):
        try:
            if self.estado == "Procesada":
                raise Exception("No es posible cancelar una reserva que ya fue procesada.")

            if self.estado == "Cancelada":
                print("La reserva ya se encuentra cancelada.")
                return

            self.estado = "Cancelada"
            registrar_log("INFO", f"Reserva de {self.cliente.get_nombre()} CANCELADA.", "reservas")
            print(f"✖ Reserva cancelada. Estado actual: {self.estado}")

        except Exception as e:
            registrar_log("WARNING", f"Fallo al cancelar reserva: {str(e)}", "reservas")
            print(f"Error: {e}")

    def mostrar_resumen(self):
        nombre_servicio = getattr(self.servicio, 'nombre', 'Desconocido')
        return (
            f"--- RESUMEN DE RESERVA ---\n"
            f"Cliente:  {self.cliente.get_nombre()}\n"
            f"Servicio: {nombre_servicio}\n"
            f"Duración: {self.duracion} unidades\n"
            f"Estado:   {self.estado}\n"
            f"--------------------------"
        )
