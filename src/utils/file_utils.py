from json import dump
from os.path import join


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
