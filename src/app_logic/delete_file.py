"""
Deletes a file at a specified
"""

from os import remove


def delete_file(path_to_the_file, download_name, reset):
    """
    Deletes a file at a specified path.

    :param path_to_the_file: The path to the directory where the file is located

    :param download_name: The name of the file that needs to be deleted

    :param reset: Function that will be called after the file deletion is attempted, regardless of  whether the deletion was successful or not, it's used to reset any variables that may ave been affected by the  file deletion
    """

    try:
        remove(f"{path_to_the_file}/{download_name}")

    finally:
        reset()
