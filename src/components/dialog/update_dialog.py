# Standard library
from typing import Callable

# Third-Party libraries
from flet import CrossAxisAlignment, Page

# Create widgets
from frontend.create_widgets import (
    CreateDialog,
    CreateElevatedButton,
    CreateOutlinedButton,
)

# Settings
from settings import ExcelTextLoader

# Utils
from utils import check_type


class UpdateDialog(CreateDialog):
    @check_type
    def __init__(self, app_page: Page, overlay: Callable, update: Callable):
        self.app_page = app_page
        self.overlay = overlay

        self.button_update = CreateElevatedButton(
            text_button=ExcelTextLoader.get_text(4), function=lambda e: update()
        )

        self.button_later = CreateOutlinedButton(
            text_button=ExcelTextLoader.get_text(19),
            function=lambda e: self.change_state(app_page),
        )

        self.button_ok = CreateElevatedButton(
            text_button="ok", function=lambda e: self.change_state(app_page)
        )

        super().__init__(
            title=ExcelTextLoader.get_text(17),
            title_size=23,
            content=ExcelTextLoader.get_text(18),
            content_size=23,
            actions=[self.button_update, self.button_later],
            actions_alignment=CrossAxisAlignment.END,
            overlay=self.overlay,
            app_page=self.app_page,
        )

    @check_type
    def show(self, is_new_release_available: bool, is_main: bool):
        if not is_new_release_available and not is_main:
            self.update_title(ExcelTextLoader.get_text(21))
            self.update_content(ExcelTextLoader.get_text(22))
            self.actions = [self.button_ok]

            return super().show()

        if is_new_release_available:
            return super().show()
