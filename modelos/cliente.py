
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE: CLIENTE
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos expresiones regulares para validar datos.
import re


class Cliente(Entidad):
    """
    Clase que representa a los clientes de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        # Inicializamos los atributos heredados de Entidad.
        super().__init__(identificador, nombre)

        # Validamos y almacenamos los datos personales.
        self.__correo = correo
        self.__telefono = telefono

        # Comprobamos que todos los datos sean correctos.
        self.validar()

    @property
    def correo(self):
        """Permite consultar el correo del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Permite consultar el telefono del cliente."""
        return self.__telefono

    def validar(self):
        """
        Valida los datos personales del cliente.
        Genera excepciones cuando encuentra datos incorrectos.
        """

        # Validamos el correo electronico.
        if not isinstance(self.__correo, str):
            raise ValueError("El correo debe ser un texto.")

        correo = self.__correo.strip()

        patron_correo = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"

        if not re.match(patron_correo, correo):
            raise ValueError("El correo electronico no es valido.")

        # Validamos el telefono.
        if not isinstance(self.__telefono, str):
            raise ValueError("El telefono debe ingresarse como texto.")

        telefono = self.__telefono.strip()

        # Permitimos numeros, espacios y el signo +.
        patron_telefono = r"^\+?[0-9]{7,15}$"

        telefono_limpio = telefono.replace(" ", "")

        if not re.match(patron_telefono, telefono_limpio):
            raise ValueError("El numero de telefono no es valido.")

        # Guardamos los datos limpios.
        self.__correo = correo
        self.__telefono = telefono_limpio

        return True

    def describir(self):
        """
        Devuelve una descripcion general del cliente.
        """

        return (
            f"Cliente: {self.nombre} | "
            f"Identificacion: {self.identificador} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        """
        Permite actualizar el correo del cliente
        verificando que el nuevo dato sea valido.
        """

        correo_anterior = self.__correo
        self.__correo = nuevo_correo

        try:
            self.validar()
            return "Correo actualizado correctamente."

        except ValueError:
            self.__correo = correo_anterior
            raise
