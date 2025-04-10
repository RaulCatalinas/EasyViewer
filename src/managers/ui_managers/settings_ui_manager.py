# Third-Party libraries
from flet import Page, Icons

# Components
from components.widgets.app_bars import AppBar
from components.widgets.buttons import IconButton
from components.widgets.checkboxes import UpdateCheckbox
from components.widgets.dropdowns import DropdownLanguage

# User preferences
from user_preferences import ThemeManager, UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys, ExcelTextLoaderKeys

# Update manager
from update import UpdateManager

# i18n
from i18n import ExcelTextLoader


class SettingsUIManager:
    def __init__(self, app: Page, update_manager: UpdateManager):
        user_preferences_manager = UserPreferencesManager()
        excel_text_loader = ExcelTextLoader()
        theme_manager = ThemeManager(app)

        automatic_notifications = user_preferences_manager.get_preference(
            UserPreferencesKeys.AUTOMATIC_NOTIFICATIONS
        )

        self.button_icon_theme = IconButton(
            app=app,
            icon=theme_manager.get_icon_theme(),
            function=lambda _: theme_manager.toggle_theme_mode(),
        )

        self.button_icon_check_updates = IconButton(
            app=app,
            icon=Icons.UPDATE,
            function=lambda _: update_manager.check_updates(True),
            visible=not automatic_notifications,
        )

        self.dropdown_language = DropdownLanguage(app)

        self.app_bar = AppBar(
            window_elements=[
                UpdateCheckbox(
                    lambda: self.button_icon_check_updates.toggle_visible()
                ),
                self.dropdown_language,
                IconButton(
                    app=app,
                    icon=Icons.LANGUAGE,
                    function=lambda _: self.dropdown_language.toggle_visibility(),
                    tooltip_text=excel_text_loader.get_text(
                        ExcelTextLoaderKeys.CHANGE_LANGUAGE
                    ),
                ),
                IconButton(
                    app=app,
                    icon=Icons.CONTACTS,
                    function=lambda _: print("Contacting"),
                    tooltip_text=excel_text_loader.get_text(
                        ExcelTextLoaderKeys.CONTACT
                    ),
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
