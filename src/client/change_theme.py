"""
Controls theme change logic
"""

from threading import Thread, Lock

from flet import icons


class ChangeTheme:
    """
    Controls theme change logic
    """

    def __init__(self):
        self.lock = Lock()

    def change_theme(self, page, icon_theme):
        """
        If the theme is dark, change it to light and vice versa

        :param page: Is a reference to the app window

        :param icon_theme: The icon that will be changed when the theme is changed
        """

        if page.theme_mode == "dark":
            page.theme_mode = "light"
            icon_theme.icon = icons.DARK_MODE
            self.__save_theme(page=page, theme="light")

        else:
            page.theme_mode = "dark"
            icon_theme.icon = icons.LIGHT_MODE
            self.__save_theme(page=page, theme="dark")

        return page.update()

    def set_initial_icon_theme(self, page):
        """
        Sets the button's initial icon based on the app's theme
        """

        if page.theme_mode == "light":
            return icons.DARK_MODE

        return icons.LIGHT_MODE

    def __save_theme(self, page, theme: str) -> None:
        """
        Saves the theme selected by the user
        """

        with self.lock:
            Thread(
                target=page.client_storage.set, args=["theme", theme], daemon=False
            ).start()

    def get_theme(self, page):
        """
        Returns the theme saved in the client storage.

        :param page: Is a reference to the app window

        :return: The value of the "theme" key from the client storage.
        """

        return page.client_storage.get("theme")

    def set_default_theme(self, page):
        """
        Sets the default theme and saves it.

        :param page: It's a reference to the application window, for which the default theme is set (light theme).
        """

        self.__save_theme(page=page, theme="light")
