"""
Create the texts of the app
"""

from flet import Text

from utils import check_type


class CreateText(Text):
    """
    Create the texts of the app
    """

    @check_type
    def __init__(self, text: str, text_size: int):
        self.text = text
        self.text_size = text_size

        super().__init__(value=self.text, font_family="Arial", size=self.text_size)

    @check_type
    def change_text(self, new_text: str):
        """
        Changes the text

        :param new_text: The new text that will replace the current text
        """

        self.value = new_text
