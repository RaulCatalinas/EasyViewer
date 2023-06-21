from typing import Callable

from flet import icons, Column, Page, TextField, AlertDialog, ElevatedButton

from config import ExcelTextLoader
from create_widgets import CreateIconButton, CreateCheckbox
from utils import check_type


class TaskBarUI:
    @check_type
    def __init__(
        self,
        page: Page,
        input_url: TextField,
        input_directory: TextField,
        close_dialog: AlertDialog,
        button_exit_the_app: ElevatedButton,
        check_updates: Callable,
    ):
        from modify_gui import ChangeLanguage, ChangeTheme
        from backend import Contact

        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.button_exit_the_app = button_exit_the_app

        self.checkbox = CreateCheckbox(
            label=ExcelTextLoader.get_text(20),
            label_position="left",
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
                page=self.page, icon_theme=self.icon_theme
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

    def get_elements(self):
        return [
            self.checkbox,
            self.icon_theme,
            Column(controls=[self.icon_language, self.dropdown_language]),
            Column(controls=[self.icon_contact, self.dropdown_contact]),
            self.icon_update,
        ]