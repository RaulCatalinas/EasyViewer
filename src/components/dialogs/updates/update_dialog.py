# Standard library
from typing import Callable

# Third-Party libraries
from flet import MainAxisAlignment, Page

# Widgets
from widgets.buttons import ElevatedButton, OutlinedButton

# Settings
from settings import ExcelTextLoader

# Control variables
from control_variables import WhatsNewRead

# Base
from .._base import BaseDialog


class UpdateDialog(BaseDialog):
    def __init__(self, app: Page, update_function: Callable):
        self.whats_new_read = WhatsNewRead()

        self.button_update = ElevatedButton(
            text=ExcelTextLoader.get_text(4),
            function=lambda e: update_function(),
        )

        self.button_later = OutlinedButton(
            text=ExcelTextLoader.get_text(19),
            function=lambda e: self.close_dialog(),
        )

        self.button_ok = ElevatedButton(
            text="ok", function=lambda e: self.close_dialog()
        )

        super().__init__(
            title=ExcelTextLoader.get_text(17),
            title_size=23,
            content=ExcelTextLoader.get_text(18),
            content_size=23,
            actions=[self.button_update, self.button_later],
            actions_alignment=MainAxisAlignment.END,
            app=app,
        )

    def show(self, is_new_release_available: bool, is_main: bool):
        if not is_new_release_available and not is_main:
            self.update_title(ExcelTextLoader.get_text(21))
            self.update_content(ExcelTextLoader.get_text(22))
            self.actions = [self.button_ok]

            return super().show_dialog()

        if is_new_release_available:
            self.whats_new_read.set(False)

            return super().show_dialog()
