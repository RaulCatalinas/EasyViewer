"""Create the app labels"""

from tkinter import Label
from tkinter.font import Font


class CreateLabel(Label):
    """Creates the labels and places them on the screen"""

    def __init__(
        self, text, y_axis_position, width, background_color, font, font_size, window
    ):
        # Create a tag with the given parameters
        self.text = text
        self.y_axis_position = y_axis_position
        self.width = width
        self.background_color = background_color
        self.font = font
        self.font_size = font_size
        self.window = window

        # Create the label
        super().__init__(
            self.window,
            text=self.text,
            font=Font(family=self.font, size=self.font_size),
            width=self.width,
            bg=self.background_color,
        )

        # Put the label on the window
        self.pack(pady=self.y_axis_position)

    def update_text(self, new_text):
        """Change the text of the label to the new_text"""
        self.configure(text=new_text)
