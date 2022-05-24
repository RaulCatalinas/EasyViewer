# Descargador de videos de youtube en mp4

import logging as log
import os
import threading as thr
import time
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

import pytube

# -----------------------------------------------

# Bloque de colores
azulEtiquetas = "#00FFEF"
verdeOscuro = "#003300"
verdeClaro = "#00FF00"
Negro = "#000000"
amarilloOscuro = "#333300"
amarilloClaro = "#FFFF00"

# ------------------------------------------------

# Configurar el logging
log.basicConfig(filename="YoutubeDownloader.log", filemode="w", level=log.DEBUG)

# Obtener tener la Fecha de cuando se ejecuta el script
fecha = datetime.today()
formato = fecha.strftime("%A, %d %B, %Y %H:%M")

log.info(f"El programa Descargador de videos de YouTube se ha ejecutado el {formato}")

# Bloque de crear la interfaz gráfica + cambiar icono + poner el titulo + centrar ventana + Redimensionar ventana

# Ventana
Ventana = tkinter.Tk()

# Fijar tamaño
Ventana.resizable(False, False)

# Título de la ventana
Ventana.title("Youtube Downloader")

# Icono personalizado
Icono = Ventana.iconbitmap(".\Icon\Icono.ico")

# Establecer color de fondo
Ventana.config(bg=Negro)

# Medida ventana
Ancho = 830
Alto = 520

# Cálculos para el centrado de la ventana
Ancho_Ventana = Ventana.winfo_screenwidth()
Alto_Ventana = Ventana.winfo_screenheight()

Coordenada_X = int((Ancho_Ventana / 2) - (Ancho / 2))
Coordenada_Y = int((Alto_Ventana / 2) - (Alto / 2))

# Redimensionar Ventana
Ventana.geometry("{}x{}+{}+{}".format(Ancho, Alto, Coordenada_X, Coordenada_Y))

# -----------------------------------------

# Bloque de crear el programa que descargara el video

# Almacenar URL del video + almacenar al ubicacion donde se va a guardar el video
Link_Video = StringVar()
Ubicacion_Video_PC = StringVar()

# Para aumentar el progreso de la barra de progresion
percent = StringVar()
text = StringVar()


# Barra de progresión
class BarraDeProgresion:
    # Crear barra de progresion
    barraProgresionDescarga = Progressbar(Ventana, orient=HORIZONTAL, length=800)

    def AumentarProgreso(self):
        """
        Es una función que aumenta el valor de una barra de progreso en un 1% cada 0,09 segundos hasta llegar al 100%
        """
        self.GB = 100
        self.download = 0
        self.speed = 1
        while self.download < self.GB:
            time.sleep(0.09)
            self.barraProgresionDescarga["value"] += (self.speed / self.GB) * 100
            self.download += self.speed
            percent.set(str(int((self.download / self.GB) * 100)) + "%")
            text.set(str(self.download) + "/" + str(self.GB) + " files completed")
            Ventana.update_idletasks()


class AumentarBarraDeProgresionEnParalelo:
    def FuncionAumentarBarraDeProgresionEnParalelo(self):
        """
        Creamos una instancia de la barra de progreso, luego creamos un hilo que llama a la función que aumenta la barra
        de progreso
        """
        # Creamos una instancia de la barra de progresion
        self.barraDeProgresion = BarraDeProgresion()

        # Aumentamos el progreso de la barra en un hilo distinto
        self.aumentarProgresoEnParalelo = thr.Thread(
            target=self.barraDeProgresion.AumentarProgreso()
        )
        self.aumentarProgresoEnParalelo.start()
        log.info(
            "El aumento del progreso de la barra de progresion esta aumentando en un hilo "
            "distinto correctamente"
        )


class Main:
    def FuncionMain(self):
        """
        Crea la GUI para el programa.
        """
        # Creamos una instancia de: BarraDeProgresion, Buscar, Descargar, AumentarBarraDeProgresionEnParalelo y CambiarColor
        self.barraDeProgresion = BarraDeProgresion()
        self.buscar = Buscar()
        self.descargarVideo = DescargarVideo()
        self.descargarAudio = DescargarAudio()
        self.aumentarBarraDeProgreso = AumentarBarraDeProgresionEnParalelo()
        self.cambiarColor = CambiarColor()

        # Texto + Caja + Botón de descargar video
        self.Etiqueta_URL = tkinter.Label(
            Ventana,
            text="Introduce la URL del video a descargar",
            font="Helvetica 15",
            bg=azulEtiquetas,
        )

        self.Etiqueta_URL.pack(pady=10)

        self.URL_Video = tkinter.Entry(
            Ventana, textvariable=Link_Video, font="Helvetica 15", width=70
        )

        self.URL_Video.pack(pady=20)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicacion para guardar el video
        self.Ubicacion = tkinter.Label(
            Ventana,
            text="Donde quieres guardar el video",
            font="Helvetica 15",
            bg=azulEtiquetas,
        )

        self.Ubicacion.pack(pady=35)

        self.Ubicacion_Video = tkinter.Entry(
            Ventana, width=70, textvariable=Ubicacion_Video_PC, font="Helvetica 15"
        )

        self.Ubicacion_Video.pack(pady=5)

        self.Boton_Buscar = tkinter.Button(
            Ventana,
            text="Seleccionar ubicación",
            command=lambda: [self.buscar.FuncionBuscar()],
            font="Helvetica 15",
            bg=verdeOscuro,
            cursor="hand2",
        )

        self.Boton_Buscar.pack(pady=20)

        self.cambiarColor.FuncionCambiarColor(
            self.Boton_Buscar, verdeClaro, verdeOscuro
        )

        self.Boton_Descargar_Video = tkinter.Button(
            Ventana,
            text="Descargar video",
            command=lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                self.descargarVideo.FuncionDescargarVideo(),
            ],
            font="Helvetica 15",
            bg=amarilloOscuro,
            cursor="hand2",
        )

        self.Boton_Descargar_Video.place(x=220, y=340)

        self.cambiarColor.FuncionCambiarColor(
            self.Boton_Descargar_Video, amarilloClaro, amarilloOscuro
        )

        self.Boton_Descargar_Audio = tkinter.Button(
            Ventana,
            text="Descargar audio",
            command=lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                self.descargarAudio.FuncionDescargarAudio(),
            ],
            font="Helvetica 15",
            bg=amarilloOscuro,
            cursor="hand2",
        )

        self.Boton_Descargar_Audio.place(x=420, y=340)

        self.cambiarColor.FuncionCambiarColor(
            self.Boton_Descargar_Audio, amarilloClaro, amarilloOscuro
        )

        # Crear la etiqueta de la barra de progresion
        self.Etiqueta_Barra_Progress = tkinter.Label(
            Ventana,
            text="Progreso de la descarga",
            font="Helvetica 15",
            bg=azulEtiquetas,
        )

        # Poner etiqueta en pantalla
        self.Etiqueta_Barra_Progress.pack(pady=77)

        # Ubicamos la barra de progresion
        self.barraDeProgresion.barraProgresionDescarga.place(x=13, y=470)

        # ---------------------------------------------------------------------------


