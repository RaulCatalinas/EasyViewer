# Standard Library

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
                IconButton(
                    icon=Icons.LANGUAGE,
                    function=lambda _: print("Change Language"),
                ),
                IconButton(
                    icon=Icons.CONTACTS, function=lambda _: print("Contacting")
                ),
            ],
            height=50,
            bg_color=AppColors.APP_BAR_BG_COLOR_THEME_DARK.value,
        )
