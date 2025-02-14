# Standard library
from typing import Callable

# Third party libraries
from flet import Icons, Page

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar


class MainUIManager:
    """Clase encargada de crear y organizar los elementos de la UI."""

    def __init__(self, app: Page):
        self.app = app
        self._initialize_ui()

    def _initialize_ui(self):
        """Inicializa los elementos de la UI y los agrega a la app."""
        self.app.add(
            self._create_icon_button(
                Icons.SETTINGS, lambda e: print("Settings")
            ),
            self._create_input(
                placeholder="Video URL",
                text_size=20,
                autofocus=True,
                is_multiline=True,
                max_height=2,
            ),
            self._create_input(
                placeholder="Directory",
                text_size=20,
                read_only=True,
                offset_y=0.5,
            ),
            self._create_icon_button(
                icon=Icons.FOLDER,
                function=lambda e: print("Selecting directory"),
                offset_x=9.42,
                offset_y=1.5,
                scale=2.5,
            ),
            self._create_icon_button(
                icon=Icons.AUDIO_FILE,
                function=lambda e: print("Downloading audio"),
                offset_x=8.4,
                offset_y=2.5,
                scale=2.5,
            ),
            self._create_icon_button(
                icon=Icons.VIDEO_FILE,
                function=lambda e: print("Downloading video"),
                offset_x=10.45,
                offset_y=1.3,
                scale=2.5,
            ),
            ProgressBar(color="", offset_y=25, app=self.app),
        )

    def _create_icon_button(
        self,
        icon: Icons,
        function: Callable,
        offset_x: float = 0,
        offset_y: float = 0,
        scale: float = 1,
    ):
        """Crea un botón de ícono con valores predeterminados."""
        return IconButton(
            icon=icon,
            function=function,
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    def _create_input(self, placeholder, **kwargs):
        """Crea un campo de entrada con valores predeterminados."""

        return Input(placeholder=placeholder, **kwargs)
