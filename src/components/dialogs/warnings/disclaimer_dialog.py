# Widgets
from ...widgets.buttons import ElevatedButton

# Third-Party libraries
from flet import MainAxisAlignment, Page

# Settings
# from settings import ExcelTextLoader

# Control variables
# from control_variables import DisclaimerDialogControlVariable

# Base
from .._base import BaseDialog


class DisclaimerDialog(BaseDialog):
    def __init__(self, app: Page):
        # self.disclaimer_dialog = DisclaimerDialogControlVariable()

        self.button_close_dialog = ElevatedButton(
            text="Ok", function=lambda e: self.close_dialog()
        )

        super().__init__(
            title="",  # ExcelTextLoader.get_text(31),
            title_size=18,
            content="",  # ExcelTextLoader.get_text(32),
            content_size=16,
            actions=[self.button_close_dialog],
            actions_alignment=MainAxisAlignment.END,
            app=app,
        )

    # def show_dialog(self):
    #     disclaimer_dialog = self.disclaimer_dialog.get()

    #     if not disclaimer_dialog:
    #         self.disclaimer_dialog.set(True)

    #         return super().show_dialog()
