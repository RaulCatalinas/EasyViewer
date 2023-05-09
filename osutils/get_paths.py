"""
Gets the path to a directory or to a file
"""

from utils import PATHS, SYSTEM_NAME, ICONS


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

        return PATHS["DESKTOP"]

    @classmethod
    def get_icon_path(cls):
        """
        Returns the path to the icon in the appropriate format based on the operating system.

        :param relative_root_path: The relative path to the root folder (optional)

        :return: The path to the icon is returned in the appropriate format depending on the operating system. On macOS, the icon is returned in ICNS format; on Windows, in ICO format; and on Linux, in the original format (PNG).
        """

        if SYSTEM_NAME not in ICONS:
            raise ValueError("Unsupported operating system")

        return ICONS[SYSTEM_NAME]
