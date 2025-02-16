# Standard Library
from typing import Callable

# Third-Party libraries
from flet import Page, Icons

# Components
from components.widgets.app_bars import AppBar
from components.widgets.buttons import IconButton
from components.widgets.checkboxes import UpdateCheckbox

# App settings
from app_settings import AppColors


class SettingsUIManager:
    def __init__(self, app: Page):
        app.appbar = AppBar(
            window_elements=[
                UpdateCheckbox(
                    lambda _: print("Check for updates automatically ")
                ),
                self._create_icon_button(
                    icon=Icons.LANGUAGE,
                    function=lambda _: print("Change Language"),
                ),
                self._create_icon_button(
                    icon=Icons.CONTACTS, function=lambda _: print("Contacting")
                ),
            ],
            height=50,
            bg_color=AppColors.APP_BAR_BG_COLOR_THEME_DARK.value,
        )

    def _create_icon_button(
        self,
        icon: Icons,
        function: Callable,
        offset_x: float = 0,
        offset_y: float = 0,
        scale: float = 1,
    ):
        """Creates an icon button with default values."""
        return IconButton(
            icon=icon,
            function=function,
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )
