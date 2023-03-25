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

        AlertDialog.__init__(
            self,
            title=CreateText(text=self.get_config_excel(12), text_size=25),
            content=CreateText(text=self.get_config_excel(3), text_size=19),
            actions=[
                CreateElevatedButton(
                    text_button=self.get_config_excel(4),
                    function=lambda e: self.__exit(),
                ),
                CreateOutlinedButton(
                    text_button="No", function=lambda e: self.__cancel()
                ),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def __exit(self):
        self.page.window_destroy()

    def __cancel(self):
        self.open = False
        self.page.update()
