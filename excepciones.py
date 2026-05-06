class ErrorSistema(Exception):
    """Clase base para todos los errores del Software FJ."""
    pass

class ErrorDeFormato(ErrorSistema):
    """Para cuando meten letras en campos de números."""
    pass

class ErrorDeRango(ErrorSistema):
    """Para valores numéricos imposibles (ej. -10 horas)."""
    pass

class ClienteInvalidoError(ErrorSistema):
    pass

class ServicioNoDisponibleError(ErrorSistema):
    pass
