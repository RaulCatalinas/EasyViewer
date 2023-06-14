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
        Changes the app's theme between dark and light mode.

        :param page: A reference to the app window.
        :param icon_theme: The icon that will be updated when the theme is changed.
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
        Sets the initial icon theme based on the app's current theme mode.

        :param page: A reference to the app window.
        :return: The icon representing the initial theme.
        """

        return icons.DARK_MODE if page.theme_mode == "light" else icons.LIGHT_MODE

    @classmethod
    @check_type
    def __save_theme(cls, page: Page, theme: str) -> None:
        """
        Saves the selected theme to the frontend storage.

        :param page: A reference to the app window.
        :param theme: The theme to be saved.
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
        Retrieves the saved theme from the frontend storage.

        :param page: A reference to the app window.
        :return: The value of the "theme" key from the frontend storage.
        """

        return page.client_storage.get("theme")

    @classmethod
    @check_type
    def set_initial_theme(cls, page: Page):
        """
        Sets the initial theme for the app and saves it.

        :param page: A reference to the app window.
        """

        theme_for_the_app = cls.get_theme(page) or "light"
        cls.__save_theme(page=page, theme=theme_for_the_app)
