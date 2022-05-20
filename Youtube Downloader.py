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
Cian = "#00FFEF"
verdeOscuro = "#003300"
verdeClaro = "#00FF00"
Negro = "#000000"

# ------------------------------------------------

# Configurar el logging
log.basicConfig(filename="YoutubeDownloader.log", filemode="w", level=log.DEBUG)

# Obtener tener la Fecha de cuando se ejecuta el script
fecha = datetime.today()
formato = fecha.strftime("%A, %d %B, %Y %H:%M")

log.info(
    f"El programa Descargador de videos de YouTube se ha ejecutado el {formato}"
)

# Bloque de crear la interfaz grafica + cambiar icono + poner el titulo + centrar ventana + Redimensionar ventana

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

# Calculos para el centrado de la ventana
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


# Barra de progresion
class BarraDeProgresion:
    """La clase BarraDeProgresion se encarga de controlar la barra de progresion y de aumentar el progreso de esta"""

    barraProgresionDescarga = Progressbar(Ventana, orient=HORIZONTAL, length=800)

    def AumentarProgreso(self):
        self.GB = 100
        self.download = 0
        self.speed = 1
        while self.download < self.GB:
            time.sleep(0.09)
            self.barraProgresionDescarga['value'] += (self.speed / self.GB) * 100
            self.download += self.speed
            percent.set(str(int((self.download / self.GB) * 100)) + "%")
            text.set(str(self.download) + "/" + str(self.GB) + " files completed")
            Ventana.update_idletasks()


class AumentarDeProgresionEnParalelo:
    """La clase AumentarDeProgresionEnParalelo se encarga de ejecutar en una hilo distinto el aumento de progreso de
    la barra de progreso"""

    def FuncionAumentarDeProgresionEnParalelo(self):
        # Creamos una instancia de la barra de progresion
        self.barraDeProgresion = BarraDeProgresion()

        # Aumentamos el progreso de la barra en un hilo distinto
        self.aumentarProgresoEnParalelo = thr.Thread(target=self.barraDeProgresion.AumentarProgreso())
        self.aumentarProgresoEnParalelo.start()
        log.info(
            "El aumento del progreso de la barra de progresion esta aumentando en un hilo "
            "distinto correctamente"
        )


class Main:
    """La calase Main se encarga de poner en pantalla los botones, etiquetas, etc."""

    def FuncionMain(self):
        # Creamos una instancia de: BarraDeProgresion, Buscar, Descargar, AumentarDeProgresionEnParalelo y CambiarColor
        self.barraDeProgresion = BarraDeProgresion()
        self.buscar = Buscar()
        self.descargarVideo = DescargarVideo()
        self.descargarAudio = DescargarAudio()
        self.aumentarBarraDeProgreso = AumentarDeProgresionEnParalelo()
        self.cambiarColor = CambiarColor()

        # Texto + Caja + Boton de descargar video
        self.Etiqueta_URL = tkinter.Label(
            Ventana,
            text="Introduce la URL del video a descargar",
            font="Helvetica 15",
            bg=Cian,
        )

        self.Etiqueta_URL.pack(pady=10)

        self.URL_Video = tkinter.Entry(
            Ventana, textvariable=Link_Video, font="Helvetica 15", width=70
        )

        self.URL_Video.pack(pady=20)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Boton de ubicacion para guardar el video
        self.Ubicacion = tkinter.Label(
            Ventana, text="Donde quieres guardar el video", font="Helvetica 15", bg=Cian
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
            cursor="hand2"
        )

        self.Boton_Buscar.pack(pady=20)

        self.cambiarColor.FuncionCambiarColor(self.Boton_Buscar, verdeClaro, verdeOscuro)

        self.Boton_Descargar_Video = tkinter.Button(
            Ventana,
            text="Descargar video",
            command=lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarDeProgresionEnParalelo(),
                self.descargarVideo.FuncionDescargarVideo()
            ],
            font="Helvetica 15",
            bg=verdeOscuro,
            cursor="hand2"
        )

        self.Boton_Descargar_Video.place(x=220, y=340)

        self.cambiarColor.FuncionCambiarColor(self.Boton_Descargar_Video, verdeClaro, verdeOscuro)

        self.Boton_Descargar_Audio = tkinter.Button(
            Ventana,
            text="Descargar audio",
            command=lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarDeProgresionEnParalelo(),
                self.descargarAudio.FuncionDescargarAudio()
            ],
            font="Helvetica 15",
            bg=verdeOscuro,
            cursor="hand2"
        )

        self.Boton_Descargar_Audio.place(x=420, y=340)

        self.cambiarColor.FuncionCambiarColor(self.Boton_Descargar_Audio, verdeClaro, verdeOscuro)

        # Crear la etiqueta de la barra de progresion
        self.Etiqueta_Barra_Progress = tkinter.Label(
            Ventana, text="Progreso de la descarga", font="Helvetica 15", bg=Cian
        )

        # Poner etiqueta en pantalla
        self.Etiqueta_Barra_Progress.pack(pady=77)

        # Ubicamos la barra de progresion
        self.barraDeProgresion.barraProgresionDescarga.place(x=13, y=470)

        percentLabel = tkinter.Label(Ventana, textvariable=percent)
        percentLabel.pack(pady=20)

        taskLabel = tkinter.Label(Ventana, textvariable=text)
        taskLabel.pack(pady=10)

        # ---------------------------------------------------------------------------


