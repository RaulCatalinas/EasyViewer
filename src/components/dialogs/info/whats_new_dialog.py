# Third-Party libraries
from flet import Page

# Widgets
from ...widgets.buttons import ElevatedButton

# Base
from .._base import BaseDialog

# User preferences
from user_preferences import UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys


class WhatsNewDialog(BaseDialog):
    def __init__(self, app: Page):
        self.user_preferences_manager = UserPreferencesManager()

        self.button_ok = ElevatedButton(
            app=app, text="Ok", function=lambda _: self.close_dialog()
        )

        super().__init__(
            title="What's new",
            content="Change this with the changes made in this version",
            title_size=23,
            content_size=23,
            actions=[self.button_ok],
            app=app,
            is_modal=True,
        )

    def _mark_as_shown(self):
        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.WHATS_NEW_SHOWN, True
        )

    def show_dialog_if_necessary(self):
        whats_new_shown: bool = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.WHATS_NEW_SHOWN
        )

        if not whats_new_shown:
            self._mark_as_shown()

            super().show_dialog()
