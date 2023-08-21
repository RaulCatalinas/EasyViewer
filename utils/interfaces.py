"""
Interfaces for the program
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Callable

# Third-Party libraries
from flet import Page


class InterfaceIconButton(ABC):
    @abstractmethod
    def toggle_state(self, page: Page):
        """
        If the button is activated, it deactivates it and vice versa

        Args:
            page (flet.Page): Reference to the app window
        """

    @abstractmethod
    def change_offset(self, offset_x: int, offset_y: int):
        """
        Change the button offset

        Args:
            offset_x (int): Offset in x-axis
            offset_y (int): Offset in the y-axis
        """

    @abstractmethod
    def set_visibility(self, visible: bool, page: Page):
        """
        Change the visibility of the button

        Args:
            visible (bool): The new button visibility
            page (Page): Reference to the app window
        """


class InterfaceTextButton(ABC):
    """
    Interface for the creation of buttons
    """

    @abstractmethod
    def change_function(self, new_function: Callable, *args, **kwargs):
        """
        Change the function that is executed when the button is clicked

        Args:
            new_function (Callable): The new function that the button will execute
        """

    @abstractmethod
    def change_text(self, new_text: str):
        """
        Changes the text of the button.

        :param new_text: The new text that will replace the current text of the button
        """
