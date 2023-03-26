"""Control the closing of the app"""

from flet import AlertDialog, MainAxisAlignment

from app_settings import AppSettings
from client.create_buttons import CreateElevatedButton, CreateOutlinedButton
from client.create_text import CreateText


class ConfirmClose(AppSettings, AlertDialog):
    """Control the closing of the app"""

    def __init__(self, page):
        self.page = page

        AppSettings.__init__(self)

        self.button_exit_the_app = CreateElevatedButton(
            text_button=self.get_config_excel(4),
            function=lambda e: self.__exit(),
        )

        self.button_cancel_exit_the_app = CreateOutlinedButton(
            text_button="No", function=lambda e: self.__cancel()
        )

        self.title_dialog = CreateText(text=self.get_config_excel(12), text_size=25)
        self.content_dialog = CreateText(text=self.get_config_excel(3), text_size=19)

        AlertDialog.__init__(
            self,
            title=self.title_dialog,
            content=self.content_dialog,
            actions=[self.button_exit_the_app, self.button_cancel_exit_the_app],
            actions_alignment=MainAxisAlignment.END,
        )

    def __exit(self):
        self.page.window_destroy()

    def __cancel(self):
        self.open = False
        self.page.update()

    def update_dialog(self):
        return self.update()
