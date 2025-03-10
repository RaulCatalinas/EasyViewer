# Third-Party libraries
from flet import dropdown, Page

# Base
from ._base import DropdownBase

# Widgets
from ..texts import Text

# App enums
from app_enums import ExcelTextLoaderKeys, UserPreferencesKeys

# i18n
from i18n import ExcelTextLoader

# User preferences
from user_preferences import UserPreferencesManager


class DropdownLanguage(DropdownBase):
    def __init__(self, app: Page):
        self.excel_text_loader = ExcelTextLoader()
        self.user_preferences_manager = UserPreferencesManager()

        super().__init__(
            app=app,
            visible=False,
            on_change=lambda _: self._change_language(),
            placeholder=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.CHANGE_LANGUAGE
            ),
            options=[
                dropdown.Option(
                    text=self.excel_text_loader.get_text(
                        ExcelTextLoaderKeys.ENGLISH_LANGUAGE
                    ),
                    content=Text(
                        text=self.excel_text_loader.get_text(
                            ExcelTextLoaderKeys.ENGLISH_LANGUAGE
                        ),
                        text_size=12,
                    ),
                    key="English",
                ),
                dropdown.Option(
                    text=self.excel_text_loader.get_text(
                        ExcelTextLoaderKeys.SPANISH_LANGUAGE
                    ),
                    content=Text(
                        text=self.excel_text_loader.get_text(
                            ExcelTextLoaderKeys.SPANISH_LANGUAGE
                        ),
                        text_size=12,
                    ),
                    key="Spanish",
                ),
            ],
        )

    def _change_language(self):
        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.LANGUAGE, self.value
        )

        self.toggle_visibility()
