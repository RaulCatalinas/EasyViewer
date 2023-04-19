"""
Control the logic to be able to change the language of the app
"""

from flet import Dropdown, dropdown, alignment, Offset

from app_settings import AppSettings


class ChangeLanguage(Dropdown, AppSettings):
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
        icon_update,
        update_dialog,
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
        self.update_dialog = update_dialog

        AppSettings.__init__(self)

        Dropdown.__init__(
            self,
            options=[
                dropdown.Option(self.get_config_excel(7)),
                dropdown.Option(self.get_config_excel(8)),
            ],
            value=self.get_language(),
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

            self.icon_language.change_offset(6.50, 0.3)
            self.icon_theme.change_offset(0, -0.65)
            self.icon_update.change_offset(0, -0.63)

            return self.page.update(self, self.appbar)

        self.visible = False
        self.icon_language.change_offset(0, 0.3)

        if not self.dropdown_contact.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(0, 0)
            self.icon_update.change_offset(0, 0)

        return self.page.update(self, self.appbar)

    def __change_language(self, page):
        """
        Change the language of the app, update the texts of the app and update the environment variable to the chosen language
        """

        if self.value in ["Spanish", "Español"]:
            self.set_language(language="Español", page=page)

        else:
            self.set_language(language="English", page=page)

        self.visible = False

        self.options = [
            dropdown.Option(self.get_config_excel(7)),
            dropdown.Option(self.get_config_excel(8)),
        ]
        self.value = self.get_language()

        self.input_url.change_placeholder(self.get_config_excel(14))
        self.input_directory.change_placeholder(self.get_config_excel(15))

        self.close_dialog.update_title_dialog(self.get_config_excel(12))

        self.close_dialog.update_content_dialog(self.get_config_excel(3))

        self.update_dialog.update_title_dialog(self.get_config_excel(21))

        self.button_exit_the_app.change_text_button(self.get_config_excel(4))

        self.dropdown_contact.change_placeholder(self.get_config_excel(16))

        self.icon_language.offset = Offset(0, 0.3)

        if not self.dropdown_contact.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(0, 0)
            self.icon_update.change_offset(0, 0)

        return self.page.update(
            self.appbar,
            self.input_url,
            self.input_directory,
            self,
            self.dropdown_contact,
            self.button_exit_the_app,
            self.close_dialog,
            self.update_dialog,
        )

    def get_visibility(self):
        """
        Returns the visibility state of the dropdown.

        :return: Returns the value of the attribute `visible`.
        """

        return self.visible
