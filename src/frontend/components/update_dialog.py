from typing import Callable

from flet import CrossAxisAlignment, Page

from settings import ExcelTextLoader
from utils import check_type

from ..create_widgets import CreateDialog, CreateElevatedButton, CreateOutlinedButton


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

        super().__init__(
            title=ExcelTextLoader.get_text(17),
            title_size=23,
            content=ExcelTextLoader.get_text(18),
            content_size=23,
            actions=[self.button_update, self.button_later],
            actions_alignment=CrossAxisAlignment.END,
        )

    def show_update_dialog(self):
        """
        Shows the update dialog
        """

        self.overlay(self.app_page)

        self.app_page.dialog = self

        self.change_state(self.app_page)
