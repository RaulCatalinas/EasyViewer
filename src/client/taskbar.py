from webbrowser import open_new_tab

from flet import AppBar, icons, Dropdown, dropdown, Column, Offset, alignment

from app_settings import AppSettings
from client.create_buttons import CreateIconButton


class TaskBar(AppBar, AppSettings):
    def __init__(
        self,
        page,
        input_url,
        input_directory,
        button_exit_the_app,
        content_dialog,
        title_dialog,
    ):
        self.page = page
        self.input_url = input_url
        self.input_directory = input_directory
        self.title_dialog = title_dialog
        self.content_dialog = content_dialog
        self.button_exit_the_app = button_exit_the_app

        AppSettings.__init__(self)

        self.social_networks = {
            "Facebook": "https://www.facebook.com/profile.php?id=100063559000286",
            "Instagram": "https://www.instagram.com/raulf1foreveryt_oficial",
            "Twitter": "https://twitter.com/F1foreverRaul",
            "GitHub": "https://github.com/RaulCatalinas",
        }

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

        self.icon_contact = CreateIconButton(
            icon_button=icons.CONTACTS,
            function=lambda e: self.__change_visibility_dropdown_contact(),
            offset_button=Offset(0, 0.3),
        )

        self.dropdown_contact = Dropdown(
            options=[
                dropdown.Option("Facebook"),
                dropdown.Option("Instagram"),
                dropdown.Option("Twitter"),
                dropdown.Option("GitHub"),
            ],
            hint_text=self.get_config_excel(16),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: self.__contact(),
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

        if not self.dropdown_contact.visible:
            self.toolbar_height = 63
            return self.page.update(self.dropdown_language, self)

        return self.page.update(self.dropdown_language)

    def __change_language(self):
        if self.dropdown_language.value in ["Spanish", "Español"]:
            self.set_language("Español")

        else:
            self.set_language("English")

        self.dropdown_language.visible = False

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
        self.dropdown_contact.hint_text = self.get_config_excel(16)

        if not self.dropdown_contact.visible:
            self.toolbar_height = 63

            return self.page.update(
                self,
                self.input_url,
                self.input_directory,
                self.title_dialog,
                self.content_dialog,
                self.button_exit_the_app,
                self.dropdown_language,
                self.dropdown_contact,
            )

        return self.page.update(
            self.input_url,
            self.input_directory,
            self.title_dialog,
            self.content_dialog,
            self.button_exit_the_app,
            self.dropdown_language,
            self.dropdown_contact,
        )

    def __change_visibility_dropdown_contact(self):
        if not self.dropdown_contact.visible:
            self.dropdown_contact.visible = True
            self.toolbar_height = 114
            return self.page.update(self.dropdown_contact, self)

        self.dropdown_contact.visible = False

        if not self.dropdown_language.visible:
            self.toolbar_height = 63
            return self.page.update(self.dropdown_contact, self)

        return self.page.update(self.dropdown_contact)

    def __contact(self):
        self.dropdown_contact.visible = False

        self.selected_social_network = self.dropdown_contact.value

        if not self.dropdown_language.visible:
            self.toolbar_height = 63
            self.page.update(self, self.dropdown_contact)

        self.page.update(self.dropdown_contact)

        return open_new_tab(self.social_networks[self.selected_social_network])

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
