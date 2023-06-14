"""
Control the closing of the app
"""

from flet import MainAxisAlignment

from config import ExcelTextLoader
from control import ControlVariables
from frontend import CreateElevatedButton, CreateOutlinedButton, CreateDialog


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
            content_size=19,
            actions=[self.button_exit_the_app, self.button_cancel_exit_the_app],
            actions_alignment=MainAxisAlignment.END,
        )

    def __exit(self, page):
        """
        Exits the program and saves the location selected by the user to your local storage

        :param page: Is a reference to the app window
        :return: None
        """

        self.change_state(page)

        ControlVariables().save_to_local_storage(page)

        page.window_destroy()

    def __cancel(self, page):
        """
        Close the app shutdown_handler confirmation dialog

        :param page: Is a reference to the app window
        :return: None
        """

        return self.change_state(page)
