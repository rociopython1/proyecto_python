from abc import abstractmethod
# Importamos la base que dejó el compañero en prueba_companero.py
from prueba_companero import Servicio 
from excepciones import ServicioNoDisponibleError
from logs import registrar_log

# --- CLASES DERIVADAS (Herencia y Polimorfismo) ---

class ReservaSala(Servicio):
    """Implementación para el servicio de alquiler de salas."""
    def calcular_costo(self, horas):
        # El costo depende de la cantidad de horas
        return self.costo_base * horas

    def validar_parametros(self, horas):
        if horas <= 0:
            raise ServicioNoDisponibleError("Las horas de reserva deben ser mayores a 0.")

class AlquilerEquipo(Servicio):
    """Implementación para el servicio de alquiler de equipos."""
    def calcular_costo(self, dias, descuento_aplicable=False):
        # Aplicamos polimorfismo con un parámetro opcional para descuentos
        total = self.costo_base * dias
        if dias > 5 or descuento_aplicable:
            total *= 0.85  # 15% de descuento por alquiler largo
        return total

    def validar_parametros(self, dias):
        if dias <= 0:
            raise ServicioNoDisponibleError("Los días de alquiler deben ser mayores a 0.")

class AsesoriaEspecializada(Servicio):
    """Implementación para asesorías con cargo administrativo fijo."""
    def calcular_costo(self, sesiones):
        # Costo por sesiones más un cargo fijo administrativo
        cargo_fijo = 20000
        return (self.costo_base * sesiones) + cargo_fijo

    def validar_parametros(self, sesiones):
        if sesiones < 1:
            raise ServicioNoDisponibleError("Debe agendar al menos una sesión.")
        # --- PRUEBA RAPIDA PARA SAMUEL ---
if __name__ == "__main__":
    print("--- Probando Módulo de Servicios de Samuel ---")
    
    # Probamos la Sala (Polimorfismo)
    sala = ReservaSala("Sala Creativa", 45000)
    print(f"Servicio: {sala.nombre} | Costo por 4 horas: ${sala.calcular_costo(4)}")
    
    # Probamos el Equipo con descuento
    equipo = AlquilerEquipo("Cámara Pro", 100000)
    print(f"Servicio: {equipo.nombre} | Costo por 6 días (con descuento): ${equipo.calcular_costo(6)}")