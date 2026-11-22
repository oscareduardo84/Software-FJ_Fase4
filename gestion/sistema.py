
# ============================================================
# SISTEMA DE GESTION
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ
# ============================================================

import logging
import os

from modelos.cliente import Cliente
from modelos.servicio import Servicio
from modelos.reserva import Reserva

from excepciones.errores import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


# ============================================================
# CONFIGURACION DE REGISTROS (LOGS)
# ============================================================

RUTA_REGISTROS = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "registros"
)

os.makedirs(RUTA_REGISTROS, exist_ok=True)

RUTA_LOG = os.path.join(RUTA_REGISTROS, "sistema.log")

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

if not logger.handlers:
    manejador = logging.FileHandler(RUTA_LOG, encoding="utf-8")
    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    manejador.setFormatter(formato)
    logger.addHandler(manejador)

logger.propagate = False


# ============================================================
# CLASE SISTEMA
# ============================================================

class SistemaGestion:
    """
    Administra los clientes, servicios y reservas
    utilizando listas de objetos, sin base de datos.
    """

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        logger.info("Sistema de gestión iniciado correctamente.")

    # --------------------------------------------------------
    # REGISTRAR CLIENTES
    # --------------------------------------------------------

    def registrar_cliente(self, cliente):

        try:
            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError(
                    "El objeto ingresado no es un cliente válido."
                )

            if any(
                elemento.identificador == cliente.identificador
                for elemento in self.__clientes
            ):
                raise DatosInvalidosError(
                    "Ya existe un cliente con ese identificador."
                )

            cliente.validar()
            self.__clientes.append(cliente)

            logger.info(
                "Cliente registrado: %s",
                cliente.identificador
            )

            return "Cliente registrado correctamente."

        except Exception as error:
            logger.exception("Error al registrar un cliente.")
            if isinstance(error, DatosInvalidosError):
                raise
            raise DatosInvalidosError(
                "No fue posible registrar el cliente."
            ) from error

    # --------------------------------------------------------
    # REGISTRAR SERVICIOS
    # --------------------------------------------------------

    def registrar_servicio(self, servicio):

        try:
            if not isinstance(servicio, Servicio):
                raise DatosInvalidosError(
                    "El objeto ingresado no es un servicio válido."
                )

            if any(
                elemento.identificador == servicio.identificador
                for elemento in self.__servicios
            ):
                raise DatosInvalidosError(
                    "Ya existe un servicio con ese identificador."
                )

            servicio.validar()
            self.__servicios.append(servicio)

            logger.info(
                "Servicio registrado: %s",
                servicio.identificador
            )

            return "Servicio registrado correctamente."

        except Exception as error:
            logger.exception("Error al registrar un servicio.")
            if isinstance(error, DatosInvalidosError):
                raise
            raise DatosInvalidosError(
                "No fue posible registrar el servicio."
            ) from error

    # --------------------------------------------------------
    # BUSCAR CLIENTES
    # --------------------------------------------------------

    def buscar_cliente(self, identificador):

        try:
            return next(
                cliente for cliente in self.__clientes
                if cliente.identificador == identificador
            )

        except StopIteration as error:
            logger.warning(
                "No se encontró el cliente: %s",
                identificador
            )
            raise ClienteNoEncontradoError(
                f"No existe el cliente {identificador}."
            ) from error

    # --------------------------------------------------------
    # BUSCAR SERVICIOS
    # --------------------------------------------------------

    def buscar_servicio(self, identificador):

        try:
            return next(
                servicio for servicio in self.__servicios
                if servicio.identificador == identificador
            )

        except StopIteration as error:
            logger.warning(
                "No se encontró el servicio: %s",
                identificador
            )
            raise ServicioNoEncontradoError(
                f"No existe el servicio {identificador}."
            ) from error

    # --------------------------------------------------------
    # REGISTRAR RESERVAS
    # --------------------------------------------------------

    def registrar_reserva(self, reserva):

        try:
            if not isinstance(reserva, Reserva):
                raise ReservaInvalidaError(
                    "El objeto ingresado no es una reserva válida."
                )

            if any(
                elemento.identificador == reserva.identificador
                for elemento in self.__reservas
            ):
                raise ReservaInvalidaError(
                    "Ya existe una reserva con ese identificador."
                )

            cliente = self.buscar_cliente(
                reserva.cliente.identificador
            )

            servicio = self.buscar_servicio(
                reserva.servicio.identificador
            )

            if cliente is not reserva.cliente:
                raise ReservaInvalidaError(
                    "El cliente de la reserva no está registrado en el sistema."
                )

            if servicio is not reserva.servicio:
                raise ReservaInvalidaError(
                    "El servicio de la reserva no está registrado en el sistema."
                )

            if not servicio.disponible:
                raise ServicioNoDisponibleError(
                    "El servicio seleccionado no está disponible."
                )

            self.__reservas.append(reserva)

            logger.info(
                "Reserva registrada: %s",
                reserva.identificador
            )

            return "Reserva registrada correctamente."

        except Exception as error:
            logger.exception("Error al registrar una reserva.")
            if isinstance(
                error,
                (
                    ReservaInvalidaError,
                    ClienteNoEncontradoError,
                    ServicioNoEncontradoError,
                    ServicioNoDisponibleError
                )
            ):
                raise
            raise ReservaInvalidaError(
                "No fue posible registrar la reserva."
            ) from error

    # --------------------------------------------------------
    # BUSCAR RESERVAS
    # --------------------------------------------------------

    def buscar_reserva(self, identificador):

        try:
            return next(
                reserva for reserva in self.__reservas
                if reserva.identificador == identificador
            )

        except StopIteration as error:
            logger.warning(
                "No se encontró la reserva: %s",
                identificador
            )
            raise ReservaInvalidaError(
                f"No existe la reserva {identificador}."
            ) from error

    # --------------------------------------------------------
    # CONFIRMAR RESERVA
    # --------------------------------------------------------

    def confirmar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            resultado = reserva.confirmar()

            logger.info(
                "Reserva confirmada: %s",
                identificador
            )

            return resultado

        except Exception:
            logger.exception(
                "Error al confirmar la reserva %s.",
                identificador
            )
            raise

    # --------------------------------------------------------
    # PROCESAR RESERVA
    # --------------------------------------------------------

    def procesar_reserva(
        self, identificador, descuento=0, impuesto=0
    ):

        try:
            reserva = self.buscar_reserva(identificador)

            resultado = reserva.procesar(
                descuento,
                impuesto
            )

            logger.info(
                "Reserva procesada: %s",
                identificador
            )

            return resultado

        except Exception:
            logger.exception(
                "Error al procesar la reserva %s.",
                identificador
            )
            raise

    # --------------------------------------------------------
    # CANCELAR RESERVA
    # --------------------------------------------------------

    def cancelar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            resultado = reserva.cancelar()

            logger.info(
                "Reserva cancelada: %s",
                identificador
            )

            return resultado

        except Exception:
            logger.exception(
                "Error al cancelar la reserva %s.",
                identificador
            )
            raise

    # --------------------------------------------------------
    # LISTAR CLIENTES
    # --------------------------------------------------------

    def listar_clientes(self):

        return [
            cliente.describir()
            for cliente in self.__clientes
        ]

    # --------------------------------------------------------
    # LISTAR SERVICIOS
    # --------------------------------------------------------

    def listar_servicios(self):

        return [
            servicio.describir()
            for servicio in self.__servicios
        ]

    # --------------------------------------------------------
    # LISTAR RESERVAS
    # --------------------------------------------------------

    def listar_reservas(self):

        return [
            reserva.describir()
            for reserva in self.__reservas
        ]

    # --------------------------------------------------------
    # CONSULTAR CANTIDADES
    # --------------------------------------------------------

    def obtener_resumen(self):

        return {
            "total_clientes": len(self.__clientes),
            "total_servicios": len(self.__servicios),
            "total_reservas": len(self.__reservas)
        }

    # --------------------------------------------------------
    # CERRAR SISTEMA
    # --------------------------------------------------------

    def cerrar_sistema(self):

        logger.info("Sistema de gestión finalizado.")

        return "El sistema se cerró correctamente."
