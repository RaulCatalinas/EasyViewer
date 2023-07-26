"""
Control the closing of the app
"""

from flet import MainAxisAlignment, Page

from control_variables import ControlVariables
from frontend import CreateDialog, CreateElevatedButton, CreateOutlinedButton
from settings import ExcelTextLoader


class ShutdownHandler(CreateDialog):
    """
    Control the closing of the app
    """

    def __init__(self, page):
        self.button_exit_the_app = CreateElevatedButton(
            text_button=ExcelTextLoader.get_text(4),
            function=lambda e: self.__exit(page=page),
        )
        self.button_cancel_exit_the_app = CreateOutlinedButton(
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
        )

    def __exit(self, page: Page):
        """
        Exits the program and saves the location selected by the user

        Args:
            page (flet.Page): Reference to the app window
        """

        self.change_state(page)

        ControlVariables().save_to_local_storage(page)

        page.window_destroy()

    def __cancel(self, page: Page):
        """
        Cancel the exit of the program

        Args:
            page (flet.Page): Reference to the app window
        """

        self.change_state(page)
