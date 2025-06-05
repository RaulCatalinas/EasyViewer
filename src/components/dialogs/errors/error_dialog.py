# Standard library

# Third-Party libraries
from flet import MainAxisAlignment, Page, Icons

# Create widgets
from ...widgets.buttons import ElevatedButton

# Base
from .._base import BaseDialog


class ErrorDialog(BaseDialog):
    def __init__(self, app: Page):
        self.button_close_dialog = ElevatedButton(
            app=app, text="Ok", function=lambda _: self.close_dialog()
        )

        super().__init__(
            icon=True,
            title=Icons.ERROR,
            title_size=1.3,
            content="",
            content_size=23,
            actions=[self.button_close_dialog],
            actions_alignment=MainAxisAlignment.END,
            app=app,
        )

    def show_dialog(self, error: str):
        self.update_content(error)

        return super().show_dialog()
