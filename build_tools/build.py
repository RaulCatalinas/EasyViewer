"""Build the app"""

# Standard library
from subprocess import CalledProcessError, run

# Constants
from constants import ENABLED_TYPE_CHECKING, USER_VERSION, SYSTEM_NAME


def build():
    """Generate the application executable"""

    ADD_DATA_COMMAND = "--add-data"
    SRC_FOLDER = "src"
    SEPARATOR = ";" if SYSTEM_NAME == "win32" else ":"

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
        f"{SRC_FOLDER}/backend{SEPARATOR}backend",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/components{SEPARATOR}components",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/constants{SEPARATOR}constants",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/control_variables{SEPARATOR}control_variables",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/osutils{SEPARATOR}osutils",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/settings{SEPARATOR}settings",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/settings_files{SEPARATOR}settings_files",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/utils{SEPARATOR}utils",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/github_credentials.py{SEPARATOR}github_credentials.py",
        ADD_DATA_COMMAND,
        f"{SRC_FOLDER}/local_storage{SEPARATOR}local_storage",
    ]

    try:
        run(command, capture_output=True, check=True)

    except CalledProcessError as e:
        print(f"Could not compile, this is the reason: {e.stderr.decode()}")

    else:
        print("App compiled successfully")


build()
