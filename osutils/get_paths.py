"""
Gets the path to a directory or file
"""

from utils import Paths, Icons, System


class GetPaths:
    @classmethod
    def get_desktop_path(cls):
        """
        Returns the path to the user's desktop.

        :return: The path to the user's desktop.
        """

        return Paths.DESKTOP.value

    @classmethod
    def get_icon_path(cls):
        """
        Returns the path to the icon in the appropriate format based on the operating system.

        :param relative_root_path: The relative path to the root folder (optional)

        :return: The path to the icon is returned in the appropriate format depending on the operating system. On macOS, the icon is returned in ICNS format; on Windows, in ICO format; and on Linux, in the original format (PNG).
        """

        system_name = System.NAME.value

        icons_dict = {
            "Windows": Icons.WINDOWS.value,
            "Darwin": Icons.MACOS.value,
            "Linux": Icons.LINUX.value,
        }

        if system_name not in icons_dict:
            raise ValueError("Unsupported operating system")

        return icons_dict[system_name]
