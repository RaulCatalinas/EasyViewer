"""Build the app"""

from subprocess import run, CalledProcessError

from utils import ENABLED_TYPE_CHECKING

__version__ = "2.1.0"


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
        "icon/icon.png",
        "--product-name",
        "EasyViewer",
        "--file-description",
        "App to download youtube videos",
        "--file-version",
        __version__,
        "--product-version",
        __version__,
        "--copyright",
        '"Copyright (c) 2023 Raul Catalinas Esteban"',
        "--add-data",
        "config;config",
        "--add-data",
        "icon;icon",
        "--add-data",
        "src;src",
        "--add-data",
        "control;control",
        "--add-data",
        "osutils;osutils",
        "--add-data",
        "utils;utils",
        "--add-data",
        "pyproject.toml;pyproject.toml",
        "--add-data",
        "github_credentials.py;github_credentials.py",
    ]

    try:
        run(command, capture_output=True, check=True)

    except CalledProcessError as e:
        print(f"Could not compile, this is the reason: {e.stderr.decode()}")

    else:
        print("App compiled successfully")


build()
