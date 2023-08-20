from flet import Page, dropdown

from components.ui import ContactUI, LanguageUI
from settings import EnvironmentVariables, ExcelTextLoader
from utils import check_type

from ..create_widgets import (
    CreateCheckbox,
    CreateDialog,
    CreateElevatedButton,
    CreateIconButton,
    CreateInputs,
    TaskBar,
)


class ChangeLanguage(LanguageUI):
    """
    Allows the user to change the language of the app
    """

    @check_type
    def __init__(
        self,
        appbar: TaskBar,
        page: Page,
        input_url: CreateInputs,
        input_directory: CreateInputs,
        close_dialog: CreateDialog,
        dropdown_contact: ContactUI,
        icon_language: CreateIconButton,
        icon_theme: CreateIconButton,
        button_exit_the_app: CreateElevatedButton,
        icon_update: CreateIconButton,
        checkbox: CreateCheckbox,
    ):
        self.appbar = appbar
        self.input_url = input_url
        self.input_directory = input_directory
        self.close_dialog = close_dialog
        self.dropdown_contact = dropdown_contact
        self.icon_language = icon_language
        self.icon_theme = icon_theme
        self.button_exit_the_app = button_exit_the_app
        self.icon_update = icon_update
        self.check_box = checkbox

        super().__init__(
            appbar=self.appbar,
            page=page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=self.close_dialog,
            dropdown_contact=self.dropdown_contact,
            icon_language=self.icon_language,
            icon_theme=self.icon_theme,
            button_exit_the_app=self.button_exit_the_app,
            callback=self.__change_language,
            icon_update=self.icon_update,
            checkbox=self.check_box,
        )

    @check_type
    def __change_language(self, page: Page):
        """
        Change the language of the application

        Args:
            page (flet.Page): Reference to the app window.
        """

        if self.value in ["Spanish", "Español"]:
            EnvironmentVariables.set_language(language="Español", page=self.page)

        else:
            EnvironmentVariables.set_language(language="English", page=self.page)

        self.visible = False

        self.options = [
            dropdown.Option(ExcelTextLoader.get_text(7)),
            dropdown.Option(ExcelTextLoader.get_text(8)),
        ]
        self.value = EnvironmentVariables.get_language()

        self.input_url.change_placeholder(ExcelTextLoader.get_text(14))
        self.input_directory.change_placeholder(ExcelTextLoader.get_text(15))

        self.close_dialog.update_title(ExcelTextLoader.get_text(12))

        self.close_dialog.update_content(ExcelTextLoader.get_text(3))

        self.button_exit_the_app.change_text(ExcelTextLoader.get_text(4))

        self.dropdown_contact.change_placeholder(ExcelTextLoader.get_text(16))

        self.icon_language.change_offset(offset_x=0, offset_y=0.3)
        self.check_box.set_label(ExcelTextLoader.get_text(20))

        if not self.dropdown_contact.is_visible():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.check_box.change_offset(offset_x=0, offset_y=0)

        page.update(
            self.appbar,
            self.input_url,
            self.input_directory,
            self,
            self.dropdown_contact,
            self.button_exit_the_app,
            self.close_dialog,
            self.check_box,
        )
