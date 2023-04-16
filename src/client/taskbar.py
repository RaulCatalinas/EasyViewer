"""Control the logic of the taskbar"""

from flet import AppBar, icons, Column, Offset

from app_settings import AppSettings
from change_language import ChangeLanguage
from change_theme import ChangeTheme
from contact import Contact
from create_buttons import CreateIconButton


class TaskBar(AppBar, AppSettings):
    """Create a taskbar with a dropdown to change the language, a dropdown to contact the developer, and create a button to toggle the app theme between light and dark theme."""

    def __init__(
        self,
        page,
        input_url,
        input_directory,
        close_dialog,
        button_exit_the_app,
        check_updates,
    ):
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.button_exit_the_app = button_exit_the_app
        self.check_updates = check_updates

        AppSettings.__init__(self)
        self.change_theme = ChangeTheme()

        self.icon_language = CreateIconButton(
            icon_button=icons.LANGUAGE,
            function=lambda e: self.dropdown_language.change_visibility_dropdown_language(),
            offset_button=Offset(0, 0.3),
        )

        self.icon_contact = CreateIconButton(
            icon_button=icons.CONTACTS,
            function=lambda e: self.dropdown_contact.change_visibility_dropdown_contact(),
            offset_button=Offset(0, 0.3),
        )

        self.icon_theme = CreateIconButton(
            icon_button=self.change_theme.set_initial_icon_theme(self.page),
            function=lambda e: self.change_theme.change_theme(
                page=self.page, icon_theme=self.icon_theme
            ),
        )

        self.icon_update = CreateIconButton(
            icon_button=icons.UPDATE,
            function=lambda e: self.check_updates(self.page),
        )

        self.dropdown_language = ChangeLanguage(
            appbar=self,
            page=self.page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=self.close_dialog,
            dropdown_contact=None,
            icon_language=self.icon_language,
            icon_theme=self.icon_theme,
            button_exit_the_app=self.button_exit_the_app,
            icon_update=self.icon_update,
        )

        self.dropdown_contact = Contact(
            dropdown_language=self.dropdown_language,
            page=self.page,
            appbar=self,
            icon_contact=self.icon_contact,
            icon_theme=self.icon_theme,
            icon_update=self.icon_update,
        )

        self.dropdown_language.dropdown_contact = self.dropdown_contact

    def _build(self):
        return AppBar.__init__(
            self,
            actions=[
                self.icon_theme,
                Column(controls=[self.icon_language, self.dropdown_language]),
                Column(controls=[self.icon_contact, self.dropdown_contact]),
                self.icon_update,
            ],
            toolbar_height=63,
        )
