# Standard library
from typing import Callable

# Third-Party libraries
from flet import MainAxisAlignment, Page

# Widgets
from ...widgets.buttons import ElevatedButton, OutlinedButton

# Base
from .._base import BaseDialog


class UpdateDialog(BaseDialog):
    def __init__(self, app: Page, update_function: Callable):
        self.update_function = update_function
        self.button_update = ElevatedButton(
            app=app, text="Update", function=lambda _: self.update_function()
        )

        self.button_later = OutlinedButton(
            app=app, text="Later", function=lambda _: self.close_dialog()
        )

        self.button_ok = ElevatedButton(
            app=app, text="ok", function=lambda _: self.close_dialog()
        )

        super().__init__(
            title="Change this to the title of the update dialog",
            title_size=23,
            content="Change this to the content of the update dialogue",
            content_size=23,
            actions=[self.button_update, self.button_later],
            actions_alignment=MainAxisAlignment.END,
            app=app,
        )

    def show_dialog(self, an_update_is_available: bool):
        if not an_update_is_available:
            self.update_title("App updated to the latest version")
            self.update_content(
                "Congratulations! You already have the latest version, no need to upgrade"
            )

            self.actions = [self.button_ok]

            return super().show_dialog()

        return super().show_dialog()
