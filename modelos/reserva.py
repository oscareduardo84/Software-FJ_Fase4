
# ============================================================
# CLASE RESERVA
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ
# ============================================================

from datetime import datetime

from modelos.cliente import Cliente
from modelos.servicio import Servicio
from modelos.alquiler_equipos import AlquilerEquipos


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion, cantidad=1):

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError(
                "El identificador de la reserva no puede estar vacío."
            )

        if not isinstance(cliente, Cliente):
            raise TypeError(
                "La reserva debe estar asociada a un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise TypeError(
                "La reserva debe estar asociada a un servicio válido."
            )

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser un número mayor que cero."
            )

        if (
            not isinstance(cantidad, int)
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ValueError(
                "La cantidad debe ser un número entero mayor que cero."
            )

        self.__identificador = identificador.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__cantidad = cantidad
        self.__estado = "Pendiente"
        self.__costo_total = 0
        self.__fecha_creacion = datetime.now()

        # Indica si esta reserva descontó equipos del inventario.
        self.__equipos_reservados = False

    # --------------------------------------------------------
    # PROPIEDADES
    # --------------------------------------------------------

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def estado(self):
        return self.__estado

    @property
    def costo_total(self):
        return self.__costo_total

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # --------------------------------------------------------
    # CONFIRMAR RESERVA
    # --------------------------------------------------------

    def confirmar(self):
        """Confirma una reserva pendiente y controla el inventario."""

        if self.__estado != "Pendiente":
            raise RuntimeError(
                "Solamente se pueden confirmar reservas pendientes."
            )

        if not self.__servicio.disponible:
            raise RuntimeError(
                "El servicio seleccionado no está disponible."
            )

        # Validamos los datos del cliente y del servicio.
        self.__cliente.validar()
        self.__servicio.validar()

        # Si es un alquiler, descontamos los equipos.
        if isinstance(self.__servicio, AlquilerEquipos):
            self.__servicio.reservar_equipos(self.__cantidad)
            self.__equipos_reservados = True

        self.__estado = "Confirmada"

        return "La reserva fue confirmada correctamente."

    # --------------------------------------------------------
    # CALCULAR COSTO
    # --------------------------------------------------------

    def calcular_costo(self, descuento=0, impuesto=0):
        """
        Calcula el costo mediante el método sobrescrito
        de cada tipo de servicio (polimorfismo).
        """

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise RuntimeError(
                "No se puede calcular el costo de una reserva cancelada o procesada."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 100
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 100
        ):
            raise ValueError(
                "El impuesto debe estar entre 0 y 100."
            )

        # Los alquileres permiten calcular el costo por cantidad.
        if isinstance(self.__servicio, AlquilerEquipos):
            self.__costo_total = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto,
                self.__cantidad
            )
        else:
            self.__costo_total = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto
            )

        return self.__costo_total

    # --------------------------------------------------------
    # PROCESAR RESERVA
    # --------------------------------------------------------

    def procesar(self, descuento=0, impuesto=0):
        """Calcula el costo y cambia el estado a Procesada."""

        if self.__estado != "Confirmada":
            raise RuntimeError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        self.calcular_costo(descuento, impuesto)

        self.__estado = "Procesada"

        return (
            f"Reserva {self.__identificador} procesada correctamente. "
            f"Costo total: ${self.__costo_total:,.2f}"
        )

    # --------------------------------------------------------
    # CANCELAR RESERVA
    # --------------------------------------------------------

    def cancelar(self):
        """Cancela una reserva y devuelve los equipos si corresponde."""

        if self.__estado == "Procesada":
            raise RuntimeError(
                "No se puede cancelar una reserva procesada."
            )

        if self.__estado == "Cancelada":
            raise RuntimeError(
                "La reserva ya se encuentra cancelada."
            )

        # Si se habían reservado equipos, los devolvemos.
        if (
            isinstance(self.__servicio, AlquilerEquipos)
            and self.__equipos_reservados
        ):
            self.__servicio.devolver_equipos(self.__cantidad)
            self.__equipos_reservados = False

        self.__estado = "Cancelada"

        return "La reserva fue cancelada correctamente."

    # --------------------------------------------------------
    # DESCRIBIR RESERVA
    # --------------------------------------------------------

    def describir(self):
        """Muestra la información general de la reserva."""

        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Cantidad: {self.__cantidad}\n"
            f"Estado: {self.__estado}\n"
            f"Costo total: ${self.__costo_total:,.2f}\n"
            f"Fecha: {self.__fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )

