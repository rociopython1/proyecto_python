class ErrorSoftwareFJ(Exception):
    pass

class ErrorReservaInvalida(ErrorSoftwareFJ):
    pass

class ErrorServicioNoDisponible(ErrorSoftwareFJ):
    pass

class ErrorDatoClienteInvalido(ErrorSoftwareFJ):
    pass

from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
    