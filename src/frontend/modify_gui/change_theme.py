# Standard library
from threading import Lock, Thread

# Third-Party libraries
from flet import Page, ThemeMode, icons

# Utils
from utils import EnumHelper, check_type

# Create widgets
from ..create_widgets import CreateIconButton


class ChangeTheme:
    """
    Controls theme change logic
    """

    LOCK = Lock()
    DARK_MODE = EnumHelper.get_enum_value(ThemeMode.DARK)
    LIGHT_MODE = EnumHelper.get_enum_value(ThemeMode.LIGHT)

    @classmethod
    @check_type
    def change_theme(cls, page: Page, icon_theme: CreateIconButton):
        """
        Changes the app's theme between dark and light mode.

        Args:
            page (flet.Page): Reference to the app window
            icon_theme (IconButton): Button icon to change the theme
        """

        if page.theme_mode == cls.DARK_MODE:
            page.theme_mode = cls.LIGHT_MODE
            icon_theme.icon = icons.DARK_MODE
            cls.__save_theme(page=page, theme=cls.LIGHT_MODE)

        else:
            page.theme_mode = cls.DARK_MODE
            icon_theme.icon = icons.LIGHT_MODE
            cls.__save_theme(page=page, theme=cls.DARK_MODE)

        page.update()

    @classmethod
    @check_type
    def set_initial_icon_theme(cls, page: Page):
        """
        Sets the initial icon theme based on the app's current theme mode.

        Args:
            page(flet.Page): Reference to the app window.

        Returns:
            Literal['dark_mode', 'light_mode']:  The icon representing the initial theme
        """

        return (
            icons.DARK_MODE if page.theme_mode == cls.LIGHT_MODE else icons.LIGHT_MODE
        )

    @classmethod
    @check_type
    def __save_theme(cls, page: Page, theme: str):
        """
        Saves the selected theme to the client storage.

        Args:
            page (flet.Page): Reference to the app window
            theme (str): The theme to be saved
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
        Gets the saved theme from the client storage

        Args:
            page (flet.Page): Reference to the app window.

        Returns:
            Any: The theme saved from the client storage
        """

        return page.client_storage.get("theme")

    @classmethod
    @check_type
    def set_initial_theme(cls, page: Page):
        """
        Sets the initial theme for the app and saves it.

        Args:
            page (flet.Page): Reference to the app window.
        """

        theme_for_the_app = cls.get_theme(page) or cls.LIGHT_MODE
        cls.__save_theme(page=page, theme=theme_for_the_app)
