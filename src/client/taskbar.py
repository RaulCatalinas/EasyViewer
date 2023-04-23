"""
Control the logic of the taskbar
"""

from flet import AppBar, icons, Column

from app_settings import AppSettings
from change_language import ChangeLanguage
from change_theme import ChangeTheme
from contact import Contact
from create_buttons import CreateIconButton


class TaskBar(AppBar, AppSettings):
    """
    Create a taskbar
    """

    def __init__(
        self,
        page,
        input_url,
        input_directory,
        close_dialog,
        button_exit_the_app,
    ):
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.button_exit_the_app = button_exit_the_app

        AppSettings.__init__(self)
        self.change_theme = ChangeTheme()

        self.icon_language = CreateIconButton(
            icon_button=icons.LANGUAGE,
            function=lambda e: self.dropdown_language.change_visibility_dropdown_language(),
            offset_y=0.3,
        )

        self.icon_contact = CreateIconButton(
            icon_button=icons.CONTACTS,
            function=lambda e: self.dropdown_contact.change_visibility_dropdown_contact(),
            offset_y=0.3,
        )

        self.icon_theme = CreateIconButton(
            icon_button=self.change_theme.set_initial_icon_theme(self.page),
            function=lambda e: self.change_theme.change_theme(
                page=self.page, icon_theme=self.icon_theme
            ),
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
        )

        self.dropdown_contact = Contact(
            dropdown_language=self.dropdown_language,
            page=self.page,
            appbar=self,
            icon_contact=self.icon_contact,
            icon_theme=self.icon_theme,
        )

        self.dropdown_language.dropdown_contact = self.dropdown_contact

    def _build(self):
        return AppBar.__init__(
            self,
            actions=[
                self.icon_theme,
                Column(controls=[self.icon_language, self.dropdown_language]),
                Column(controls=[self.icon_contact, self.dropdown_contact]),
            ],
            toolbar_height=63,
        )

    def change_height(self, new_height):
        """
        Changes the height of the taskbar.

        :param new_height: The new height that will be assigned to the taskbar
        """

        self.toolbar_height = new_height
