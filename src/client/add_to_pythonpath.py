"""Add the necessary paths to the pythonpath"""

import os
import sys

SRC_PATH = os.path.abspath("../../src")
CONFIG_PATH = os.path.abspath("../../config")

APP_LOGIC = os.path.abspath("../app_logic")
CLIENT_PATH = os.path.abspath("../client")


print(
    f"""
    {SRC_PATH = }
    {CONFIG_PATH = }
    
    {APP_LOGIC = }
    {CLIENT_PATH = }
    """
)


def add_to_pythonpath():
    """Add the necessary paths to the pythonpath"""

    for path in [SRC_PATH, CONFIG_PATH, APP_LOGIC, CLIENT_PATH]:
        if path not in sys.path:
            sys.path.insert(0, path)
            print(f"{path} added to sys.path")
        else:
            print(f"{path} already in sys.path")

    return print()