class Buscar:
    def FuncionBuscar(self):
        """
        Abre un cuadro de diálogo de archivo y establece el valor de la variable "Ubicacion_Video_PC" al directorio
        seleccionado por el usuario
        """
        log.info(
            "Se ha hecho click en el botón de seleccionar la dirección de la carpeta donde se quiere "
            "guardar el video descargado"
        )

        self.Directorio_Descarga = filedialog.askdirectory(
            initialdir="Directorio seleccionado"
        )
        Ubicacion_Video_PC.set(self.Directorio_Descarga)


class DescargarVideo:
    def FuncionDescargarVideo(self):
        """
        Descarga un video de YouTube y lo guarda en una carpeta que el usuario elija
        """
        # Crear instancia de la barra de progresion
        self.barra = BarraDeProgresion()

        log.info("Se ha hecho click en el botón de descargar")

        try:

            self.URL = Link_Video.get()

            log.info("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = Ubicacion_Video_PC.get()

            log.info(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = pytube.YouTube(self.URL)

            log.info("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_highest_resolution()

            log.info("Se ha obtenido la resolución mas alta del video a descargar")

            self.Descargar_Video.download(self.Carpeta_Guardar_Video)

        except:

            messagebox.showerror(
                "Error de descarga", "No se ha conseguido descargar el video"
            )

            self.barra.barraProgresionDescarga["value"] = 0

            percent.set("")

            log.info(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.info("El video no se ha podido descargar, algo ha salido mal")

        else:

            messagebox.showinfo(
                "Completado",
                "Puedes encontrar tu video en:\n" + self.Carpeta_Guardar_Video,
            )

            self.barra.barraProgresionDescarga["value"] = 0

            percent.set("")

            log.info(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.info("La descarga del video se ha completado correctamente")


class DescargarAudio:
    def FuncionDescargarAudio(self):
        """
        Descarga el audio de un vídeo de YouTube y lo guarda en la carpeta que el usuario haya elegido
        """
        # Crear instancia de la barra de progresion
        self.barra = BarraDeProgresion()

        log.info("Se ha hecho click en el botón de descargar")

        try:

            self.URL = Link_Video.get()

            log.info("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = Ubicacion_Video_PC.get()

            log.info(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = pytube.YouTube(self.URL)

            log.info("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_audio_only()

            log.info("Se ha obtenido el audio del video a descargar")

            self.base, self.ext = os.path.splitext(
                self.Descargar_Video.download(self.Carpeta_Guardar_Video)
            )

            self.cambiarFormato = self.base + ".mp3"

            os.rename(
                self.Descargar_Video.download(self.Carpeta_Guardar_Video),
                self.cambiarFormato,
            )

        except:

            messagebox.showerror(
                "Error de descarga", "No se ha conseguido descargar el audio"
            )

            self.barra.barraProgresionDescarga["value"] = 0

            percent.set("")

            log.info(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.info("El audio no se ha podido descargar, algo ha salido mal")

        else:

            messagebox.showinfo(
                "Completado",
                "Puedes encontrar el audio del video en:\n"
                + self.Carpeta_Guardar_Video,
            )

            self.barra.barraProgresionDescarga["value"] = 0

            percent.set("")

            log.info(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.info("La descarga del audio del video se ha completado correctamente")


class CambiarColor:
    def FuncionCambiarColor(self, button, colorRatonDentro, colorRatonFuera):
        """
        Toma un botón y dos colores, y vincula el botón para cambiar de color cuando el mouse ingresa y deja el botón

        :param button: El botón al que desea cambiar el color
        :param colorRatonDentro: El color del botón cuando el mouse está sobre él
        :param colorRatonFuera: El color del botón cuando el mouse no está sobre él
        """
        button.bind(
            "<Enter>", func=lambda e: button.config(background=colorRatonDentro)
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


# -----------------------------------------

# Crear instancia de la clase que inicia el programa
interfaz = Main()

# Llamar a la función que inicia el programa
interfaz.FuncionMain()

# Actualizar ventana
Ventana.mainloop()
