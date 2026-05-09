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
    """
    Clase que gestiona las reservas del sistema.
    Integra: cliente, servicio, duración y estado.
    Permite confirmar y cancelar la reserva con manejo de excepciones.
    """

    def __init__(self, cliente, servicio, duracion):
        """
        Constructor de la clase Reserva.

        :param cliente:  Instancia de la clase Cliente (quién hace la reserva).
        :param servicio: Instancia de Servicio o sus clases hijas (qué se reserva).
        :param duracion: Duración de la reserva en horas o días (número positivo).
        """
        try:
            # --- Validación del cliente ---
            # Verificamos que el objeto recibido sea realmente un Cliente válido.
            if not isinstance(cliente, Cliente):
                raise ValueError("El objeto proporcionado no es un Cliente válido.")

            # --- Validación de la duración ---
            # Usamos el Validador del sistema para asegurar que sea un número positivo.
            self.duracion = Validador.validar_numero_positivo(duracion, "Duración", "reservas")

            # --- Asignación de atributos ---
            self.cliente = cliente        # Cliente que realiza la reserva
            self.servicio = servicio      # Servicio que se va a reservar
            self.estado = "Pendiente"     # Estado inicial de toda reserva nueva

            # Registramos la creación de la reserva en el log del sistema
            registrar_log("INFO", f"Reserva creada para el cliente: {cliente.get_nombre()}", "reservas")

        except (ValueError, ErrorSistema) as e:
            # Si algo falla en la creación, lo registramos y relanzamos el error
            registrar_log("ERROR", f"Error al crear la reserva: {str(e)}", "reservas")
            print(f"Error crítico en Reserva: {e}")
            raise

    def confirmar(self):
        """
        Confirma la reserva cambiando su estado de 'Pendiente' a 'Confirmada'.
        No se puede confirmar una reserva que ya está cancelada.
        """
        try:
            # No tiene sentido confirmar algo que ya fue cancelado
            if self.estado == "Cancelada":
                raise Exception("No se puede confirmar una reserva ya cancelada.")

            # Si ya está confirmada, simplemente lo informamos
            if self.estado == "Confirmada":
                print("La reserva ya se encuentra confirmada.")
                return

            # Cambiamos el estado y registramos el evento
            self.estado = "Confirmada"
            registrar_log("INFO", f"Reserva de {self.cliente.get_nombre()} CONFIRMADA.", "reservas")
            print(f"✔ Reserva confirmada exitosamente. Estado actual: {self.estado}")

        except Exception as e:
            # Cualquier error en la confirmación queda registrado
            registrar_log("WARNING", f"Fallo al confirmar reserva: {str(e)}", "reservas")
            print(f"Atención: {e}")

    def cancelar(self):
        """
        Cancela la reserva cambiando su estado a 'Cancelada'.
        No se puede cancelar una reserva que ya fue procesada.
        """
        try:
            # Una reserva procesada ya no puede cancelarse
            if self.estado == "Procesada":
                raise Exception("No es posible cancelar una reserva que ya fue procesada.")

            # Si ya está cancelada, lo notificamos
            if self.estado == "Cancelada":
                print("La reserva ya se encuentra cancelada.")
                return

            # Cambiamos el estado y registramos el evento
            self.estado = "Cancelada"
            registrar_log("INFO", f"Reserva de {self.cliente.get_nombre()} CANCELADA.", "reservas")
            print(f"✖ Reserva cancelada. Estado actual: {self.estado}")

        except Exception as e:
            # Cualquier error en la cancelación queda registrado
            registrar_log("WARNING", f"Fallo al cancelar reserva: {str(e)}", "reservas")
            print(f"Error: {e}")

    def mostrar_resumen(self):
        """
        Devuelve un resumen en texto con la información completa de la reserva:
        cliente, servicio, duración y estado actual.
        """
        nombre_servicio = getattr(self.servicio, 'nombre', 'Desconocido')
        return (
            f"--- RESUMEN DE RESERVA ---\n"
            f"Cliente:  {self.cliente.get_nombre()}\n"
            f"Servicio: {nombre_servicio}\n"
            f"Duración: {self.duracion} unidades\n"
            f"Estado:   {self.estado}\n"
            f"--------------------------"
        )
