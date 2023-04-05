"""Create a dialog to communicate something to the user"""

from flet import Icon, AlertDialog

from create_text import CreateText


class CreateDialog(AlertDialog):
    """Create a dialog with a title, content, and actions to communicate something to the user"""

    def __init__(
        self,
        title_dialog: str | Icon,
        content_dialog: str,
        title_size: float,
        content_size: float,
        actions_dialog: list,
        actions_alignment_dialog,
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

    def change_state(self, page) -> None:
        """
        If the dialog is not open, open it and update the page. If the dialog is open, close it and
        update the page

        :param page: The page that the dialog is on
        :return: The page.update() function is being returned.
        """
        if not self.open:
            self.open = True

        else:
            self.open = False

        page.update()

    def update_text(self, text_title, text_content):
        """
        It takes two strings as arguments, and returns a tuple of two functions

        :param text_title: The title of the text
        :param text_content: The text that will be displayed in the content text box
        :return: A tuple of the return values of the two methods.
        """
        self.title_text.change_text(text_title)
        self.content_text.change_text(text_content)
