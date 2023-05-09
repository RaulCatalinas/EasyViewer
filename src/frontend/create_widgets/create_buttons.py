"""
Create three types of buttons
"""

from typing import Callable

from flet import IconButton, ElevatedButton, OutlinedButton, Offset, Icon, Page

from utils import check_type


class CreateIconButton(IconButton):
    """
    Create a button of type IconButton
    """

    @check_type
    def __init__(
        self,
        icon: Icon,
        function: Callable,
        offset_x: int = 0,
        offset_y: int = 0,
        scale: int = 1,
    ):
        self.icon_for_the_button = icon
        self.function = function
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.scale_button = scale

        super().__init__(
            icon=self.icon_for_the_button,
            on_click=self.function,
            scale=self.scale_button,
            offset=Offset(self.offset_x, self.offset_y),
        )

    @check_type
    def toggle_state(self, page: Page):
        """
        If the button is activated, it deactivates it and vice versa

        :param page: Is a reference to the app window
        """

        self.disabled = not self.disabled

        return page.update(self)

    @check_type
    def change_offset(self, offset_x: int, offset_y: int):
        """
        Changes the offset of the button using the given x and y values.

        :param offset_x: x-coordinate offset

        :param offset_y: y-coordinate offset
        """

        self.offset = Offset(offset_x, offset_y)


class CreateElevatedButton(ElevatedButton):
    """
    Create a button of type ElevatedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    @check_type
    def change_text_button(self, new_text: str):
        """
        Changes the text of the button.

        :param new_text: The new text that will replace the current text of the button
        """

        self.text = new_text

    @check_type
    def change_function(self, new_function: Callable, *args):
        """
        Takes a new function and its arguments, and sets it as the on_click event.

        :param new_function: The new function that will be executed when the button is clicked
        """

        self.on_click = lambda e: new_function(*args)


class CreateOutlinedButton(OutlinedButton):
    """
    Create a button of type OutlinedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    @check_type
    def change_function(self, new_function: Callable, *args):
        """
        Takes a new function and its arguments, and sets it as the on_click event.

        :param new_function: The new function that will be executed when the button is clicked
        """

        self.on_click = lambda e: new_function(*args)
