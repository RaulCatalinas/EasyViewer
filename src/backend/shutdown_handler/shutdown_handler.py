"""
Control the closing of the app
"""

# Third-Party libraries
from flet import MainAxisAlignment, Page

# Control variables
from control_variables import store_control_variables

# Create widgets
from components.widgets import (
    Dialog,
    ElevatedButton,
    OutlinedButton,
)

# Settings
from settings import ExcelTextLoader


class ShutdownHandler(Dialog):
    """
    Control the closing of the app
    """

    def __init__(self, page, overlay):
        self.button_exit_the_app = ElevatedButton(
            text_button=ExcelTextLoader.get_text(4),
            function=lambda e: self.__exit(page=page),
        )
        self.button_cancel_exit_the_app = OutlinedButton(
            text_button="No", function=lambda e: self.__cancel(page)
        )

        self.title_dialog = ExcelTextLoader.get_text(12)
        self.content_dialog = ExcelTextLoader.get_text(3)

        super().__init__(
            icon=False,
            title=self.title_dialog,
            title_size=25,
            content=self.content_dialog,
            content_size=25,
            actions=[self.button_exit_the_app, self.button_cancel_exit_the_app],
            actions_alignment=MainAxisAlignment.END,
            overlay=overlay,
            app_page=page,
        )

    def __exit(self, page: Page):
        """
        Exits the program and saves the location selected by the user

        Args:
            page (flet.Page): Reference to the app window
        """

        self.change_state(page)

        store_control_variables(page)

        page.window_destroy()

    def __cancel(self, page: Page):
        """
        Cancel the exit of the program

        Args:
            page (flet.Page): Reference to the app window
        """

        self.change_state(page)
