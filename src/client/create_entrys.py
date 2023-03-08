"""Create the entries for the user to interact with the app"""

from tkinter import Entry
from tkinter.font import Font


class CreateEntrys(Entry):
    """This function creates an Input widget and positions it in the window."""

    def __init__(self, window, textvariable, font, font_size, width, y_axis_position):
        self.window = window
        self.textvariable = textvariable
        self.font = font
        self.font_size = font_size
        self.width = width
        self.y_axis_position = y_axis_position

        # Create the Entry
        super().__init__(
            self.window,
            textvariable=self.textvariable,
            font=Font(family=self.font, size=self.font_size),
            width=self.width,
        )
        # Position the Entry
        self.pack(pady=self.y_axis_position)

    def deactivate(self):
        """
        Disables the input widget.
        """
        self.config(state="disabled")

    def activate(self):
        """
        Change the state of the input widget to normal.
        """
        self.config(state="normal")
