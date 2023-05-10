"""
Controls the logic that is responsible for interacting with the user's OS files
"""

from os import remove
from pathlib import Path
from re import sub
from typing import Callable


class FileHandler:
    """
    Controls the logic that is responsible for interacting with the user's OS files
    """

    @classmethod
    def delete_file(
        cls,
        path_to_file: str,
        download_name: str,
        callback: Callable = lambda: None,
    ) -> None:
        """
        Deletes a file at a given path and raises an error if it fails.

        :param path_to_file: A string representing the path to the directory where the file to be deleted is located

        :param download_name: The name of the file to be deleted

        :param callback: Is a function that is executed after the file is successfully deleted. It is an optional parameter and by default, it's set to a lambda function that does nothing. This parameter can be used to perform any additional actions after the file is deleted
        """

        from utils import LoggingManagement

        try:
            remove(f"{path_to_file}/{download_name}")

            callback()

        except OSError as error:
            LoggingManagement.write_error(error)

            raise OSError(
                f"Unable to delete file {download_name} at {path_to_file}"
            ) from error

    @classmethod
    def clean_invalid_chars(cls, title: str) -> str:
        """
        Removes invalid characters from a given string, with different invalid characters depending on the operating system.

        :param title: A string representing the title of the file

        :return: A string that has been cleaned of any invalid characters based on the operating system.
        """

        from utils import INVALID_CHARS, SYSTEM_NAME

        invalid_chars = INVALID_CHARS[SYSTEM_NAME]

        return sub(invalid_chars, "", sub(r"\.$", "", title)).strip()

    @classmethod
    def check_file_exists(cls, file_path: str | Path):
        """
        Checks if a file exists at a given file path and raises a FileNotFoundError if it does not.

        :param file_path: Is a string or Path object that represents the path to a file that needs to be checked for existence
        """

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Config file not found at {file_path}")
