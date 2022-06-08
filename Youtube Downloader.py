import logging as log
import os
import threading as thr
import time
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox, Tk, Entry, Button, Label
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
Ventana = Tk()

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

# Almacenar URL del video + almacenar la ubicación donde se va a guardar el video
Link_Video = StringVar()
Ubicacion_Video_PC = StringVar()

# Para aumentar el progreso de la barra de progresion
percent = StringVar()
text = StringVar()


# Clase que se encarga de crear los Entrys
class CrearEntrys:
    def __init__(self, ventana, textvariable, fuente, tamañoDeFuente, ancho, y):
        """
        Esta función crea un widget de Entrada y lo posiciona en la ventana.
        @param ventana - La ventana donde se colocará la Entrada.
        @param textvariable - Esta es la variable que se utilizará para almacenar el texto que ingresa el usuario.
        @param fuente - La fuente que desea utilizar.
        @param tamañoDeFuente - El tamaño de fuente del texto en la Entrada.
        @param ancho - ancho de la entrada
        @param y - La posición del eje Y de la entrada.
        """
        self.ventana = ventana
        self.textvariable = textvariable
        self.fuente = fuente
        self.tamañoDeFuente = tamañoDeFuente
        self.ancho = ancho
        self.y = y

        # Crear el Entry
        self.crearEntry = Entry(
            self.ventana,
            textvariable=self.textvariable,
            font=(self.fuente, self.tamañoDeFuente),
            width=self.ancho,
        )

        # Posicionar el Entry
        self.crearEntry.pack(pady=self.y)


