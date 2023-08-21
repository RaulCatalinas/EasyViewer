# Third-Party libraries
from flet import Text

# Utils
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
        Change the text that is displayed

        Args:
            new_text (str): The new text to be displayed
        """

        self.value = new_text
