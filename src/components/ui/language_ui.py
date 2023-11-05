# Standard library
from typing import Callable

# Third-Party libraries
from flet import Page, alignment, dropdown

# Create widgets
from ..widgets import (
    Checkbox,
    Dialog,
    ElevatedButton,
    IconButton,
    Input,
    TaskBar,
    Dropdown,
)

# Settings
from settings import EnvironmentVariables, ExcelTextLoader

# Utils
from utils import check_type


class LanguageUI(Dropdown):
    @check_type
    def __init__(
        self,
        appbar: TaskBar,
        page: Page,
        input_url: Input,
        input_directory: Input,
        close_dialog: Dialog,
        dropdown_contact: Dropdown,
        icon_language: IconButton,
        icon_theme: IconButton,
        button_exit_the_app: ElevatedButton,
        callback: Callable,
        icon_update: IconButton,
        checkbox: Checkbox,
    ):
        self.appbar = appbar
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.dropdown_contact = dropdown_contact
        self.icon_language = icon_language
        self.icon_theme = icon_theme
        self.button_exit_the_app = button_exit_the_app
        self.icon_update = icon_update
        self.checkbox = checkbox

        super().__init__(
            options=[
                dropdown.Option(ExcelTextLoader.get_text(7)),
                dropdown.Option(ExcelTextLoader.get_text(8)),
            ],
            value=EnvironmentVariables.get_language(),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: callback(page),
            page=page,
        )

    def change_visibility(self):
        dropdown_contact_is_visible = self.dropdown_contact.is_visible()

        if not self.visible:
            self.appbar.change_height(114)

            self.icon_language.change_offset(offset_x=0, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)
            self.checkbox.change_offset(offset_x=0, offset_y=-0.79)
            self.icon_update.change_offset(
                offset_x=(
                    -2.61
                    if self.visible
                    and dropdown_contact_is_visible
                    and dropdown_contact_is_visible is not None
                    else 0
                ),
                offset_y=-0.62,
            )

            return super().change_visibility(True)

        self.icon_language.change_offset(offset_x=0, offset_y=0.3)
        self.icon_update.change_offset(offset_x=0, offset_y=-0.62)

        if not dropdown_contact_is_visible:
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.checkbox.change_offset(offset_x=0, offset_y=0)

        return super().change_visibility(False)
