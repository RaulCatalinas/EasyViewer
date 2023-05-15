"""
Control the logic to be able to change the language of the app
"""

from flet import Dropdown, dropdown, alignment

from config import ExcelTextLoader, EnvironmentVariables


class ChangeLanguage(Dropdown):
    """
    Allows the user to change the language of the app
    """

    def __init__(
        self,
        appbar,
        page,
        input_url,
        input_directory,
        close_dialog,
        dropdown_contact,
        icon_language,
        icon_theme,
        button_exit_the_app,
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

        Dropdown.__init__(
            self,
            options=[
                dropdown.Option(ExcelTextLoader.get_text(7)),
                dropdown.Option(ExcelTextLoader.get_text(8)),
            ],
            value=EnvironmentVariables.get_language(),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: self.__change_language(page),
        )

    def change_visibility_dropdown_language(self):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        if not self.visible:
            self.visible = True
            self.appbar.change_height(114)

            self.icon_language.change_offset(offset_x=6.50, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)

            return self.page.update(self, self.appbar)

        self.visible = False
        self.icon_language.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_contact.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)

        return self.page.update(self, self.appbar)

    def __change_language(self, page):
        """
        Change the language of the app, update the texts of the app and update the environment variable to the chosen language
        """

        if self.value in ["Spanish", "Español"]:
            EnvironmentVariables.set_language(language="Español", page=page)

        else:
            EnvironmentVariables.set_language(language="English", page=page)

        self.visible = False

        self.options = [
            dropdown.Option(ExcelTextLoader.get_text(7)),
            dropdown.Option(ExcelTextLoader.get_text(8)),
        ]
        self.value = EnvironmentVariables.get_language()

        self.input_url.change_placeholder(ExcelTextLoader.get_text(14))
        self.input_directory.change_placeholder(ExcelTextLoader.get_text(15))

        self.close_dialog.update_title_dialog(ExcelTextLoader.get_text(12))

        self.close_dialog.update_content_dialog(ExcelTextLoader.get_text(3))

        self.button_exit_the_app.change_text(ExcelTextLoader.get_text(4))

        self.dropdown_contact.change_placeholder(ExcelTextLoader.get_text(16))

        self.icon_language.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_contact.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)

        return self.page.update(
            self.appbar,
            self.input_url,
            self.input_directory,
            self,
            self.dropdown_contact,
            self.button_exit_the_app,
            self.close_dialog,
        )

    def get_visibility(self):
        """
        Returns the visibility state of the dropdown.

        :return: Returns the value of the attribute `visible`.
        """

        return self.visible
