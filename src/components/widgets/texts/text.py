# Third-Party libraries
from flet import Text as FletText


class Text(FletText):
    """
    Create the text content for the app
    """

    def __init__(self, text: str, text_size: float):
        self.text = text
        self.text_size = text_size

        super().__init__(
            value=self.text, font_family="Arial", size=self.text_size
        )

    def set_text(self, new_text: str):
        """
        Change the text that is displayed

        Args:
            new_text (str): The new text to be displayed
        """

        self.value = new_text
