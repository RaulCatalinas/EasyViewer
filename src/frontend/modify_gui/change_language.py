from flet import dropdown

from utils import check_type, ExcelTextLoader, EnvironmentVariables


class ChangeLanguage(LanguageUI):
    """
    Allows the user to change the language of the app
    """

    @check_type
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
        )

    @check_type
    def __change_language(self, page):
        """
        Change the language of the app, update the texts of the app, and update the environment variable to the chosen language.

        :param page: A reference to the app window.
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

        self.close_dialog.update_title(ExcelTextLoader.get_text(12))

        self.close_dialog.update_content(ExcelTextLoader.get_text(3))

        self.button_exit_the_app.change_text(ExcelTextLoader.get_text(4))

        self.dropdown_contact.change_placeholder(ExcelTextLoader.get_text(16))

        self.icon_language.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_contact.is_visible():
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
