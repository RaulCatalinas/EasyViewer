# Base
from .._base import BaseDialog

# Widgets
from ...widgets.buttons import ElevatedButton, OutlinedButton

# Third-Party libraries
from flet import Page


class CloseAppDialog(BaseDialog):
    def __init__(self, app: Page):
        self.button_close_app = ElevatedButton(
            app=app,
            text="Yes",
            function=lambda _: self.app.window.destroy(),
            scale=1.2,
            offset_x=-0.24,
        )

        self.button_close_dialog = OutlinedButton(
            app=app,
            text="No",
            function=lambda _: self.close_dialog(),
            scale=1.1,
            offset_x=0.2,
        )

        super().__init__(
            title="Close Application",
            content="Are you sure you wanna close the application?",
            title_size=23,
            content_size=20,
            actions=[self.button_close_app, self.button_close_dialog],
            app=app,
        )
