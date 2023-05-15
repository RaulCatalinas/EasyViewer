"""
Interfaces for the program
"""

from abc import ABC, abstractmethod
from typing import Callable

from flet import Page


class InterfaceIconButton(ABC):
    @abstractmethod
    def toggle_state(self, page: Page):
        """
        If the button is activated, it deactivates it and vice versa

        :param page: Is a reference to the app window
        """

    @abstractmethod
    def change_offset(self, offset_x: int, offset_y: int):
        """
        Changes the offset of the button using the given x and y values.

        :param offset_x: x-coordinate offset

        :param offset_y: y-coordinate offset
        """


class InterfaceTextButton(ABC):
    """
    Interface for the creation of buttons
    """

    @abstractmethod
    def change_function(self, new_function: Callable, *args, **kwargs):
        """
        Takes a new function and its arguments, and sets it as the on_click event.

        :param new_function: The new function that will be executed when the button is clicked
        """

    @abstractmethod
    def change_text(self, new_text: str):
        """
        Changes the text of the button.

        :param new_text: The new text that will replace the current text of the button
        """
