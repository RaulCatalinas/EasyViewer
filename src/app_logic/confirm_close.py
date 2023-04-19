"""
Control the closing of the app
"""

from flet import MainAxisAlignment

from client.app_settings import AppSettings
from client.create_buttons import CreateElevatedButton, CreateOutlinedButton
from client.create_dialog import CreateDialog


class ConfirmClose(AppSettings, CreateDialog):
    """
    Control the closing of the app
    """

    def __init__(self, page, save_to_local_storage):
        AppSettings.__init__(self)

        self.button_exit_the_app = CreateElevatedButton(
            text_button=self.get_config_excel(4),
            function=lambda e: self.__exit(
                page=page, save_to_local_storage=save_to_local_storage
            ),
        )
        self.button_cancel_exit_the_app = CreateOutlinedButton(
            text_button="No", function=lambda e: self.__cancel(page)
        )

        self.title_dialog = self.get_config_excel(12)
        self.content_dialog = self.get_config_excel(3)

        CreateDialog.__init__(
            self,
            icon=False,
            title_dialog=self.title_dialog,
            title_size=25,
            content_dialog=self.content_dialog,
            content_size=19,
            actions_dialog=[self.button_exit_the_app, self.button_cancel_exit_the_app],
            actions_alignment_dialog=MainAxisAlignment.END,
        )

    def __exit(self, page, save_to_local_storage):
        """
        Exits the program and saves the location selected by the user to your local storage
        """

        self.change_state(page)

        save_to_local_storage(page)

        page.window_destroy()

    def __cancel(self, page):
        """
        Close the app exit confirmation dialog

        :param page: Is a reference to the app window
        """

        return self.change_state(page)
