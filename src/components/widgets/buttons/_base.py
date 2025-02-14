# Standard library
from typing import Callable, Union
from functools import partial

# Third-Party libraries
from flet import Control, Page, Offset

# Third-Party libraries
from flet import (
    ElevatedButton as FletElevatedButton,
    OutlinedButton as FletOutlinedButton,
)


class BaseButton(Control):
    """
    Base class for buttons to encapsulate common behavior.
    """

    def __init__(self):
        super().__init__()

    def change_function(self, new_function: Callable, *args, **kwargs):
        """
        Change the function that is executed when the button is clicked.

        Args:
            new_function (Callable): The new function that the button will execute.
        """
        self.on_click = partial(new_function, *args, **kwargs)

    def toggle_state(self, app: Page):
        """Toggles the button state (enabled/disabled)."""
        self.disabled = not self.disabled

        app.update(self)

    def change_offset(self, offset_x: int, offset_y: int):
        """Changes the button's offset."""

        self.offset = Offset(offset_x, offset_y)


class BaseTextButton(BaseButton):
    """
    Base class for text-based buttons (ElevatedButton, OutlinedButton).
    """

    def __init__(
        self, button_reference: Union[FletElevatedButton, FletOutlinedButton]
    ):
        super().__init__()

        self.button_reference = button_reference

    def change_text(self, new_text: str):
        """Updates the button text."""

        self.button_reference.text = new_text
