# Standard library
from typing import Callable, Optional, List

# Third-Party libraries
from flet import Dropdown, dropdown, Alignment, Page


class DropdownBase(Dropdown):
    def __init__(
        self,
        app: Page,
        options: List[dropdown.Option],
        on_change: Callable,
        visible: bool = True,
        alignment: Optional[Alignment] = None,
        placeholder: Optional[str] = None,
        value: Optional[str] = None,
    ):
        self.app = app

        super().__init__(
            options=options,
            visible=visible,
            alignment=alignment,
            hint_text=placeholder,
            value=value,
            on_change=on_change,
        )

    def toggle_visibility(self):
        """
        If the input is activated, it deactivates it and vice versa
        """

        self.visible = not self.visible

        self.app.update(self)

    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder text.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder

        self.app.update(self)
