"""
Gets the path to a directory or to a file
"""

from pathlib import Path


class GetPaths:
    """
    Gets the path to a directory or to a file
    """

    @classmethod
    def get_desktop_path(cls):
        """
        Returns the path to the user's desktop.

        :return: The path to the user's desktop.
        """

        from utils import DESKTOP_PATH

        return DESKTOP_PATH

    @classmethod
    def get_icon_path(cls):
        """
        Returns the path to the icon in the appropriate format based on the operating system.

        :param relative_root_path: The relative path to the root folder (optional)

        :return: The path to the icon is returned in the appropriate format depending on the operating system. On macOS, the icon is returned in ICNS format; on Windows, in ICO format; and on Linux, in the original format (PNG).
        """

        from utils import SYSTEM_NAME, ICONS

        if SYSTEM_NAME not in ICONS:
            raise ValueError("Unsupported operating system")

        return ICONS[SYSTEM_NAME]

    @classmethod
    def get_config_file(cls, config_file: str):
        """
        Returns a configuration file based on the input string parameter.

        :param config_file: config_file is a string parameter that represents the name of the configuration file that needs to be retrieved

        :return: The path to the configuration file
        """

        from utils import CONFIG_FILES

        if config_file.upper() not in CONFIG_FILES:
            raise ValueError("Configuration file doesn't exist")

        return CONFIG_FILES[config_file.upper()]

    @classmethod
    def get_project_root_path(cls):
        """
        Gets the path to the root of the project.
        
        :return: The path to the root of the project.
        """

        current_dir = Path(__file__).resolve()

        return current_dir.parent.parent
