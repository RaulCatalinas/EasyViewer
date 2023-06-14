"""
Create a dialog to communicate something to the user
"""

from typing import Union

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
        title: Union[str, Icon],
        content: str,
        title_size: float,
        content_size: float,
        actions: list,
        actions_alignment: MainAxisAlignment,
        icon: bool = False,
    ) -> None:
        self.title_text = CreateText(text=title, text_size=title_size)
        self.content_text = CreateText(text=content, text_size=content_size)

        super().__init__(
            title=(Icon(name=title, scale=title_size) if icon else self.title_text),
            content=self.content_text,
            actions=actions,
            actions_alignment=actions_alignment,
        )

    def change_state(self, page: Page) -> None:
        """
        If the dialog is not open, it opens it and updates the window. If it's open, it closes it and updates the window.

        :param page: A reference to the app window
        """

        self.open = not self.open
        page.update()

    @check_type
    def update_title(self, new_title: str):
        """
        Updates the title of the dialog.

        :param new_title: The new title that will replace the current title
        """

        self.title_text.set_text(new_title)

    @check_type
    def update_content(self, new_content: str):
        """
        Updates the content of the dialog.

        :param new_content: The new content that will replace the current content of the dialog
        """

        self.content_text.set_text(new_content)

    def is_open(self):
        """
        Checks if the dialog is open.

        :return: True if the dialog is open, False otherwise
        """

        return self.open
