"""Create a button in the desired position and function to execute"""

from tkinter import Button
from tkinter.font import Font

from hover import Hover


class CreateButton(Button):
    """
    Create a button.

    :param text: The text to be displayed on the button
    :param position_x_axis: The x position of the button
    :param width: width
    :param background_color: The background color of the button
    :param function: The function the button will call when clicked
    :param window: The window the button will be in
    :param color_mouse_in: The color of the button when the mouse is over it
    :param mouse_color_out: The color of the button when the mouse is not over it
    :param absolute_position: If True, the button will be positioned in the window using the
    pack() method. If it is False, it will be placed using the place() method.
    :param position_y_axis: The y position of the button
    """

    def __init__(
        self,
        text,
        width,
        background_color,
        function,
        window,
        color_mouse_in,
        color_mouse_out,
        absolute_position,
        font,
        font_size,
        y_axis_position,
        x_axis_position=None,
    ):
        self.text = text
        self.width = width
        self.background_color = background_color
        self.window = window
        self.color_mouse_in = color_mouse_in
        self.color_mouse_out = color_mouse_out
        self.function = function
        self.absolute_position = absolute_position
        self.position_x_axis = x_axis_position
        self.y_axis_position = y_axis_position
        self.font = font
        self.font_size = font_size

        super().__init__(
            self.window,
            text=self.text,
            bg=self.background_color,
            font=Font(family=self.font, size=self.font_size),
            command=self.function,
            width=self.width,
        )

        if self.absolute_position:
            self.pack(pady=self.y_axis_position)
        else:
            self.place(x=self.position_x_axis, y=self.y_axis_position)

        Hover(
            self,
            self.color_mouse_in,
            self.color_mouse_out,
        )

    def disable(self):
        """
        Disable the button
        """
        self.configure(state="disabled")

    def activate(self):
        """
        Enable the button
        """
        self.configure(state="normal")

    def update_text(self, new_text):
        """
        Takes a string as an argument and changes the button text to that string

        :param new_text: The new text to be displayed on the button
        """
        self.configure(text=new_text)
