"""
Control the logic to be able to contact the developer
"""

# Standard library
from webbrowser import open_new_tab

# Third-Party libraries
from flet import Page

# Components
from components.ui import ContactUI

# Create widgets
from components.widgets import Checkbox, IconButton, TaskBar, Dropdown

# Utils
from utils import check_type

# Constants
from constants import SOCIAL_NETWORKS


class Contact(ContactUI):
    """
    Control the logic to be able to contact the developer
    """

    @check_type
    def __init__(
        self,
        dropdown_language: Dropdown,
        page: Page,
        appbar: TaskBar,
        icon_contact: IconButton,
        icon_theme: IconButton,
        icon_update: IconButton,
        checkbox: Checkbox,
    ):
        self.dropdown_language = dropdown_language
        self.page = page
        self.appbar = appbar
        self.icon_contact = icon_contact
        self.icon_theme = icon_theme
        self.icon_update = icon_update
        self.checkbox = checkbox

        super().__init__(
            appbar=self.appbar,
            dropdown_language=self.dropdown_language,
            page=page,
            icon_theme=self.icon_theme,
            icon_contact=self.icon_contact,
            callback=self.__contact,
            checkbox=self.checkbox,
            icon_update=self.icon_update,
        )

    def __contact(self):
        """
        Opens the selected social network in a new browser tab
        """

        self.selected_social_network = self.value

        if self.selected_social_network is None:
            return

        open_new_tab(SOCIAL_NETWORKS[self.selected_social_network])

        self.icon_contact.change_offset(offset_x=0, offset_y=0.3)

        if not self.dropdown_language.is_visible():
            self.appbar.change_height(63)

            self.icon_theme.change_offset(offset_x=0, offset_y=0)
            self.icon_update.change_offset(offset_x=0, offset_y=0)
            self.checkbox.change_offset(offset_x=0, offset_y=0)

        return self.change_visibility()
