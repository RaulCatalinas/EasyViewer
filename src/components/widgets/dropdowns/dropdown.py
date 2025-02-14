# Standard library
from typing import Callable, Optional

# Third-Party libraries
from flet import Dropdown as FletDropdown, dropdown, Alignment


class Dropdown(FletDropdown):
    def __init__(
        self,
        options: list[dropdown.Option],
        visible: bool,
        alignment: Alignment,
        on_change: Callable,
        placeholder: Optional[str] = None,
        value: Optional[str] = None,
    ):
        super().__init__(
            options=options,
            visible=visible,
            alignment=alignment,
            hint_text=placeholder,
            value=value,
            on_change=on_change,
        )

    def change_visibility(self):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        self.visible = not self.visible

    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder text.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder
