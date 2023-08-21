# Standard library
from typing import Callable

# Third-Party libraries
from flet import Dropdown, Page, alignment, dropdown

# Create widgets
from frontend.create_widgets import (
    CreateCheckbox,
    CreateDialog,
    CreateElevatedButton,
    CreateIconButton,
    CreateInputs,
    TaskBar,
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
        input_url: CreateInputs,
        input_directory: CreateInputs,
        close_dialog: CreateDialog,
        dropdown_contact: Dropdown,
        icon_language: CreateIconButton,
        icon_theme: CreateIconButton,
        button_exit_the_app: CreateElevatedButton,
        callback: Callable,
        icon_update: CreateIconButton,
        checkbox: CreateCheckbox,
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
        )

    def change_visibility(self):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        drodropdown_contact_is_visible = self.dropdown_contact.is_visible()

        if not self.visible:
            self.visible = True
            self.appbar.change_height(114)

            self.icon_language.change_offset(offset_x=0, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)
            self.checkbox.change_offset(offset_x=0, offset_y=-0.79)
            self.icon_update.change_offset(
                offset_x=(
                    -2.61
                    if self.visible
                    and drodropdown_contact_is_visible
                    and drodropdown_contact_is_visible is not None
                    else 0
                ),
                offset_y=-0.62,
            )

            return self.page.update(self, self.appbar)

        self.visible = False
        self.icon_language.change_offset(offset_x=0, offset_y=0.3)
        self.icon_update.change_offset(offset_x=0, offset_y=-0.62)

        if not drodropdown_contact_is_visible:
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.checkbox.change_offset(offset_x=0, offset_y=0)

        return self.page.update(self, self.appbar)

    def is_visible(self):
        """
        Returns the visibility state of the dropdown.

        :return: Returns the value of the attribute `visible`.
        """

        return self.visible
