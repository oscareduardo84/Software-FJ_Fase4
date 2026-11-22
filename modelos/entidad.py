
# ==============================================
# PROYECTO: SOFTWARE FJ
# CLASE ABSTRACTA: ENTIDAD
# FASE 4 - PROGRAMACION ORIENTADA A OBJETOS
# ==============================================

# Importamos las herramientas para crear clases abstractas.
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificador, nombre):
        # Validamos que el identificador no este vacio.
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacio.")

        # Validamos que el nombre sea un texto valido.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        # Aplicamos encapsulacion usando atributos privados.
        self.__identificador = identificador.strip()
        self.__nombre = nombre.strip()

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self.__identificador

    @property
    def nombre(self):
        """Permite consultar el nombre."""
        return self.__nombre

    @abstractmethod
    def describir(self):
        """
        Metodo abstracto que cada clase derivada
        debe implementar para describir su entidad.
        """
        pass

    @abstractmethod
    def validar(self):
        """
        Metodo abstracto que obliga a las clases
        derivadas a implementar sus validaciones.
        """
        pass
