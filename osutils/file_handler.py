"""
Deletes a file at a specified
"""

from os import remove
from re import sub

from control import WriteControlVariables
from utils import check_type, InvalidChars, System


class FileHandler:
    @classmethod
    def delete_file(cls, path_to_the_file: str, download_name: str):
        """
        Deletes a file at a specified path.

        :param path_to_the_file: The path to the directory where the file is located

        :param download_name: The name of the file that needs to be deleted

        :param reset: Function that will be called after the file deletion is attempted, regardless of  whether the deletion was successful or not, it's used to reset any variables that may ave been affected by the  file deletion
        """

        check_type(path_to_the_file, str)
        check_type(download_name, str)

        try:
            remove(f"{path_to_the_file}/{download_name}")

        finally:
            WriteControlVariables.reset()

    @classmethod
    def clean_invalid_chars(cls, title: str) -> str:
        """
        Removes invalid characters from a given string, with different invalid characters depending on the operating system.

        :param title: A string representing the title of the file

        :type title: str

        :return: A string that has been cleaned of any invalid characters based on the operating system.
        """

        check_type(title, str)

        invalid_chars_dict = {
            "Windows": InvalidChars.WINDOWS.value,
            "Darwin": InvalidChars.MACOS.value,
            "Linux": InvalidChars.LINUX.value,
        }

        invalid_chars = invalid_chars_dict[System.NAME.value]

        return sub(invalid_chars, "", sub(r"\.$", "", title)).strip()
