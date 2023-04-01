"""Control the closing of the app"""

from flet import AlertDialog, MainAxisAlignment

from client.app_settings import AppSettings
from client.create_buttons import CreateElevatedButton, CreateOutlinedButton
from client.create_text import CreateText
from control_variables import ControlVariables
from interact_api_pytube import cancel_download
from client.create_dialog import CreateDialog


class ConfirmClose(AppSettings):
    """Control the closing of the app"""

    def __init__(self, page):
        AppSettings.__init__(self)

        self.control_variables = ControlVariables()

        self.button_exit_the_app = CreateElevatedButton(
            text_button=self.get_config_excel(4),
            function=lambda e: self.__exit(page),
        )

        self.button_cancel_exit_the_app = CreateOutlinedButton(
            text_button="No", function=lambda e: self.__cancel(page)
        )

        self.title_dialog = self.get_config_excel(12)
        self.content_dialog = self.get_config_excel(3)

        self.exit_dialog = CreateDialog(
            icon=False,
            title_dialog=self.title_dialog,
            title_size=25,
            content_dialog=self.content_dialog,
            content_size=19,
            actions_dialog=[self.button_exit_the_app, self.button_cancel_exit_the_app],
            actions_alignment_dialog=MainAxisAlignment.END,
        )

    def __exit(self, page):
        try:
            if not self.control_variables.get_control_variables(
                "DOWNLOADED_SUCCESSFULLY"
            ):
                cancel_download()

        finally:
            self.exit_dialog.change_state_dialog(page)
            page.window_destroy()

    def __cancel(self, page):
        return self.exit_dialog.change_state_dialog(page)

    def show_close_dialog(self, page):
        return self.exit_dialog.change_state_dialog(page)

    def update_text_dialog(self, text_title, text_content):
        return (
            self.exit_dialog.update_text(
                text_title=text_title, text_content=text_content
            ),
            self.button_exit_the_app.change_text_button(self.get_config_excel(4)),
        )
