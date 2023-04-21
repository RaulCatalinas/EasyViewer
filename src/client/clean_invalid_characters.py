"""
Removes invalid characters
"""

from platform import system
from re import sub

OS = system()


def clean_invalid_characters(title: str) -> str:
    """
    Removes invalid characters from a given string, with different invalid characters depending on the operating system.

    :param title: A string representing the title of the file

    :type title: str

    :return: A string that has been cleaned of any invalid characters based on the operating system.
    """

    name_without_period = sub(r"\.$", "", title)

    if OS == "Windows":
        invalid_chars = r"[<>:/\\|?*]"

    elif OS == "Darwin":
        invalid_chars = r"[:/]"

    elif OS == "Linux":
        invalid_chars = r"[/]"

    clean_name = sub(invalid_chars, "", name_without_period)

    return clean_name.strip()
