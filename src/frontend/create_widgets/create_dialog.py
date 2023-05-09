"""
Create a dialog to communicate something to the user
"""

from flet import Icon, AlertDialog, MainAxisAlignment, Page

from create_text import CreateText
from utils import check_type


class CreateDialog(AlertDialog):
    """
    Create a dialog to communicate something to the user
    """

    @check_type
    def __init__(
        self,
        title_dialog: str | Icon,
        content_dialog: str,
        title_size: float,
        content_size: float,
        actions_dialog: list,
        actions_alignment_dialog: MainAxisAlignment,
        icon: bool = False,
    ) -> None:
        self.title_dialog = title_dialog
        self.content_dialog = content_dialog
        self.title_size = title_size
        self.content_size = content_size
        self.actions_dialog = actions_dialog
        self.actions_alignment_dialog = actions_alignment_dialog
        self.icon = icon

        self.title_text = CreateText(text=self.title_dialog, text_size=self.title_size)
        self.content_text = CreateText(
            text=self.content_dialog, text_size=self.content_size
        )

        super().__init__(
            self,
            title=(
                Icon(name=self.title_dialog, scale=self.title_size)
                if self.icon
                else self.title_text
            ),
            content=self.content_text,
            actions=self.actions_dialog,
            actions_alignment=self.actions_alignment_dialog,
        )

    def change_state(self, page: Page) -> None:
        """
        If the dialog is not open, it opens it and updates the window, if it's open, it closes it and updates the window

        :param page: Is a reference to the app window
        """

        if not self.open:
            self.open = True

        else:
            self.open = False

        page.update()

    @check_type
    def update_title_dialog(self, new_title: str):
        """
        Updates the title of the dialog.

        :param new_title: The new title that will replace the current title
        """

        self.title_text.change_text(new_title)

    @check_type
    def update_content_dialog(self, new_content: str):
        """
        Updates the content of the dialog.

        :param new_content: The new content that will replace the current content of the dialog
        """

        self.content_text.change_text(new_content)
