# Third-Party libraries
from flet import Page, Icons

# Components
from components.widgets.app_bars import AppBar
from components.widgets.buttons import IconButton
from components.widgets.checkboxes import UpdateCheckbox

# User preferences
from user_preferences import ThemeManager, UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys

# Update manager
from update import UpdateManager


class SettingsUIManager:
    def __init__(self, app: Page, update_manager: UpdateManager):
        user_preferences_manager = UserPreferencesManager()
        theme_manager = ThemeManager(app)

        automatic_notifications = user_preferences_manager.get_preference(
            UserPreferencesKeys.AUTOMATIC_NOTIFICATIONS
        )

        self.button_icon_theme = IconButton(
            icon=theme_manager.get_icon_theme(),
            function=lambda _: theme_manager.toggle_theme_mode(),
        )

        self.button_icon_check_updates = IconButton(
            icon=Icons.UPDATE,
            function=lambda: update_manager.check_updates(True),
            visible=not automatic_notifications,
        )

        self.app_bar = AppBar(
            window_elements=[
                UpdateCheckbox(
                    lambda: self.button_icon_check_updates.toggle_visible(app)
                ),
                IconButton(
                    icon=Icons.LANGUAGE,
                    function=lambda _: print("Change Language"),
                ),
                IconButton(
                    icon=Icons.CONTACTS, function=lambda _: print("Contacting")
                ),
                self.button_icon_theme,
                self.button_icon_check_updates,
            ],
            height=50,
            bg_color=theme_manager.get_app_bar_theme(),
        )

        theme_manager.app_bar_reference = self.app_bar
        theme_manager.button_icon_theme_reference = self.button_icon_theme

        app.appbar = self.app_bar
