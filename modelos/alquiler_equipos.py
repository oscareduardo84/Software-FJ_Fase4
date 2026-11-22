
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE: ALQUILER DE EQUIPOS
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

from modelos.servicio import Servicio


class AlquilerEquipos(Servicio):
    """
    Clase que representa el servicio de alquiler
    de equipos tecnologicos de Software FJ.
    """

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        tipo_equipo,
        cantidad_disponible
    ):
        super().__init__(identificador, nombre, tarifa_base)

        self.__tipo_equipo = tipo_equipo
        self.__cantidad_disponible = cantidad_disponible

        self.validar_parametros()

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    def validar_parametros(self):
        if (
            not isinstance(self.__tipo_equipo, str)
            or not self.__tipo_equipo.strip()
        ):
            raise ValueError(
                "El tipo de equipo es obligatorio."
            )

        if (
            not isinstance(self.__cantidad_disponible, int)
            or isinstance(self.__cantidad_disponible, bool)
            or self.__cantidad_disponible < 0
        ):
            raise ValueError(
                "La cantidad disponible debe ser un entero no negativo."
            )

        return True

    def validar(self):
        super().validar()
        self.validar_parametros()
        return True

    def reservar_equipos(self, cantidad):
        """
        Descuenta del inventario los equipos reservados.
        """

        if (
            not isinstance(cantidad, int)
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ValueError(
                "La cantidad debe ser un entero positivo."
            )

        if not self.disponible:
            raise ValueError(
                "El servicio de alquiler no esta disponible."
            )

        if cantidad > self.__cantidad_disponible:
            raise ValueError(
                "No hay suficientes equipos disponibles."
            )

        self.__cantidad_disponible -= cantidad

        return self.__cantidad_disponible

    def devolver_equipos(self, cantidad):
        """
        Devuelve al inventario los equipos de una reserva cancelada.
        """

        if (
            not isinstance(cantidad, int)
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ValueError(
                "La cantidad debe ser un entero positivo."
            )

        self.__cantidad_disponible += cantidad

        return self.__cantidad_disponible

    def calcular_costo(
        self,
        duracion,
        descuento=0,
        impuesto=0,
        cantidad=1
    ):
        """
        Calcula el costo del alquiler de equipos.
        """

        self.validar_costo(duracion, descuento, impuesto)

        if (
            not isinstance(cantidad, int)
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise ValueError(
                "La cantidad solicitada debe ser un entero positivo."
            )

        if not self.disponible:
            raise ValueError(
                "El servicio de alquiler no esta disponible."
            )

        if cantidad > self.__cantidad_disponible:
            raise ValueError(
                "No hay suficientes equipos disponibles."
            )

        subtotal = self.tarifa_base * duracion * cantidad

        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = (
            subtotal_con_descuento * (impuesto / 100)
        )

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Codigo: {self.identificador} | "
            f"Tipo de equipo: {self.__tipo_equipo} | "
            f"Tarifa por unidad de tiempo: "
            f"${self.tarifa_base:,.2f} | "
            f"Cantidad disponible: {self.__cantidad_disponible} | "
            f"Disponible: {'Si' if self.disponible else 'No'}"
        )
