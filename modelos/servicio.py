
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE ABSTRACTA: SERVICIO
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos herramientas para crear clases abstractas.
from abc import abstractmethod


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa_base):

        # Inicializamos los atributos heredados.
        super().__init__(identificador, nombre)

        # Validamos que la tarifa sea un numero positivo.
        if (
            not isinstance(tarifa_base, (int, float))
            or isinstance(tarifa_base, bool)
            or tarifa_base <= 0
        ):
            raise ValueError("La tarifa base debe ser un numero positivo.")

        # Atributos privados para aplicar encapsulacion.
        self.__tarifa_base = float(tarifa_base)
        self.__disponible = True

    @property
    def tarifa_base(self):
        """Permite consultar la tarifa base del servicio."""
        return self.__tarifa_base

    @property
    def disponible(self):
        """Permite consultar la disponibilidad del servicio."""
        return self.__disponible

    def cambiar_disponibilidad(self, estado):
        """
        Cambia el estado de disponibilidad del servicio.
        """

        if not isinstance(estado, bool):
            raise ValueError("La disponibilidad debe ser True o False.")

        self.__disponible = estado

    def validar(self):
        """
        Comprueba que los datos generales del servicio
        sean correctos.
        """

        if not self.nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if self.__tarifa_base <= 0:
            raise ValueError("La tarifa base debe ser positiva.")

        return True

    def validar_costo(self, duracion, descuento=0, impuesto=0):
        """
        Valida los parametros utilizados para calcular costos.
        """

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duracion debe ser un numero positivo.")

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or descuento < 0
            or descuento > 100
        ):
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or impuesto < 0
            or impuesto > 100
        ):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        return True

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """
        Metodo abstracto para calcular el costo
        de cada servicio especializado.
        """
        pass

    @abstractmethod
    def describir(self):
        """
        Metodo abstracto que describe cada servicio.
        """
        pass

    @abstractmethod
    def validar_parametros(self):
        """
        Metodo abstracto para validar los parametros
        particulares de cada servicio.
        """
        pass
