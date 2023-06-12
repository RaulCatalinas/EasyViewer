"""
Control the logic to be able to contact the developer
"""

from webbrowser import open_new_tab

from flet import Dropdown, dropdown, alignment, Page, IconButton, AppBar

from config import ExcelTextLoader
from utils import check_type


class Contact(Dropdown):
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

    def _build(self):
        return Dropdown.__init__(
            self,
            options=[
                dropdown.Option("Facebook"),
                dropdown.Option("Instagram"),
                dropdown.Option("Twitter"),
                dropdown.Option("GitHub"),
            ],
            hint_text=ExcelTextLoader.get_text(16),
            visible=False,
            alignment=alignment.center,
            on_change=lambda e: self.__contact(),
        )

    def change_visibility_dropdown_contact(self):
        """
        Show or hide the dropdown if it's hidden or not respectively
        """

        if not self.visible:
            self.visible = True

            self.appbar.change_height(114)

            self.icon_contact.change_offset(offset_x=6.50, offset_y=0.3)
            self.icon_theme.change_offset(offset_x=0, offset_y=-0.65)

            return self.page.update(self, self.appbar)

        self.visible = False
        self.icon_contact.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_language.get_visibility():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)

        return self.page.update(self, self.appbar)

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

    @check_type
    def change_placeholder(self, new_placeholder: str):
        """
        Changes the placeholder text.

        :param new_placeholder: The new text that will replace the current placeholder text
        """

        self.hint_text = new_placeholder

    def get_visibility(self):
        """
        Returns the visibility state of the dropdown.

        :return: The value of the attribute `visible`.
        """

        return self.visible