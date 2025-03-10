# Widgets
from ...widgets.buttons import ElevatedButton

# Third-Party libraries
from flet import MainAxisAlignment, Page

# User preferences
from user_preferences import UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys, ExcelTextLoaderKeys

# Base
from .._base import BaseDialog

# i18n
from i18n import ExcelTextLoader


class DisclaimerDialog(BaseDialog):
    def __init__(self, app: Page):
        self.user_preferences_manager = UserPreferencesManager()
        self.excel_text_loader = ExcelTextLoader()

        self.button_close_dialog = ElevatedButton(
            app=app, text="Ok", function=lambda _: self.close_dialog()
        )

        super().__init__(
            title=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.LIABILITY_NOTICE_TITLE
            ),
            title_size=18,
            content=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.LIABILITY_NOTICE_BODY
            ),
            content_size=16,
            actions=[self.button_close_dialog],
            actions_alignment=MainAxisAlignment.END,
            app=app,
            is_modal=True,
        )

    def _mark_as_shown(self):
        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.DISCLAIMER_SHOWN, True
        )

    def show_dialog_if_necessary(self):
        disclaimer_shown: bool = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.DISCLAIMER_SHOWN
        )

        if not disclaimer_shown:
            self._mark_as_shown()

            super().show_dialog()
