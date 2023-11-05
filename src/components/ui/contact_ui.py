# Standard library
from typing import Callable

# Third-Party libraries
from flet import Page, alignment, dropdown

# Create widgets
from ..widgets import Checkbox, IconButton, TaskBar, Dropdown

# Settings
from settings import ExcelTextLoader

# Utils
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
        appbar: TaskBar,
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
            placeholder=ExcelTextLoader.get_text(16),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: callback(),
            page=page,
        )

    def change_visibility(self):
        dropdown_language_is_visible = self.dropdown_language.is_visible()

        if not self.visible:
            self.appbar.change_height(114)

            self.icon_contact.change_offset(offset_x=0, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)
            self.checkbox.change_offset(offset_x=0, offset_y=-0.79)
            self.icon_update.change_offset(
                offset_x=(
                    -2.61 if self.visible and dropdown_language_is_visible else 0
                ),
                offset_y=-0.62,
            )

            return super().change_visibility(True)

        self.icon_contact.change_offset(offset_x=0, offset_y=0.3)
        self.icon_update.change_offset(offset_x=0, offset_y=-0.62)

        if (
            not dropdown_language_is_visible
            and dropdown_language_is_visible is not None
        ):
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.checkbox.change_offset(offset_x=0, offset_y=0)

        return super().change_visibility(False)
