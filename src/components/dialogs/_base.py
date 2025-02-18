"""
Create a dialog to communicate something to the user
"""

# Third-Party libraries
from flet import AlertDialog, Icon, MainAxisAlignment, Page

# Create text
from ..widgets.texts import Text


class BaseDialog(AlertDialog):
    """
    Create a dialog to communicate something to the user
    """

    def __init__(
        self,
        title: str,
        content: str,
        title_size: float,
        content_size: float,
        actions: list,
        app: Page,
        actions_alignment: MainAxisAlignment = MainAxisAlignment.CENTER,
        icon: bool = False,
        is_modal=False,
    ):
        self.app = app

        self.title_text = Text(text=title, text_size=title_size)
        self.content_text = Text(text=content, text_size=content_size)

        super().__init__(
            title=(
                Icon(name=title, scale=title_size) if icon else self.title_text
            ),
            content=self.content_text,
            actions=actions,
            actions_alignment=actions_alignment,
            modal=is_modal,
        )

    def update_title(self, new_title: str):
        """
        Updates the title of the dialog.

        Args:
            new_title (str): The new title that will replace the current title
        """

        self.title_text.set_text(new_title)

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

    def show_dialog(self):
        """
        Show the dialogue
        """

        self.app.open(self)

    def close_dialog(self):
        """
        Close the dialog
        """

        self.app.close(self)
