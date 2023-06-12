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

    @classmethod
    def get_user_home_path(cls):
        """
        Get the home directory path of the user.

        :return: The home directory path of the user.
        """
        return Path.home()
