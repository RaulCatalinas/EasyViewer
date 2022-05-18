# Descargador de videos de youtube en mp4

import logging
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

import pytube

# -----------------------------------------------

# Bloque de colores
Cian = "#00FFEF"
Verde_Claro = "#00FF66"
Negro = "#000000"

# ------------------------------------------------

# Configurar el logging
logging.basicConfig(filename="YoutubeDownloader.log", filemode="w", level=logging.DEBUG)

# Obtener tener la Fecha de cuando se ejecuta el script
fecha = datetime.today()
formato = fecha.strftime("%A, %d %B, %Y %H:%M")

logging.info(
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


# Barra de progresion
class BarraDeProgresion:
    Instancia_Barra_De_Progresion = Progressbar(Ventana, orient=HORIZONTAL, length=800)


def Crear_Elementos_De_La_Interfaz():
    # Texto + Caja + Boton de descargar video
    Etiqueta_URL = tkinter.Label(
        Ventana,
        text="Introduce la URL del video a descargar",
        font="Helvetica 15",
        bg=Cian,
    )

    Etiqueta_URL.pack(pady=10)

    URL_Video = tkinter.Entry(
        Ventana, textvariable=Link_Video, font="Helvetica 15", width=70
    )

    URL_Video.pack(pady=20)

    # ---------------------------------------------------------------------------

    # Texto + Caja + Boton de ubicacion para guardar el video
    Ubicacion = tkinter.Label(
        Ventana, text="Donde quieres guardar el video", font="Helvetica 15", bg=Cian
    )

    Ubicacion.pack(pady=35)

    Ubicacion_Video = tkinter.Entry(
        Ventana, width=70, textvariable=Ubicacion_Video_PC, font="Helvetica 15"
    )

    Ubicacion_Video.pack(pady=5)

    Boton_Exploracion = tkinter.Button(
        Ventana,
        text="Seleccionar ubicación",
        command=Buscar,
        font="Helvetica 15",
        bg=Verde_Claro,
    )

    Boton_Exploracion.pack(pady=20)

    Boton_Descargar = tkinter.Button(
        Ventana,
        text="Descargar",
        command=Descargar,
        font="Helvetica 15",
        bg=Verde_Claro,
    )

    Boton_Descargar.pack(pady=20)

    # Creamos una instancia de la barra de progresion
    MostrarBarra = BarraDeProgresion()

    # Crear la etiqueta de la barra de progresion
    Etiqueta_Barra_Progress = tkinter.Label(
        Ventana, text="Progreso de la descarga", font="Helvetica 15", bg=Cian
    )

    # Poner etiqueta en pantalla
    Etiqueta_Barra_Progress.pack(pady=20)

    # Ubicamos la barra de progresion
    MostrarBarra.Instancia_Barra_De_Progresion.pack(pady=5)

    # ---------------------------------------------------------------------------


def Buscar():
    logging.info(
        "Se ha hecho click en el boton de seleccionar la direccion de la carpeta donde se quiere guardar el video descargado"
    )

    Directorio_Descarga = filedialog.askdirectory(initialdir="Directorio seleccionado")
    Ubicacion_Video_PC.set(Directorio_Descarga)


def Descargar():
    logging.info("Se ha hecho click en el boton de descargar")

    try:

        URL = Link_Video.get()

        logging.info("Se ha obtenido la URL del video a descargar")

        Carpeta_Guardar_Video = Ubicacion_Video_PC.get()

        logging.info(
            "Se ha obtenido la direccion de la carpeta donde se quiere guardar el video descargado"
        )

        Obtener_Video = pytube.YouTube(URL)

        logging.info("Se ha obtenido el ID del video a descargar")

        Descargar_Video = Obtener_Video.streams.get_highest_resolution()

        logging.info("Se ha obtenido la resolucion mas alta del video a descargar")

        Descargar_Video.download(Carpeta_Guardar_Video)

    except:

        messagebox.showerror(
            "Error de descarga", "No se ha conseguido descargar el video"
        )

        logging.info("El video no se ha podido descargar, algo ha salido mal")

    else:

        messagebox.showinfo(
            "Completado", "Puedes encontar tu video en:\n" + Carpeta_Guardar_Video
        )

        logging.info("La descarga se ha completado correctamente")


# -----------------------------------------

# Llamar al la funcion que inicia el programa
Crear_Elementos_De_La_Interfaz()

# Actualizar ventana
Ventana.mainloop()
