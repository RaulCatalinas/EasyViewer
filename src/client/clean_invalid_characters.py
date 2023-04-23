"""
Removes invalid characters
"""

from platform import system
from re import sub


def clean_invalid_characters(title: str) -> str:
    """
    Removes invalid characters from a given string, with different invalid characters depending on the operating system.

    :param title: A string representing the title of the file

    :type title: str

    :return: A string that has been cleaned of any invalid characters based on the operating system.
    """

    OS = system()

    invalid_chars_dict = {
        "Windows": r'[<>:/\\"|?*]',
        "Darwin": r"[:/]",
        "Linux": r"[/]",
    }

    invalid_chars = invalid_chars_dict[OS]

    clean_name = sub(invalid_chars, "", sub(r"\.$", "", title)).strip()

    return clean_name
