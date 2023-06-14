"""
Control the logic to be able to contact the developer
"""

from webbrowser import open_new_tab

from flet import Dropdown, Page, IconButton, AppBar

from frontend import ContactUI
from utils import check_type


class Contact(ContactUI):
    """
    Control the logic to be able to contact the developer
    """

    @check_type
    def __init__(
        self,
        dropdown_language: Dropdown,
        page: Page,
        appbar: AppBar,
        icon_contact: IconButton,
        icon_theme: IconButton,
    ):
        self.dropdown_language = dropdown_language
        self.page = page
        self.appbar = appbar
        self.icon_contact = icon_contact
        self.icon_theme = icon_theme

        self.social_networks = {
            "Facebook": "https://www.facebook.com/profile.php?id=100063559000286",
            "Instagram": "https://www.instagram.com/raulf1foreveryt_oficial",
            "Twitter": "https://twitter.com/F1foreverRaul",
            "GitHub": "https://github.com/RaulCatalinas",
        }

        super().__init__(
            dropdown_language=self.dropdown_language,
            page=page,
            icon_theme=self.icon_theme,
            icon_contact=self.icon_contact,
            callback=self.__contact,
        )

    def __contact(self):
        """
        Opens the selected social network in a new browser tab
        """

        self.selected_social_network = self.value
        open_new_tab(self.social_networks[self.selected_social_network])

        self.visible = False

        self.icon_contact.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_language.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)

        return self.page.update(self, self.appbar)
