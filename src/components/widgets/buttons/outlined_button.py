# Standard Library
from typing import Callable

# Third-Party libraries
from flet import OutlinedButton as FletOutlinedButton, Offset, Page

# Base
from ._base import BaseTextButton


class OutlinedButton(FletOutlinedButton, BaseTextButton):
    """
    Creates a button of type OutlinedButton.
    """

    def __init__(
        self,
        app: Page,
        text: str,
        function: Callable,
        scale: float = 1,
        offset_x: float = 0,
        offset_y: float = 0,
    ):
        BaseTextButton.__init__(self, button_reference=self, app=app)

        super().__init__(
            text=text,
            on_click=function,
            scale=scale,
            offset=Offset(offset_x, offset_y),
        )
