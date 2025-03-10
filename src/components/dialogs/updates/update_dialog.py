# Standard library
from typing import Callable

# Third-Party libraries
from flet import MainAxisAlignment, Page

# Widgets
from ...widgets.buttons import ElevatedButton, OutlinedButton

# Base
from .._base import BaseDialog

# App enums
from app_enums import ExcelTextLoaderKeys

# i18n
from i18n import ExcelTextLoader


class UpdateDialog(BaseDialog):
    def __init__(self, app: Page, update_function: Callable):
        self.update_function = update_function
        self.excel_text_loader = ExcelTextLoader()

        self.button_update = ElevatedButton(
            app=app,
            text=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.YES_OPTION
            ),
            function=lambda _: self.update_function(),
        )

        self.button_later = OutlinedButton(
            app=app,
            text=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.LATER_OPTION
            ),
            function=lambda _: self.close_dialog(),
        )

        self.button_ok = ElevatedButton(
            app=app, text="Ok", function=lambda _: self.close_dialog()
        )

        super().__init__(
            title=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.UPDATE_AVAILABLE_TITLE
            ),
            title_size=23,
            content=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.UPDATE_AVAILABLE_BODY
            ),
            content_size=23,
            actions=[self.button_update, self.button_later],
            actions_alignment=MainAxisAlignment.END,
            app=app,
        )

    def show_dialog(self, an_update_is_available: bool):
        if not an_update_is_available:
            self.update_title(
                self.excel_text_loader.get_text(
                    ExcelTextLoaderKeys.UPDATED_VERSION_TITLE
                )
            )
            self.update_content(
                self.excel_text_loader.get_text(
                    ExcelTextLoaderKeys.UPDATED_VERSION_BODY
                )
            )

            self.actions = [self.button_ok]

            return super().show_dialog()

        return super().show_dialog()
