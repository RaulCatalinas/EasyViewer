"""Control the logic to be able to change the language of the app"""

from flet import Dropdown, dropdown, alignment

from app_settings import AppSettings


class ChangeLanguage(Dropdown, AppSettings):
    """Allows the user to change the language of the app"""

    def __init__(
        self,
        appbar,
        page,
        input_url,
        input_directory,
        title_dialog,
        content_dialog,
        button_exit_the_app,
        dropdown_contact,
    ):
        self.appbar = appbar
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.title_dialog = title_dialog
        self.content_dialog = content_dialog
        self.button_exit_the_app = button_exit_the_app
        self.dropdown_contact = dropdown_contact

        AppSettings.__init__(self)

    def _build(self):
        return Dropdown.__init__(
            self,
            options=[
                dropdown.Option(self.get_config_excel(7)),
                dropdown.Option(self.get_config_excel(8)),
            ],
            value=self.get_language(),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: self.__change_language(),
        )

    def change_visibility_dropdown_language(self):
        """Show or hide the dropdown if it is hidden or not respectively"""

        if not self.visible:
            self.visible = True
            self.appbar.toolbar_height = 114
            return self.page.update(self, self.appbar)

        self.visible = False

        if not self.dropdown_contact.visible:
            self.appbar.toolbar_height = 63
            return self.page.update(self, self.appbar)

        return self.page.update(self)

    def __change_language(self):
        """Change the language of the app, update the texts of the app and update the environment variable to the chosen language"""

        if self.value in ["Spanish", "Español"]:
            self.set_language("Español")

        else:
            self.set_language("English")

        self.visible = False

        self.options = [
            dropdown.Option(self.get_config_excel(7)),
            dropdown.Option(self.get_config_excel(8)),
        ]
        self.value = self.get_language()

        self.input_url.change_placeholder(self.get_config_excel(14))
        self.input_directory.change_placeholder(self.get_config_excel(15))
        self.title_dialog.change_text(self.get_config_excel(12))
        self.content_dialog.change_text(self.get_config_excel(3))
        self.button_exit_the_app.change_text_button(self.get_config_excel(4))
        self.dropdown_contact.hint_text = self.get_config_excel(16)

        if not self.dropdown_contact.visible:
            self.appbar.toolbar_height = 63

            return self.page.update(
                self.appbar,
                self.input_url,
                self.input_directory,
                self.title_dialog,
                self.content_dialog,
                self.button_exit_the_app,
                self,
                self.dropdown_contact,
            )

        return self.page.update(
            self.input_url,
            self.input_directory,
            self.title_dialog,
            self.content_dialog,
            self.button_exit_the_app,
            self,
            self.dropdown_contact,
        )
