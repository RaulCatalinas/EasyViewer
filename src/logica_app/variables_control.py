"""Variales de control para el funcionamiento de la app"""

from tkinter import StringVar, BooleanVar

UBICACION_VIDEO = StringVar()
LINK_VIDEO = StringVar()
NOMBRE_DESCARGA = StringVar()
DESCARGADO_CORRECTAMENTE = BooleanVar()


class VariablesControl:
    """Variables de control para la app"""

    @staticmethod
    def get_ubicacion_video():
        """
        Devuelve la ubicacion seleccionada por el usuario
        :return: La ubicacion seleccionada por el usuario
        """

        return UBICACION_VIDEO.get()

    @staticmethod
    def get_nombre_descarga():
        """
        Devuelve el nombre de la descarga
        :return: El nombre de la descarga
        """

        return NOMBRE_DESCARGA.get()

    @staticmethod
    def set_nombre_descarga(nombre):
        """Establece el nombre para el video descargado"""

        NOMBRE_DESCARGA.set(nombre)

    @staticmethod
    def set_descargado_correctamente(descargado):
        """
        Establece si un video/audio se ha descargado bien o no
        """

        DESCARGADO_CORRECTAMENTE.set(descargado)

    @staticmethod
    def get_descargado_correctamente():
        """
        Devuelve si un video se ha descargado bien o no
        :return: Si un video se ha descragado bien o no
        """

        return DESCARGADO_CORRECTAMENTE.get()

    @staticmethod
    def get_url_video():
        """
        Devuelve la url del video
        :return: La url del video
        """

        return LINK_VIDEO.get()
