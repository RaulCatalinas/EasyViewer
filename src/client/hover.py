"""Hover effect for buttons"""


class Hover:
    """
    Hover effect for buttons
    It takes a button, a color for when the mouse is over the button, and a color for when the mouse is not over the button.

    :param button: The button to which the hover effect will be applied
    :param color_mouse_in: The color of the button when the mouse is over it
    :param color_mouse_out: The color of the button when the mouse is not over it
    """

    def __init__(self, button, color_mouse_in, color_mouse_out):
        self.button = button
        self.color_mouse_in = color_mouse_in
        self.color_mouse_out = color_mouse_out

        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=color_mouse_in, cursor="hand2"),
        )

        button.bind("<Leave>", func=lambda e: button.config(background=color_mouse_out))
