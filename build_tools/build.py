"""Build the app"""

# Standard library
from subprocess import CalledProcessError, run

# Constants
from constants import ENABLED_TYPE_CHECKING, USER_VERSION


def build():
    """Generate the application executable"""

    ADD_DATA_COMMAND = "--add-data"
    SRC_FOLDER = "src"

    if not ENABLED_TYPE_CHECKING:
        print("Type checking off")

    command = [
        "flet",
        "pack",
        f"{SRC_FOLDER}/main.py",
        "-n",
        "EasyViewer",
        "-i",
        "build_tools/icon/icon.png",
        "--product-name",
        "EasyViewer",
        "--file-description",
        "App to download YouTube videos",
        "--file-version",
        USER_VERSION,
        "--product-version",
        USER_VERSION,
        "--copyright",
        "Copyright (c) 2023 Raul Catalinas Esteban",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/backend;backend",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/components;components",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/constants;constants",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/control_variables;control_variables",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/frontend;frontend",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/osutils;osutils",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/settings;settings",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/settings_files;settings_files",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/utils;utils",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/github_credentials.py;github_credentials.py",
    ]

    try:
        run(command, capture_output=True, check=True)

    except CalledProcessError as e:
        print(f"Could not compile, this is the reason: {e.stderr.decode()}")

    else:
        print("App compiled successfully")


build()
