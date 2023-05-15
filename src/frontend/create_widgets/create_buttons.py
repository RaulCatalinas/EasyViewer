"""
Create three types of buttons
"""

from typing import Callable

from flet import IconButton, ElevatedButton, OutlinedButton, Offset, Icon, Page

from utils import check_type, InterfaceIconButton, InterfaceTextButton


class CreateIconButton(InterfaceIconButton, IconButton):
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

        IconButton.__init__(
            self,
            icon=self.icon_for_the_button,
            on_click=self.function,
            scale=self.scale_button,
            offset=Offset(self.offset_x, self.offset_y),
        )

    @check_type
    def toggle_state(self, page: Page):
        self.disabled = not self.disabled

        return page.update(self)

    @check_type
    def change_offset(self, offset_x: int, offset_y: int):
        self.offset = Offset(offset_x, offset_y)


class CreateElevatedButton(InterfaceTextButton, ElevatedButton):
    """
    Create a button of type ElevatedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        ElevatedButton.__init__(self, text=self.text_button, on_click=self.function)

    @check_type
    def change_text(self, new_text: str):
        self.text = new_text

    @check_type
    def change_function(self, new_function: Callable, *args, **kwargs):
        self.on_click = lambda e: new_function(*args, **kwargs)


class CreateOutlinedButton(InterfaceTextButton, OutlinedButton):
    """
    Create a button of type OutlinedButton
    """

    @check_type
    def __init__(self, text_button: str, function: Callable):
        self.text_button = text_button
        self.function = function

        OutlinedButton.__init__(self, text=self.text_button, on_click=self.function)

    @check_type
    def change_function(self, new_function: Callable, *args, **kwargs):
        self.on_click = lambda e: new_function(*args, **kwargs)

    @check_type
    def change_text(self, new_text: str):
        self.text = new_text
