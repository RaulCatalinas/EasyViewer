"""
Controls theme change logic
"""

from threading import Thread, Lock

from flet import icons, Page, IconButton

from utils import check_type


class ChangeTheme:
    """
    Controls theme change logic
    """

    LOCK = Lock()

    @classmethod
    @check_type
    def change_theme(cls, page: Page, icon_theme: IconButton):
        """
        If the theme is dark, change it to light and vice versa

        :param page: Is a reference to the app window

        :param icon_theme: The icon that will be changed when the theme is changed
        """

        if page.theme_mode == "dark":
            page.theme_mode = "light"
            icon_theme.icon = icons.DARK_MODE
            cls.__save_theme(page=page, theme="light")

        else:
            page.theme_mode = "dark"
            icon_theme.icon = icons.LIGHT_MODE
            cls.__save_theme(page=page, theme="dark")

        return page.update()

    @classmethod
    @check_type
    def set_initial_icon_theme(cls, page: Page):
        """
        Sets the button's initial icon based on the app's theme
        """

        if page.theme_mode == "light":
            return icons.DARK_MODE

        return icons.LIGHT_MODE

    @classmethod
    @check_type
    def __save_theme(cls, page: Page, theme: str) -> None:
        """
        Saves the theme selected by the user
        """

        with cls.LOCK:
            Thread(
                target=page.client_storage.set,
                args=["theme", theme],
                daemon=False,
            ).start()

    @classmethod
    @check_type
    def get_theme(cls, page: Page):
        """
        Returns the theme saved in the frontend storage.

        :param page: Is a reference to the app window

        :return: The value of the "theme" key from the frontend storage.
        """

        return page.client_storage.get("theme")

    @classmethod
    @check_type
    def set_initial_theme(cls, page: Page):
        """
        Sets the default theme and saves it.

        :param page: It's a reference to the application window, for which the default theme is set (light theme).
        """

        theme_for_the_app = cls.get_theme(page) or "light"

        cls.__save_theme(page=page, theme=theme_for_the_app)
