
# ============================================================
# EXCEPCIONES PERSONALIZADAS
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ
# ============================================================


class ErrorSistema(Exception):
    """Excepción principal del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se genera cuando no se encuentra un cliente."""
    pass


class ServicioNoEncontradoError(ErrorSistema):
    """Se genera cuando no se encuentra un servicio."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta algún problema."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass


class CapacidadInsuficienteError(ErrorSistema):
    """Se genera cuando no hay suficientes equipos disponibles."""
    pass
