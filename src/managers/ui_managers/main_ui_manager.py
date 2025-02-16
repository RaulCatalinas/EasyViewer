# Standard library
from typing import Callable, Optional

# Third party libraries
from flet import Icons, Page, Alignment

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar

# Managers
from managers.ui_managers.settings_ui_manager import SettingsUIManager

# App settings
from app_settings import AppColors


class MainUIManager:
    def __init__(self, app: Page):
        self.app = app
        self._initialize_ui()

    def _initialize_ui(self):
        """Initialises the UI elements and adds them to the app."""
        SettingsUIManager(self.app)
        self.app.add(
            self._create_input(
                placeholder="Video URL",
                text_size=20,
                autofocus=True,
                is_multiline=True,
                max_height=2,
                offset_y=0.5,
            ),
            self._create_input(
                placeholder="Directory",
                text_size=20,
                read_only=True,
                offset_y=1,
            ),
            self._create_icon_button(
                icon=Icons.FOLDER,
                function=lambda _: print("Selecting directory"),
                offset_x=9.42,
                offset_y=2.02,
                scale=2.5,
            ),
            self._create_icon_button(
                icon=Icons.AUDIO_FILE,
                function=lambda _: print("Downloading audio"),
                offset_x=8.4,
                offset_y=2.79,
                scale=2.5,
            ),
            self._create_icon_button(
                icon=Icons.VIDEO_FILE,
                function=lambda _: print("Downloading video"),
                offset_x=10.45,
                offset_y=1.56,
                scale=2.5,
            ),
            ProgressBar(
                color=AppColors.PROGRESS_BAR_COLOR.value,
                offset_y=25,
                app=self.app,
            ),
        )

    def _create_icon_button(
        self,
        icon: Icons,
        function: Callable,
        offset_x: float = 0,
        offset_y: float = 0,
        scale: float = 1,
        alignment: Optional[Alignment] = None,
    ):
        """Creates an icon button with default values."""
        return IconButton(
            icon=icon,
            function=function,
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
            alignment=alignment,
        )

    def _create_input(self, placeholder, **kwargs):
        """Crea un campo de entrada con valores predeterminados."""

        return Input(placeholder=placeholder, **kwargs)
