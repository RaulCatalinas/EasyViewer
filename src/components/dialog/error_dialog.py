# Standard library
from typing import Callable

# Third-Party libraries
from flet import CrossAxisAlignment, Page, icons

# Create widgets
from ..widgets import Dialog, ElevatedButton

# Utils
from utils import check_type


class ErrorDialog(Dialog):
    @check_type
    def __init__(self, app_page: Page, overlay: Callable):
        self.app_page = app_page
        self.overlay = overlay

        self.button_close_dialog = ElevatedButton(
            text_button="Ok", function=lambda e: self.change_state(app_page)
        )

        super().__init__(
            icon=True,
            title=icons.ERROR,
            title_size=1.3,
            content="",
            content_size=23,
            actions=[self.button_close_dialog],
            actions_alignment=CrossAxisAlignment.END,
            overlay=self.overlay,
            app_page=self.app_page,
        )

    @check_type
    def show(self, error: str):
        self.update_content(error)

        return super().show()
