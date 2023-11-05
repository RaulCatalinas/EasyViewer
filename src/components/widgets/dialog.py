"""
Create a dialog to communicate something to the user
"""

# Standard library
from typing import Callable

# Third-Party libraries
from flet import AlertDialog, Icon, MainAxisAlignment, Page

# Utils
from utils import check_type

# Create text
from .text import Text


class Dialog(AlertDialog):
    """
    Create a dialog to communicate something to the user
    """

    @check_type
    def __init__(
        self,
        title: str,
        content: str,
        title_size: float,
        content_size: float,
        actions: list,
        overlay: Callable,
        app_page: Page,
        actions_alignment: MainAxisAlignment,
        icon: bool = False,
    ):
        self.overlay = overlay
        self.app_page = app_page

        self.title_text = Text(text=title, text_size=title_size)
        self.content_text = Text(text=content, text_size=content_size)

        super().__init__(
            title=(Icon(name=title, scale=title_size) if icon else self.title_text),
            content=self.content_text,
            actions=actions,
            actions_alignment=actions_alignment,
        )

    def change_state(self, page: Page):
        """
        If the dialog is not open it opens it and vice versa

        Args:
            page (flet.Page): Reference to the app window
        """

        self.open = not self.open
        page.update()

    @check_type
    def update_title(self, new_title: str):
        """
        Updates the title of the dialog.

        Args:
            new_title (str): The new title that will replace the current title
        """

        self.title_text.set_text(new_title)

    @check_type
    def update_content(self, new_content: str):
        """
        Updates the content of the dialog.

        Args:
            new_content (str): The new content that will replace the current one
        """

        self.content_text.set_text(new_content)

    def is_open(self):
        """
        Checks if the dialog is open.

        Returns:
            bool: True if the dialog is open, False otherwise
        """

        return self.open

    @check_type
    def show(self):
        """
        Show the dialogue
        """

        self.overlay(self.app_page)

        self.app_page.dialog = self

        self.change_state(self.app_page)
