# Standard library
from typing import Callable

# Third-Party libraries
from flet import ElevatedButton, Icon, IconButton, Offset, OutlinedButton, Page

# Utils
from utils import InterfaceIconButton, InterfaceTextButton, check_type


class CreateIconButton(InterfaceIconButton, IconButton):
    """
    Creates a button of type IconButton
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

        Args:
            page (flet.Page): Reference to the app window
        """

        self.disabled = not self.disabled
        page.update(self)

    @check_type
    def change_offset(self, offset_x: int, offset_y: int):
        """
        Change the button offset

        Args:
            offset_x (int): Offset in x-axis
            offset_y (int): Offset in the y-axis
        """

        self.offset = Offset(offset_x, offset_y)

    @check_type
    def set_visibility(self, visible: bool, page: Page):
        """
        Change the visibility of the button

        Args:
            visible (bool): The new button visibility
            page (Page): Reference to the app window
        """

        self.visible = visible
        page.update(self)


class CreateElevatedButton(InterfaceTextButton, ElevatedButton):
    """
    Creates a button of type ElevatedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    @check_type
    def change_text(self, new_text: str):
        """
        Change the text displayed on the button

        Args:
            new_text (str): The new text to display on the button
        """

        self.text = new_text

    @check_type
    def change_function(self, new_function: Callable, *args, **kwargs):
        """
        Change the function that is executed when the button is clicked

        Args:
            new_function (Callable): The new function that the button will execute
        """

        self.on_click = lambda e: new_function(*args, **kwargs)


class CreateOutlinedButton(InterfaceTextButton, OutlinedButton):
    """
    Creates a button of type OutlinedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    @check_type
    def change_function(self, new_function: Callable, *args, **kwargs):
        """
        Change the function that is executed when the button is clicked

        Args:
            new_function (Callable): The new function that the button will execute
        """

        self.on_click = lambda e: new_function(*args, **kwargs)

    @check_type
    def change_text(self, new_text: str):
        """
        Change the text displayed on the button

        Args:
            new_text (str): The new text to display on the button
        """

        self.text = new_text
