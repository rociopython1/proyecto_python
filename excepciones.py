class ErrorSistema(Exception):
    pass

class ClienteInvalidoError(ErrorSistema):
    pass

class ServicioNoDisponibleError(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass
