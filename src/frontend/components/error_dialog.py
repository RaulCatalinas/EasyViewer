from typing import Callable

from flet import icons, CrossAxisAlignment, Page

from create_widgets import CreateDialog, CreateElevatedButton
from utils import check_type


class ErrorDialog(CreateDialog):
    @check_type
    def __init__(self, app_page: Page, overlay: Callable):
        self.app_page = app_page
        self.overlay = overlay

        self.button_close_dialog = CreateElevatedButton(
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
        )

    @check_type
    def show_error_dialog(self, error: str):
        """
        Show a dialog with the specified error.

        :param error: Error message
        :param app_page: Reference to the app window
        """

        self.overlay(self.app_page)

        self.update_content(error)

        self.app_page.dialog = self

        self.change_state(self.app_page)
