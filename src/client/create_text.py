from flet import Text


class CreateText(Text):
    def __init__(self, text, text_size):
        self.text = text
        self.text_size = text_size

        super().__init__(value=self.text, font_family="Arial", size=self.text_size)

    def change_text(self, new_text):
        self.value = new_text
