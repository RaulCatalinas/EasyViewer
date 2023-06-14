from flet import Text

from utils import check_type


class CreateText(Text):
    """
    Create the text content for the app
    """

    @check_type
    def __init__(self, text: str, text_size: int):
        self.text = text
        self.text_size = text_size

        super().__init__(value=self.text, font_family="Arial", size=self.text_size)

    @check_type
    def set_text(self, new_text: str):
        """
        Set a new text content.

        :param new_text: The new text content.
        """

        self.value = new_text