class Buscar:
    """La clase buscar se encarga de preguntar y almacenar en una variable la ruta en la cual el usuario desea guardar
    el video una vez que se haya descargado"""

    def FuncionBuscar(self):
        log.info(
            "Se ha hecho click en el boton de seleccionar la direccion de la carpeta donde se quiere "
            "guardar el video descargado"
        )

        self.Directorio_Descarga = filedialog.askdirectory(initialdir="Directorio seleccionado")
        Ubicacion_Video_PC.set(self.Directorio_Descarga)


class DescargarVideo:
    """La clase DescargarVideo se encarga de obtener el video que le hemos pasado por la URL, descargarlo y guardarlo
    en la carpeta seleccionada por el usuario"""

    def FuncionDescargarVideo(self):
        # Crear instancia de la barra de progresion
        self.barra = BarraDeProgresion()

        log.info("Se ha hecho click en el boton de descargar")

        try:

            self.URL = Link_Video.get()

            log.info("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = Ubicacion_Video_PC.get()

            log.info(
                "Se ha obtenido la direccion de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = pytube.YouTube(self.URL)

            log.info("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_highest_resolution()

            log.info("Se ha obtenido la resolucion mas alta del video a descargar")

            self.Descargar_Video.download(self.Carpeta_Guardar_Video)

        except:

            messagebox.showerror(
                "Error de descarga", "No se ha conseguido descargar el video"
            )

            self.barra.barraProgresionDescarga['value'] = 0

            percent.set("")

            log.info("La variale que guarda el porcentaje de la descarga de se "
                     "ha restablecido correctamente")

            log.info("El video no se ha podido descargar, algo ha salido mal")

        else:

            messagebox.showinfo(
                "Completado", "Puedes encontar tu video en:\n" + self.Carpeta_Guardar_Video
            )

            self.barra.barraProgresionDescarga['value'] = 0

            percent.set("")

            log.info("La variale que guarda el porcentaje de la descarga de se "
                     "ha restablecido correctamente")

            log.info("La descarga del video se ha completado correctamente")


class DescargarAudio:
    """La clase DescargarAudio se encarga de obtener el audio del video que le hemos pasado por la URL y una vez
    descargado le cambia la extension a mp3 y lo guarda en la carpeta seleccionada por el usuario"""

    def FuncionDescargarAudio(self):
        # Crear instancia de la barra de progresion
        self.barra = BarraDeProgresion()

        log.info("Se ha hecho click en el boton de descargar")

        try:

            self.URL = Link_Video.get()

            log.info("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = Ubicacion_Video_PC.get()

            log.info(
                "Se ha obtenido la direccion de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = pytube.YouTube(self.URL)

            log.info("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_audio_only()

            log.info("Se ha obtenido el audio del video a descargar")

            self.base, self.ext = os.path.splitext(self.Descargar_Video.download(self.Carpeta_Guardar_Video))

            self.cambiarFormato = self.base + '.mp3'

            os.rename(self.Descargar_Video.download(self.Carpeta_Guardar_Video), self.cambiarFormato)

        except:

            messagebox.showerror(
                "Error de descarga", "No se ha conseguido descargar el audio"
            )

            self.barra.barraProgresionDescarga['value'] = 0

            percent.set("")

            log.info("La variale que guarda el porcentaje de la descarga de se "
                     "ha restablecido correctamente")

            log.info("El audio no se ha podido descargar, algo ha salido mal")

        else:

            messagebox.showinfo(
                "Completado", "Puedes encontar el audio del video en:\n" + self.Carpeta_Guardar_Video
            )

            self.barra.barraProgresionDescarga['value'] = 0

            percent.set("")

            log.info("La variale que guarda el porcentaje de la descarga de se "
                     "ha restablecido correctamente")

            log.info("La descarga del audio del video se ha completado correctamente")


class CambiarColor:
    """La clase CambiarColor controla que los botones cambien de color al pasar el ratón por encima de ellos"""

    def FuncionCambiarColor(self, button, colorRatonDentro, colorRatonFuera):
        button.bind(
            "<Enter>", func=lambda e: button.config(background=colorRatonDentro)
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


# -----------------------------------------

# Crear instancia de la clase que inicia el programa
interfaz = Main()

# Llamar a la funcion que inicia el programa
interfaz.FuncionMain()

# Actualizar ventana
Ventana.mainloop()
