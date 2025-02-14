# Standard library
from typing import Callable

# Third party libraries
from flet import Page, WindowEvent


class WindowManager:
    """Clase encargada de manejar la configuración de la ventana."""

    def __init__(
        self, app: Page, events_handler: Callable[[WindowEvent], None]
    ):
        self.app = app
        self.events_handler = events_handler
        self._configure_window()

    def _configure_window(self):
        """Configura las propiedades de la ventana."""
        self.app.window.wait_until_ready_to_show = True
        self.app.window.center()
        self.app.window.resizable = False
        self.app.window.maximizable = False
        self.app.window.width = 830
        self.app.window.height = 575
        self.app.title = "EasyViewer"
        self.app.window.prevent_close = True
        self.app.window.on_event = self.events_handler
