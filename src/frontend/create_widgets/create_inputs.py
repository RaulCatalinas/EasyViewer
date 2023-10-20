"""
Create the inputs
"""

# Third-Party libraries
from flet import KeyboardType, Offset, Page, TextAlign, TextField

# Utils
from utils import check_type


class CreateInputs(TextField):
    """
    Create the inputs
    """

    @check_type
    def __init__(
        self,
        placeholder: str,
        text_size: int,
        text_align: TextAlign,
        offset_x: int = 0,
        offset_y: int = 0,
        keyboard_type: KeyboardType = KeyboardType.TEXT,
        autofocus: bool = False,
        read_only: bool = False,
        value_input: str | None = None,
        is_multiline: bool = False,
        max_height: int = 1,
    ):
        self.placeholder_input = placeholder
        self.text_size_input = text_size
        self.keyboard_type_input = keyboard_type
        self.text_align_input = text_align
        self.autofocus_input = autofocus
        self.read_only_input = read_only
        self.value_input = value_input
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.max_height = max_height
        self.is_multiline = is_multiline

    def _build(self):
        return super().__init__(
            hint_text=self.placeholder_input,
            keyboard_type=self.keyboard_type_input,
            autofocus=self.autofocus_input,
            read_only=self.read_only_input,
            text_size=self.text_size_input,
            text_align=self.text_align_input,
            offset=Offset(self.offset_x, self.offset_y),
            value=self.value_input,
            multiline=self.is_multiline,
            max_lines=self.max_height,
        )

    @check_type
    def toggle_state(self, page: Page):
        """
        If the input is activated, it deactivates it and vice versa

        Args:
            page (flet.Page): Reference to the app window
        """

        self.disabled = not self.disabled
        page.update(self)

    @check_type
    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder

    @check_type
    def set_value(self, new_value: str):
        """
        Sets a new value for the input.

        Args:
            new_value (str): The new value that will be assigned to the input
        """

        self.value = new_value

    def get_value(self):
        """
        Get the current value of the input.

        Returns:
            str: The current value of the input.
        """

        return self.value
