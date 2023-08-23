"""Build the app"""

# Standard library
from subprocess import CalledProcessError, run

# Constants
from constants import ENABLED_TYPE_CHECKING, USER_VERSION


def build():
    """Generate the application executable"""

    if not ENABLED_TYPE_CHECKING:
        print("Type checking off")

    command = [
        "flet",
        "pack",
        "src/main.py",
        "-n",
        "EasyViewer",
        "-i",
        "build_tools/icon/icon.png",
        "--product-name",
        "EasyViewer",
        "--file-description",
        "App to download youtube videos",
        "--file-version",
        USER_VERSION,
        "--product-version",
        USER_VERSION,
        "--copyright",
        "Copyright (c) 2023 Raul Catalinas Esteban",
        "--add-data",
        "build_tools/;build_tools",
        "--add-data",
        "src;src",
    ]

    try:
        run(command, capture_output=True, check=True)

    except CalledProcessError as e:
        print(f"Could not compile, this is the reason: {e.stderr.decode()}")

    else:
        print("App compiled successfully")


build()
