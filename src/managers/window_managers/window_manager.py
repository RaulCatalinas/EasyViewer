# Standard library
from typing import Callable

# Third party libraries
from flet import Page, WindowEvent

# App settings
from app_settings import AppSettings


class WindowManager:
    """Class in charge of managing the window configuration."""

    def __init__(
        self, app: Page, events_handler: Callable[[WindowEvent], None]
    ):
        self.app = app
        self.events_handler = events_handler
        self._configure_window()

    def _configure_window(self):
        """Set up the app window."""
        self.app.window.wait_until_ready_to_show = True
        self.app.window.center()
        self.app.window.resizable = AppSettings.RESIZABLE.value
        self.app.window.maximizable = AppSettings.MAXIMIZABLE.value
        self.app.window.width = AppSettings.WIDTH.value
        self.app.window.height = AppSettings.HIGH.value
        self.app.title = AppSettings.TITLE.value
        self.app.window.prevent_close = AppSettings.PREVENT_CLOSE.value
        self.app.window.on_event = self.events_handler
