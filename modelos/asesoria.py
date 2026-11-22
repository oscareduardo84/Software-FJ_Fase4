
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE: ASESORIA ESPECIALIZADA
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

# Importamos la clase Servicio.
from modelos.servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """
    Clase que representa los servicios de asesoria
    especializada ofrecidos por Software FJ.
    """

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        especialidad,
        modalidad
    ):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador, nombre, tarifa_base)

        # Guardamos los atributos propios de la asesoria.
        self.__especialidad = especialidad
        self.__modalidad = modalidad

        # Validamos los parametros especificos.
        self.validar_parametros()

    @property
    def especialidad(self):
        """Permite consultar la especialidad."""
        return self.__especialidad

    @property
    def modalidad(self):
        """Permite consultar la modalidad."""
        return self.__modalidad

    def validar_parametros(self):
        """
        Comprueba que la especialidad y modalidad
        de la asesoria sean correctas.
        """

        if (
            not isinstance(self.__especialidad, str)
            or not self.__especialidad.strip()
        ):
            raise ValueError(
                "La especialidad de la asesoria es obligatoria."
            )

        if (
            not isinstance(self.__modalidad, str)
            or self.__modalidad.strip().lower()
            not in ("virtual", "presencial")
        ):
            raise ValueError(
                "La modalidad debe ser virtual o presencial."
            )

        return True

    def validar(self):
        """
        Sobrescribe la validacion general del servicio.
        """

        super().validar()
        self.validar_parametros()

        return True

    def calcular_costo(
        self,
        duracion,
        descuento=0,
        impuesto=0
    ):
        """
        Calcula el costo de una asesoria especializada.

        La tarifa base corresponde al precio por hora.
        """

        # Validamos los parametros del calculo.
        self.validar_costo(duracion, descuento, impuesto)

        # Comprobamos la disponibilidad.
        if not self.disponible:
            raise ValueError(
                "La asesoria no se encuentra disponible."
            )

        # Calculamos el subtotal.
        subtotal = self.tarifa_base * duracion

        # Aplicamos el descuento.
        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        # Calculamos los impuestos.
        valor_impuesto = (
            subtotal_con_descuento * (impuesto / 100)
        )

        # Calculamos el total.
        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    def describir(self):
        """
        Devuelve una descripcion de la asesoria.
        """

        return (
            f"Servicio: {self.nombre} | "
            f"Codigo: {self.identificador} | "
            f"Especialidad: {self.__especialidad} | "
            f"Modalidad: {self.__modalidad.capitalize()} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"Disponible: {'Si' if self.disponible else 'No'}"
        )
