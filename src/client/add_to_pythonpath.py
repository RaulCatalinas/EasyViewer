"""Add the necessary paths to the pythonpath"""

from os.path import abspath
from sys import path


def add_to_pythonpath():
    """Add the necessary paths to the pythonpath"""

    PATHS_TO_ADD = [
        abspath("../../src"),
        abspath("../../config"),
        abspath("../app_logic"),
        abspath("../client"),
    ]

    for path_to_add in PATHS_TO_ADD:
        if path_to_add not in path:
            path.insert(0, path_to_add)
            print(f"{path_to_add} added to Pythonpath")
        else:
            print(f"{path_to_add} already in Pythonpath")

    print()
