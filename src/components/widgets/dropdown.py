# Standard library
from typing import Callable, Union

# Third-Party libraries
from flet import Dropdown as FletDropdown, dropdown, Alignment, Page

# Utils
from utils import check_type


class Dropdown(FletDropdown):
    @check_type
    def __init__(
        self,
        page: Page,
        options: list[dropdown.Option],
        visible: bool,
        alignment: Alignment,
        on_change: Callable,
        placeholder: Union[str, None] = None,
        value: Union[str, None] = None,
    ):
        self.page = page

        super().__init__(
            options=options,
            visible=visible,
            alignment=alignment,
            hint_text=placeholder,
            value=value,
            on_change=on_change,
        )

    def is_visible(self):
        """
        Returns the visibility state of the dropdown.

        :return: Returns the value of the attribute `visible`.
        """

        return self.visible

    @check_type
    def change_visibility(self, visibility: bool):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        if self.page is None:
            return

        self.visible = visibility

        self.page.update()

    @check_type
    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder text.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder
