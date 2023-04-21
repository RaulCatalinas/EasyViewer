"""
Gets the path to a directory or file
"""

from pathlib import Path
from platform import system

_home = Path().home()
_OS = system()


def get_desktop_path():
    """
    Returns the path to the user's desktop.

    :return: The path to the user's desktop.
    """

    return _home.joinpath("Desktop")


def __get_folder_icon(relative_root_path):
    """
    Takes a relative root path as input, converts it to an absolute path using the Path
    module, and returns the path to the "icon" folder

    :param relative_root_path: The relative path to the root folder

    :return: Path to the "icon" folder
    """

    root_path = Path(relative_root_path).absolute()

    return root_path.joinpath("icon")


def get_icon_path(relative_root_path: str = "../../"):
    """
    Returns the path to the icon in the appropriate format based on the operating system.

    :param relative_root_path: The relative path to the root folder (optional)

    :return: The path to the icon is returned in the appropriate format depending on the operating system. On macOS, the icon is returned in ICNS format; on Windows, in ICO format; and on Linux, in the original format (PNG).
    """

    folder_icon = __get_folder_icon(relative_root_path)

    if _OS == "Darwin":
        return folder_icon.joinpath("icon-macOS.icns")

    if _OS == "Windows":
        return folder_icon.joinpath("icon-Windows.ico")

    if _OS == "Linux":
        return folder_icon.joinpath("icon-Linux.png")

    return None
