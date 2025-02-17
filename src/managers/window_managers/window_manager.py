# Standard library
from typing import Callable

# Third party libraries
from flet import Page, WindowEvent

# App settings
from app_settings import WindowSettings

# User preferences
from user_preferences import ThemeManager


class WindowManager:
    """Class in charge of managing the window configuration."""

    def __init__(
        self, app: Page, events_handler: Callable[[WindowEvent], None]
    ):
        self.app = app
        self.events_handler = events_handler
        self.theme_manager = ThemeManager(self.app)
        self._configure_window()

    def _configure_window(self):
        """Set up the app window."""

        self.app.window.wait_until_ready_to_show = True
        self.app.window.center()
        self.app.window.resizable = WindowSettings.RESIZABLE.value
        self.app.window.maximizable = WindowSettings.MAXIMIZABLE.value
        self.app.window.width = WindowSettings.WIDTH.value
        self.app.window.height = WindowSettings.HIGH.value
        self.app.title = WindowSettings.TITLE.value
        self.app.window.prevent_close = WindowSettings.PREVENT_CLOSE.value
        self.app.window.on_event = self.events_handler

        self.theme_manager.set_initial_theme()
