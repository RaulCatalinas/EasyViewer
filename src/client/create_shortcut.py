"""
Creates shortcuts
"""

from pyshortcuts import make_shortcut

from get_paths import get_icon_path


def create_shortcut(target_file_path: str) -> None:
    """
    Creates a shortcut to a file on the desktop for both Windows and Unix operating systems.

    :param target_file_path: The path of the file that the shortcut will point to

    :type target_file_path: str
    """

    make_shortcut(
        target_file_path,
        terminal=False,
        executable=target_file_path,
        icon=get_icon_path(),
    )
