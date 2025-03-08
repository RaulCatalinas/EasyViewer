# Standard library
from json import dump
from os.path import join
from os import remove
from re import sub
from typing import Callable

# App Logging
from app_logging import LoggingManager

# App enums
from app_enums import LogLevels

# Constants
from constants import INVALID_CHARS, SYSTEM_NAME

logging_manager = LoggingManager()


def create_empty_json_file(file_path: str, file_name: str):
    """
    Create a JSON file

    Args:
        file_name (str): Name of the file to be created without the extension.
        file_path (str): Directory where the file will be created
    """

    file_path = join(file_path, file_name)

    with open(f"{file_path}.json", mode="a", encoding="utf-8") as f:
        dump({}, f)


def delete_file(
    path_to_file: str, file_name: str, on_delete_callback: Callable = lambda: ()
):
    """
    Delete a file from the user's PC

    Args:
        path_to_file (str): Location of the file to delete
        file_name (str): File name to delete
        callback (Callable, optional): Action to be executed after deleting the file

    Raises:
        OSError: Error occurred during file deletion
    """

    try:
        remove(f"{path_to_file}/{file_name}")

        on_delete_callback()

    except OSError as e:
        logging_manager.write_log(LogLevels.ERROR, str(e))

        raise OSError(f"Unable to delete file {file_name} at {path_to_file}")


def clean_invalid_chars(title: str):
    """
    Remove invalid characters from a string

    Args:
        title (str): Title to clean from invalid characters

    Returns:
        str: The title without invalid characters based on the user's OS
    """

    invalid_chars = INVALID_CHARS[SYSTEM_NAME]

    return sub(invalid_chars, "", sub(r"\.$", "", title)).strip()
