# Standard library
from pathlib import Path
from os import startfile
from subprocess import run
from typing import Callable, Union

# Constants
from constants import SYSTEM_NAME


def verify_download_directory(directory: str) -> bool:
    """
    Verifies if the given directory exists.

    Args:
        directory (str): Path to check.

    Returns:
        bool: True if directory exists, False otherwise.
    """

    directory_path = Path(directory)

    return directory_path.exists() and directory_path.is_dir()


def open_directory(directory: Union[str, Path]):
    """
    Opens the given directory in the system's file explorer.

    Args:
        directory (str | Path): The directory path to open.
    """

    open_directory_function_dict: dict[str, Callable] = {
        "Windows": lambda: startfile(directory),
        "Darwin": lambda: run(["open", directory], check=True),
        "Linux": lambda: run(["xdg-open", directory], check=True),
    }

    if SYSTEM_NAME in open_directory_function_dict.keys():
        open_directory_function_dict[SYSTEM_NAME]()

        return

    raise RuntimeError("Unsupported operating system")
