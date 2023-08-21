"""
Gets the path to a directory or to a file
"""

# Standard library
from pathlib import Path


class GetPaths:
    """
    Gets the path to a directory or to a file
    """

    @staticmethod
    def get_desktop_path():
        """
        Gets the path to the user's desktop

        Returns:
            Path: The path to the user's desktop.
        """

        from constants import DESKTOP_PATH

        return DESKTOP_PATH

    @staticmethod
    def get_config_file(config_file: str):
        """
        Gets the configuration file

        Args:
            config_file (str): Configuration file to get

        Raises:
            ValueError: The configuration file doesn't exist

        Returns:
            Path: The path to the configuration file
        """

        from constants import CONFIG_FILES

        if config_file.upper() not in CONFIG_FILES:
            raise ValueError("Configuration file doesn't exist")

        return CONFIG_FILES[config_file.upper()]

    @staticmethod
    def get_project_root_path():
        """
        Gets the path to the root of the project.

        Returns:
            Path: The path to the root of the project.
        """

        current_dir = Path(__file__).resolve()

        return current_dir.parent.parent

    @staticmethod
    def get_user_home_path():
        """
        Gets the path of the user's home directory.

        Returns:
            Path: The home directory path of the user.
        """

        return Path.home()
