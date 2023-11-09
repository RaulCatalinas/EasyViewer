# Create widgets
from ..widgets import Dialog, ElevatedButton

# Utils
from utils import check_type

# Standard library
from typing import Callable

# Third-Party libraries
from flet import CrossAxisAlignment, Page

# Constants
from constants import WHATS_NEW_FILES

# Settings
from settings import EnvironmentVariables, ExcelTextLoader

# Control variables
from control_variables import WhatsNewRead


class WhatsNewDialog(Dialog):
    @check_type
    def __init__(self, app_page: Page, overlay: Callable):
        self.whats_new_read = WhatsNewRead()

        self.overlay = overlay
        self.app_page = app_page

        self.button_close_dialog = ElevatedButton(
            text_button="Ok", function=lambda e: self.change_state(app_page)
        )

        super().__init__(
            title=ExcelTextLoader.get_text(30),
            title_size=18,
            content=self.__get_content(),
            content_size=16,
            actions=[self.button_close_dialog],
            actions_alignment=CrossAxisAlignment.END,
            overlay=self.overlay,
            app_page=self.app_page,
        )

    def __get_content(self) -> str:
        app_language = EnvironmentVariables.get_language()

        if app_language is None:
            return ""

        whats_new_file = WHATS_NEW_FILES[app_language]

        with open(whats_new_file, mode="r", encoding="utf-8") as f:
            return f.read()

    def show(self):
        whats_new_read = self.whats_new_read.get()

        if not whats_new_read:
            self.whats_new_read.set(True)

            return super().show()
