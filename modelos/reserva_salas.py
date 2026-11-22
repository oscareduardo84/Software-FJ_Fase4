
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE: RESERVA DE SALAS
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

# Importamos la clase Servicio.
from modelos.servicio import Servicio


class ReservaSalas(Servicio):
    """
    Clase que representa el servicio de alquiler de salas
    ofrecido por Software FJ.
    """

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        capacidad,
        ubicacion
    ):

        # Inicializamos los atributos de la clase padre.
        super().__init__(identificador, nombre, tarifa_base)

        # Guardamos los atributos propios de la sala.
        self.__capacidad = capacidad
        self.__ubicacion = ubicacion

        # Validamos los parametros especificos.
        self.validar_parametros()

    @property
    def capacidad(self):
        """Permite consultar la capacidad de la sala."""
        return self.__capacidad

    @property
    def ubicacion(self):
        """Permite consultar la ubicacion de la sala."""
        return self.__ubicacion

    def validar_parametros(self):
        """
        Comprueba que la capacidad y ubicacion
        de la sala sean validas.
        """

        if (
            not isinstance(self.__capacidad, int)
            or isinstance(self.__capacidad, bool)
            or self.__capacidad <= 0
        ):
            raise ValueError(
                "La capacidad de la sala debe ser un entero positivo."
            )

        if (
            not isinstance(self.__ubicacion, str)
            or not self.__ubicacion.strip()
        ):
            raise ValueError(
                "La ubicacion de la sala es obligatoria."
            )

        return True

    def validar(self):
        """
        Sobrescribe la validacion general del servicio.
        """

        super().validar()
        self.validar_parametros()

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """
        Calcula el costo del alquiler de una sala.

        La tarifa base corresponde al precio por hora.
        Se aplican descuentos e impuestos opcionales.
        """

        self.validar_costo(duracion, descuento, impuesto)

        if not self.disponible:
            raise ValueError("La sala no se encuentra disponible.")

        # Calculamos el costo inicial.
        subtotal = self.tarifa_base * duracion

        # Aplicamos el descuento.
        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        # Calculamos el impuesto.
        valor_impuesto = subtotal_con_descuento * (impuesto / 100)

        # Obtenemos el costo total.
        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    def describir(self):
        """
        Devuelve una descripcion del servicio de reserva de salas.
        """

        return (
            f"Servicio: {self.nombre} | "
            f"Codigo: {self.identificador} | "
            f"Capacidad: {self.__capacidad} personas | "
            f"Ubicacion: {self.__ubicacion} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"Disponible: {'Si' if self.disponible else 'No'}"
        )
