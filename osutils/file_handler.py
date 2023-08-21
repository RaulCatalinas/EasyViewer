"""
Controls the logic that is responsible for interacting with the user's OS files
"""

# Standard library
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
    ):
        """
        Delete a file from the user's PC

        Args:
            path_to_file (str): Location of the file to delete
            download_name (str): File name to delete
            callback (Callable, optional): Action to be executed after deleting the file

        Raises:
            OSError: Error occurred during file deletion
        """

        # Utils
        from utils import LoggingManagement

        try:
            remove(f"{path_to_file}/{download_name}")

            callback()

        except OSError as error:
            LoggingManagement.write_error(str(error))

            raise OSError(
                f"Unable to delete file {download_name} at {path_to_file}"
            ) from error

    @classmethod
    def clean_invalid_chars(cls, title: str):
        """
        Remove invalid characters from a string

        Args:
            title (str): Title to clean from invalid characters

        Returns:
            str: The title without invalid characters based on the user's OS
        """

        # Constants
        from constants import INVALID_CHARS, SYSTEM_NAME

        invalid_chars = INVALID_CHARS[SYSTEM_NAME]

        return sub(invalid_chars, "", sub(r"\.$", "", title)).strip()

    @classmethod
    def check_file_exists(cls, file_path: str | Path):
        """
        Check that a file exists

        Args:
            file_path (str | Path): Path to the file to check

        Raises:
            FileNotFoundError: Error that the file doesn't exist at the given path
        """

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Config file not found at {file_path}")
