# Standard library
from typing import Callable

# Third-Party libraries
from flet import (
    Column,
    LabelPosition,
    Page,
    icons,
)

# Create widgets
from frontend.create_widgets import (
    CreateCheckbox,
    CreateDialog,
    CreateElevatedButton,
    CreateIconButton,
    CreateInputs,
)

# Settings
from settings import ExcelTextLoader

# Utils
from utils import check_type


class TaskBarUI:
    @check_type
    def __init__(
        self,
        page: Page,
        input_url: CreateInputs,
        input_directory: CreateInputs,
        close_dialog: CreateDialog,
        button_exit_the_app: CreateElevatedButton,
        check_updates: Callable,
    ):
        # Backend
        from backend import Contact

        # Modify GUI
        from frontend.modify_gui import ChangeLanguage, ChangeTheme

        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.button_exit_the_app = button_exit_the_app

        self.checkbox = CreateCheckbox(
            label=ExcelTextLoader.get_text(20),
            label_position=LabelPosition.LEFT,
            callback=None,
            page=self.page,
        )

        self.icon_language = CreateIconButton(
            icon=icons.LANGUAGE,
            function=lambda e: self.dropdown_language.change_visibility(),
            offset_y=0.3,
        )

        self.icon_contact = CreateIconButton(
            icon=icons.CONTACTS,
            function=lambda e: self.dropdown_contact.change_visibility(),
            offset_y=0.3,
        )

        self.icon_theme = CreateIconButton(
            icon=ChangeTheme.set_initial_icon_theme(self.page),
            function=lambda e: ChangeTheme.change_theme(
                page=page, icon_theme=self.icon_theme
            ),
        )

        self.icon_update = CreateIconButton(
            icon=icons.UPDATE, function=lambda e: check_updates(page, False)
        )

        self.icon_update.set_visibility(
            visible=not self.checkbox.get_value(), page=page
        )

        self.checkbox.callback = lambda: self.icon_update.set_visibility(
            visible=not self.checkbox.get_value(), page=page
        )

        self.dropdown_language = ChangeLanguage(
            appbar=None,
            page=self.page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=self.close_dialog,
            dropdown_contact=None,
            icon_language=self.icon_language,
            icon_theme=self.icon_theme,
            button_exit_the_app=self.button_exit_the_app,
            icon_update=self.icon_update,
            checkbox=self.checkbox,
        )

        self.dropdown_contact = Contact(
            dropdown_language=self.dropdown_language,
            page=self.page,
            appbar=None,
            icon_contact=self.icon_contact,
            icon_theme=self.icon_theme,
            icon_update=self.icon_update,
            checkbox=self.checkbox,
        )

        self.dropdown_language.dropdown_contact = self.dropdown_contact

    def get_elements(self) -> list:
        """
        Get all taskbar items

        Returns:
            list: Taskbar items
        """

        return [
            self.checkbox,
            self.icon_theme,
            Column(controls=[self.icon_language, self.dropdown_language]),
            Column(controls=[self.icon_contact, self.dropdown_contact]),
            self.icon_update,
        ]
