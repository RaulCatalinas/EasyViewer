"""Control the logic to be able to contact the developer"""

from webbrowser import open_new_tab

from flet import Dropdown, dropdown, alignment

from app_settings import AppSettings


class Contact(Dropdown, AppSettings):
    """Allows the user to select a social network and then opens a new tab with the selected social network."""

    def __init__(self, dropdown_language, page, appbar):
        self.dropdown_language = dropdown_language
        self.page = page
        self.appbar = appbar

        AppSettings.__init__(self)

        self.social_networks = {
            "Facebook": "https://www.facebook.com/profile.php?id=100063559000286",
            "Instagram": "https://www.instagram.com/raulf1foreveryt_oficial",
            "Twitter": "https://twitter.com/F1foreverRaul",
            "GitHub": "https://github.com/RaulCatalinas",
        }

    def _build(self):
        return Dropdown.__init__(
            self,
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

    def change_visibility_dropdown_contact(self):
        """Show or hide the dropdown if it is hidden or not respectively"""

        if not self.visible:
            self.visible = True
            self.appbar.toolbar_height = 114
            return self.page.update(self, self.appbar)

        self.visible = False

        if not self.dropdown_language.visible:
            self.appbar.toolbar_height = 63
            return self.page.update(self, self.appbar)

        return self.page.update(self)

    def __contact(self):
        """Opens the selected social network in a new browser tab"""

        self.selected_social_network = self.value
        open_new_tab(self.social_networks[self.selected_social_network])

        self.visible = False

        if not self.dropdown_language.visible:
            self.appbar.toolbar_height = 63
            return self.page.update(self, self.appbar)

        return self.page.update(self)
