from flet import AppBar, icons, Dropdown, dropdown, Column, Offset, alignment

from app_settings import AppSettings
from client.create_buttons import CreateIconButton


class TaskBar(AppBar, AppSettings):
    def __init__(
        self,
        page,
        input_url,
        input_directory,
        update_dialog,
        button_exit_the_app,
        content_dialog,
        title_dialog,
    ):
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.update_dialog = update_dialog
        self.title_dialog = title_dialog
        self.content_dialog = content_dialog
        self.button_exit_the_app = button_exit_the_app

        AppSettings.__init__(self)

        self.icon_theme = CreateIconButton(
            icon_button=self.__set_initial_icon_theme(),
            function=lambda e: self.__change_theme(),
        )

        self.icon_language = CreateIconButton(
            icon_button=icons.LANGUAGE,
            function=lambda e: self.__change_visibility_dropdown_language(),
            offset_button=Offset(0, 0.3),
        )

        self.dropdown_language = Dropdown(
            options=[
                dropdown.Option(self.get_config_excel(7)),
                dropdown.Option(self.get_config_excel(8)),
            ],
            value=self.get_language(),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: self.__change_language(),
        )

    def __change_theme(self):
        if self.page.theme_mode == "dark":
            self.page.theme_mode = "light"
            self.icon_theme.icon = icons.DARK_MODE
            self.page.client_storage.set("theme", "light")
            self.page.update()

        else:
            self.page.theme_mode = "dark"
            self.icon_theme.icon = icons.LIGHT_MODE
            self.page.client_storage.set("theme", "dark")
            self.page.update()

    def __set_initial_icon_theme(self):
        if self.page.theme_mode == "light":
            return icons.DARK_MODE

        return icons.LIGHT_MODE

    def __change_visibility_dropdown_language(self):
        if not self.dropdown_language.visible:
            self.dropdown_language.visible = True
            self.toolbar_height = 114
            return self.page.update(self.dropdown_language, self)

        self.dropdown_language.visible = False
        self.toolbar_height = 63
        return self.page.update(self.dropdown_language, self)

    def __change_language(self):
        if self.dropdown_language.value in ["Spanish", "Español"]:
            self.set_language("Español")

        else:
            self.set_language("English")

        self.dropdown_language.visible = False
        self.toolbar_height = 63

        self.dropdown_language.options = [
            dropdown.Option(self.get_config_excel(7)),
            dropdown.Option(self.get_config_excel(8)),
        ]
        self.dropdown_language.value = self.get_language()

        self.input_url.change_placeholder(self.get_config_excel(14))
        self.input_directory.change_placeholder(self.get_config_excel(15))
        self.title_dialog.change_text(self.get_config_excel(12))
        self.content_dialog.change_text(self.get_config_excel(3))
        self.button_exit_the_app.change_text_button(self.get_config_excel(4))

        return self.page.update()

    def _build(self):
        return AppBar.__init__(
            self,
            actions=[
                self.icon_theme,
                Column(controls=[self.icon_language, self.dropdown_language]),
            ],
            toolbar_height=63,
        )
