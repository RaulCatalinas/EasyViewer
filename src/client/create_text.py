"""
Create the texts of the app
"""

from flet import Text


class CreateText(Text):
    """
    Create the texts of the app
    """

    def __init__(self, text, text_size):
        self.text = text
        self.text_size = text_size

        super().__init__(value=self.text, font_family="Arial", size=self.text_size)

    def change_text(self, new_text):
        """
        Changes the text

        :param new_text: The new text that will replace the current text
        """

        self.value = new_text
