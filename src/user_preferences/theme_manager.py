# Standard library
from typing import Optional

# App enums
from app_enums import UserPreferencesKeys

# User preferences
from .user_preferences_manager import UserPreferencesManager

# Third-Party libraries
from flet import Page, ThemeMode, Icons

# App settings
from app_settings import AppColors

# Components
from components.widgets.buttons import IconButton
from components.widgets.app_bars import AppBar


class ThemeManager:
    """Manages the application theme settings, including light/dark mode and theme persistence."""

    def __init__(
        self,
        app: Page,
        button_icon_theme_reference: Optional[IconButton] = None,
        app_bar_reference: Optional[AppBar] = None,
    ):
        """
        Initializes the ThemeManager.

        Args:
            app (Page): The main application page where the theme settings will be applied.
        """
        self.app = app
        self.button_icon_theme_reference = button_icon_theme_reference
        self.app_bar_reference = app_bar_reference

        self.user_preferences_manager = UserPreferencesManager()

    def set_initial_theme(self):
        """
        Sets the initial theme of the app (light mode/dark mode) based on user preferences.
        """
        self.app.theme_mode = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.THEME
        )

    def toggle_theme_mode(self):
        """
        Toggles the theme mode of the app and updates the user preferences.
        """

        if (
            self.button_icon_theme_reference is None
            or self.app_bar_reference is None
        ):
            return

        self.app.theme_mode = (
            ThemeMode.DARK
            if self.app.theme_mode == ThemeMode.LIGHT
            else ThemeMode.LIGHT
        )

        self.button_icon_theme_reference.change_icon(self.get_icon_theme())
        self.app_bar_reference.change_bg_color(self.get_app_bar_theme())

        self.app.update()

        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.THEME, self.app.theme_mode.value
        )

    def get_icon_theme(self):
        """
        Returns the appropriate theme icon based on the current theme mode.

        Returns:
            str: The icon representing the opposite theme mode (light mode icon if in dark mode and vice versa).
        """

        return (
            Icons.DARK_MODE
            if self.app.theme_mode == ThemeMode.LIGHT.value
            else Icons.LIGHT_MODE
        )

    def get_app_bar_theme(self):
        """Returns the appropriate color for the taskbar based on the current theme mode."""

        return (
            AppColors.APP_BAR_BG_COLOR_THEME_DARK.value
            if self.app.theme_mode == ThemeMode.DARK.value
            else AppColors.APP_BAR_BG_COLOR_THEME_LIGHT.value
        )
