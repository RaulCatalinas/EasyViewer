"""
Create the inputs
"""

# Third-Party libraries
from flet import Offset, TextAlign, TextField, Page


class Input(TextField):
    """
    Create the inputs
    """

    def __init__(
        self,
        placeholder: str,
        text_size: int,
        app: Page,
        text_align: TextAlign = TextAlign.CENTER,
        offset_x: float = 0,
        offset_y: float = 0,
        autofocus: bool = False,
        read_only: bool = False,
        initial_value: str | None = None,
        is_multiline: bool = False,
        max_height: int = 1,
    ):
        self.app = app

        super().__init__(
            hint_text=placeholder,
            autofocus=autofocus,
            read_only=read_only,
            text_size=text_size,
            text_align=text_align,
            offset=Offset(offset_x, offset_y),
            value=initial_value,
            multiline=is_multiline,
            max_lines=max_height,
        )

    def toggle_state(self):
        """
        If the input is activated, it deactivates it and vice versa
        """

        self.disabled = not self.disabled

        self.app.update(self)

    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder

    def set_value(self, new_value: str):
        """
        Sets a new value for the input.

        Args:
            new_value (str): The new value that will be assigned to the input
        """

        self.value = new_value

        self.app.update(self)

    def get_value(self):
        """
        Get the current value of the input.

        Returns:
            str: The current value of the input.
        """

        return self.value
