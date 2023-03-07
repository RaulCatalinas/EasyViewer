# Instalacion de poetry

## Globalmente

1. Descargar e instalar poetry:

   * Si estas en un sistema tipo Unix o WSL ejecuta como administardor este comando en una terminal: <p>curl -sSL https://install.python-poetry.org | python3 - </p>
   * Si estas en windows usa este otro comando ejecutandolo como administardor en una terminal de "Poweshell": <p>(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - </p>
2. Agrega la ruta de instalacion de "poetry" a tu variable de entorno "PATH"
3. Tras ejecutar el comando que obtiene e instala poetry y agregarlo al "PATH" ejecuta este comando en una terminal (no es necesario que lo ejeutes como administrador): <p>poetry --version<p> Si te sale la version de poetry esta instalado correctamente.

   ## Localmente


   1. Crear un entorno virtual
   2. Activar el entorno virtual
   3. Ejecutar en una terminal este comando: pip install poetry

      ## Instalacion de las dependencias

      Ejecuta poetry install (teniendo el entorno virtual activado), cuando termine de ejecutarse ya tienes instalas las dependencias del programa.

# Mas informacion de poetry

https://python-poetry.org

# Descripcion del poyecto

App para descargar videos y/o el audio de los videos de YouTube.

El usuario introduce la URL del video que quiere descargar y selecciona la ubicación donde quiere guardar el video y/o
el audio, en caso de que el usuario no seleccione una ubicacion, se establece su escritorio como ubicacion por defecto.

El usuario tiene 2 dos botones para escoger:

1. Descargar video: Este botón descargará el video obtenido de la URL proporcionada por el usuario, una vez que este
   descargado lo guardara en la carpeta seleccionada por el usuario

2. Descargar audio: Este botón descargará el audio del video obtenido de la URL proporcionada por el usuario, una vez que
   este descargado le cambiara el formato a .mp3 y por último se guardara en la carpeta
   seleccionada por el usuario

Mientras se está descargando el video y/o el audio aumentara una barra de progresión conforme vaya avanzando
la descarga

# Redes sociales

<a href="https://www.instagram.com/raulf1foreveryt_oficial/?hl=es">Instagram</a>
<a href="https://twitter.com/F1foreverRaul">Twitter</a>
<a href="https://www.facebook.com/Raul-F1forever-114186780454598/">Facebook</a>
