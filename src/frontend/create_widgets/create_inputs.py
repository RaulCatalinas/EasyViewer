"""
Create the inputs
"""

from flet import TextField, KeyboardType, Offset, MainAxisAlignment

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
        text_align: MainAxisAlignment,
        offset_x: int = 0,
        offset_y: int = 0,
        keyboard_type: KeyboardType = KeyboardType.TEXT,
        autofocus: bool = False,
        read_only: bool = False,
        value_input: str | None = None,
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
        )

    def toggle_state(self, page):
        """
        If the input is activated, it deactivates it and vice versa

        :param page: Is a reference to the app window
        """

        self.disabled = not self.disabled

        return page.update(self)

    def change_placeholder(self, new_placeholder):
        """
        Changes the placeholder.

        :param new_placeholder: The new placeholder that will replace the current placeholder
        """

        self.hint_text = new_placeholder

    def set_value(self, new_value):
        """
        Sets a new value for the input.

        :param new_value: The new value that will be assigned to the input
        """

        self.value = new_value

    def get_value(self):
        """
        Get the current value of the input.

        :return: The current value of the input.
        """

        return self.value
