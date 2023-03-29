"""Controls theme change logic"""

from flet import icons


class ChangeTheme:
    """It changes the theme of the page and sets the icon of the button to the opposite of the current theme"""

    def change_theme(self, page, icon_theme):
        """
        If the theme is dark, change it to light and vice versa

        :param page: The page that the user is currently on
        :param icon_theme: The icon that will be changed when the theme is changed
        """
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            icon_theme.icon = icons.DARK_MODE
            page.client_storage.set("theme", "light")
            page.update()

        else:
            page.theme_mode = "dark"
            icon_theme.icon = icons.LIGHT_MODE
            page.client_storage.set("theme", "dark")
            page.update()

    def set_initial_icon_theme(self, page):
        """Sets the button's initial icon based on the app's theme"""
        if page.theme_mode == "light":
            return icons.DARK_MODE

        return icons.LIGHT_MODE
