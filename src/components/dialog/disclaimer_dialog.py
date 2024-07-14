# Create widgets
from ..widgets import Dialog, ElevatedButton

# Utils
from utils import check_type

# Standard library
from typing import Callable

# Third-Party libraries
from flet import CrossAxisAlignment, Page

# Constants

# Settings
from settings import ExcelTextLoader

# Control variables
from control_variables import DisclaimerDialogControlVariable


class DisclaimerDialog(Dialog):
    @check_type
    def __init__(self, app_page: Page, overlay: Callable):
        self.disclaimer_dialog = DisclaimerDialogControlVariable()

        self.overlay = overlay
        self.app_page = app_page

        self.button_close_dialog = ElevatedButton(
            text_button="Ok", function=lambda e: self.change_state(app_page)
        )

        super().__init__(
            title=ExcelTextLoader.get_text(31),
            title_size=18,
            content=ExcelTextLoader.get_text(32),
            content_size=16,
            actions=[self.button_close_dialog],
            actions_alignment=CrossAxisAlignment.END,
            overlay=self.overlay,
            app_page=self.app_page,
        )

    def show(self):
        disclaimer_dialog = self.disclaimer_dialog.get()

        if not disclaimer_dialog:
            self.disclaimer_dialog.set(True)

            return super().show()
