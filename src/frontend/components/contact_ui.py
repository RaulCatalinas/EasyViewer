from typing import Callable

from flet import AppBar, Checkbox, Dropdown, IconButton, Page, alignment, dropdown

from settings import ExcelTextLoader
from utils import check_type


class ContactUI(Dropdown):
    """
    Controls the user interface for contacting the developer
    """

    @check_type
    def __init__(
        self,
        dropdown_language: Dropdown,
        page: Page,
        appbar: AppBar,
        icon_contact: IconButton,
        icon_theme: IconButton,
        callback: Callable,
        icon_update: IconButton,
        checkbox: Checkbox,
    ):
        self.dropdown_language = dropdown_language
        self.page = page
        self.appbar = appbar
        self.icon_contact = icon_contact
        self.icon_theme = icon_theme
        self.icon_update = icon_update
        self.checkbox = checkbox

        super().__init__(
            options=[
                dropdown.Option("Facebook"),
                dropdown.Option("Instagram"),
                dropdown.Option("Twitter"),
                dropdown.Option("GitHub"),
            ],
            hint_text=ExcelTextLoader.get_text(16),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: callback(),
        )

    def change_visibility(self):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        if not self.visible:
            self.visible = True

            self.appbar.change_height(114)

            self.icon_contact.change_offset(offset_x=0, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)
            self.checkbox.change_offset(offset_x=0, offset_y=-0.79)
            self.icon_update.change_offset(
                offset_x=(
                    -2.61 if self.visible and self.dropdown_language.is_visible() else 0
                ),
                offset_y=-0.62,
            )

            return self.page.update(self, self.appbar)

        self.visible = False
        self.icon_contact.change_offset(offset_x=0, offset_y=0.3)
        self.icon_update.change_offset(offset_x=0, offset_y=-0.62)

        if not self.dropdown_language.is_visible():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.checkbox.change_offset(offset_x=0, offset_y=0)

        return self.page.update(self, self.appbar)

    def is_visible(self) -> bool:
        """
        Checks if the dialog is visible.

        Returns:
            bool: True if the dropdown is visible, False otherwise
        """

        return self.visible

    @check_type
    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder text.

        Args:
            new_placeholder (str): The new placeholder that will replace the current one
        """

        self.hint_text = new_placeholder