# Clase que cambia el color de los botones al pasar el ratón por encima
class CambiarColor:
    @staticmethod
    def FuncionCambiarColor(button, colorRatonDentro, colorRatonFuera):
        """
        Toma un botón y dos colores, y vincula el botón para cambiar de color cuando el mouse ingresa y deja el botón
        @param button - El botón al que desea cambiar el color.
        @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
        @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
        """
        button.bind(
            "<Enter>", func=lambda e: button.config(background=colorRatonDentro)
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


# Clase que crea los botones, los coloca en pantalla y los cambia de color al pasar el ratón por encima de ellos
class Botones:
    """
    Clase que crea los botones, los coloca en la ventana y los cambia de color al pasar el ratón por encima de ellos.
    """

    class BotonPosicionAbsoluta:
        def __init__(
            self,
            texto,
            y,
            ancho,
            colorFondo,
            funcion,
            fuente,
            tamañoFuente,
            ventana,
            colorRatonDentro,
            colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del 4
            botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            self.cambiarColor = CambiarColor()
            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            self.boton = Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.boton.pack(pady=self.y)

            self.cambiarColor.FuncionCambiarColor(
                self.boton, self.colorRatonDentro, self.colorRatonFuera
            )

    class BotonPosicionRelativa:
        def __init__(
            self,
            texto,
            x,
            y,
            ancho,
            colorFondo,
            funcion,
            fuente,
            tamañoFuente,
            ventana,
            colorRatonDentro,
            colorRatonFuera,
        ):
            """
            Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del
            botón
            cuando el mouse está sobre él.
            @param texto - El texto que se mostrará en el botón.
            @param x - La distancia entre el botón y el widget anterior.
            @param y - La distancia entre el botón y el widget anterior.
            @param ancho - ancho del botón
            @param colorFondo - color de fondo
            @param funcion - La función que se ejecutará cuando se presione el botón.
            @param fuente - La fuente del texto.
            @param tamañoFuente - El tamaño de la fuente.
            @param ventana - La ventana en la que estará el botón.
            @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
            @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
            """
            self.cambiarColor = CambiarColor()

            # Crea el botón con los parámetros dados
            self.texto = texto
            self.y = y
            self.ancho = ancho
            self.colorFondo = colorFondo
            self.fuente = fuente
            self.tamañoFuente = tamañoFuente
            self.ventana = ventana
            self.colorRatonDentro = colorRatonDentro
            self.colorRatonFuera = colorRatonFuera
            self.funcion = funcion

            self.boton = Button(
                self.ventana,
                text=self.texto,
                bg=self.colorFondo,
                font=(self.fuente, self.tamañoFuente),
                command=self.funcion,
                width=self.ancho,
            )

            self.boton.place(x=x, y=y)

            self.cambiarColor.FuncionCambiarColor(
                self.boton, self.colorRatonDentro, self.colorRatonFuera
            )


# Clase que crea los labels y los coloca en pantalla
class Etiqueta:
    def __init__(self, texto, y, ancho, colorFondo, fuente, tamañoFuente, ventana):
        """
        Crea una etiqueta con los parámetros dados y luego la coloca en la ventana.
        @param texto - El texto que se mostrará en la etiqueta.
        @param y - La posición del eje y de la etiqueta.
        @param ancho - El ancho de la etiqueta.
        @param colorFondo - El color de fondo de la etiqueta.
        @param fuente - La fuente a utilizar.
        @param tamañoFuente - Tamaño de la fuente.
        """
        # Crea una etiqueta con los parámetros dados
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana

        # Crear la etiqueta
        self.etiqueta = Label(
            self.ventana,
            text=self.texto,
            font=(self.fuente, self.tamañoFuente),
            width=self.ancho,
            bg=self.colorFondo,
        )
        # Colocar la etiqueta en la ventana
        self.etiqueta.pack(pady=self.y)


# Barra de progresión
class BarraDeProgresion:
    # Crear barra de progresion
    barraProgresionDescarga = Progressbar(Ventana, orient=HORIZONTAL, length=800)

    def __init__(self):
        self.speed = None
        self.download = None
        self.GB = None

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


# Clase que aumenta la barra de progreso en paralelo con la descarga
class AumentarBarraDeProgresionEnParalelo:
    def __init__(self):
        self.aumentarProgresoEnParalelo = None
        self.barraDeProgresion = None

    def FuncionAumentarBarraDeProgresionEnParalelo(self):
        """
        Creamos una instancia de la barra de progreso, luego creamos un hilo que llama a la función que aumenta la barra de
        progreso
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


# Clase principal del programa
class Main:
    def __init__(self):
        self.downloader = None
        self.Etiqueta_Barra_Progress = None
        self.Boton_Descargar_Audio = None
        self.Boton_Descargar_Video = None
        self.Boton_Buscar = None
        self.Ubicacion_Video = None
        self.Ubicacion = None
        self.URL_Video = None
        self.Etiqueta_URL = None
        self.cambiarColor = None
        self.aumentarBarraDeProgreso = None
        self.descargarAudio = None
        self.descargarVideo = None
        self.buscar = None
        self.barraDeProgresion = None
        self.boton = Botones()

    # noinspection PyArgumentList
    def FuncionMain(self):
        """
        Crea la GUI para el programa.
        """
        # Creamos una instancia de: BarraDeProgresion, Buscar, Descargar, AumentarBarraDeProgresionEnParalelo y CambiarColor
        self.barraDeProgresion = BarraDeProgresion()
        self.buscar = Buscar()
        self.downloader = Downloader()
        self.aumentarBarraDeProgreso = AumentarBarraDeProgresionEnParalelo()

        # Texto + Caja + Botón de descargar video
        self.Etiqueta_URL = Etiqueta(
            "Introduce la URL del video a descargar",
            10,
            30,
            azulEtiquetas,
            "Helvetica",
            18,
            Ventana,
        )

        self.URL_Video = CrearEntrys(Ventana, Link_Video, "Helvetica", 15, 70, 20)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicación para guardar el video
        self.Ubicacion = Etiqueta(
            "¿Donde quieres guardar el video?",
            35,
            27,
            azulEtiquetas,
            "Helvetica",
            18,
            Ventana,
        )

        self.Ubicacion_Video = CrearEntrys(
            Ventana, Ubicacion_Video_PC, "Helvetica", 15, 70, 20
        )

        self.Boton_Buscar = self.boton.BotonPosicionAbsoluta(
            "Seleccionar ubicación",
            0.0012,
            20,
            verdeOscuro,
            lambda: [self.buscar.FuncionBuscar()],
            "Helvetica",
            15,
            Ventana,
            verdeClaro,
            verdeOscuro,
        )

        self.Boton_Descargar_Video = self.boton.BotonPosicionRelativa(
            "Descargar video",
            220,
            348,
            15,
            amarilloOscuro,
            lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                self.downloader.DescargarVideo(),
            ],
            "Helvetica",
            15,
            Ventana,
            amarilloClaro,
            amarilloOscuro,
        )

        self.Boton_Descargar_Audio = self.boton.BotonPosicionRelativa(
            "Descargar audio",
            420,
            348,
            15,
            amarilloOscuro,
            lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                self.downloader.DescargarAudio(),
            ],
            "Helvetica",
            15,
            Ventana,
            amarilloClaro,
            amarilloOscuro,
        )

        # Crear la etiqueta de la barra de progresion
        self.Etiqueta_Barra_Progress = Etiqueta(
            "Progreso de la descarga:",
            77,
            20,
            azulEtiquetas,
            "Helvetica",
            18,
            Ventana,
        )

        # Ubicamos la barra de progresion
        self.barraDeProgresion.barraProgresionDescarga.place(x=13, y=470)

        # ---------------------------------------------------------------------------


# Clase que se encarga de preguntar al usuario donde quiere guardar el video
class Buscar:
    def __init__(self):
        self.Directorio_Descarga = None

    def FuncionBuscar(self):
        """
        Abre un cuadro de diálogo de archivo y establece el valor de la variable “Ubicacion_Video_PC” al directorio
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


# Clase que se encarga de descargar el video y/o el audio
class Downloader:
    class DescargarVideo:
        def __init__(self):
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

                self.Descargar_Video = (
                    self.Obtener_Video.streams.get_highest_resolution()
                )

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
        def __init__(self):
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

                os.rename(self.base + self.ext, self.cambiarFormato)

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

                log.info(
                    "La descarga del audio del video se ha completado correctamente"
                )


# -----------------------------------------

# Crear instancia de la clase que inicia el programa
interfaz = Main()

# Llamar a la función que inicia el programa
interfaz.FuncionMain()

# Actualizar ventana
Ventana.mainloop()
