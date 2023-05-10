"""
Constants needed for the application
"""

from pathlib import Path
from platform import system

PATHS = {
    "DESKTOP": Path().home().joinpath("Desktop"),
    "CONFIG_FOLDER": Path("../config").resolve(),
    "ICON_FOLDER": Path("./icon").resolve(),
}

CONFIG_FILES = {
    "INI": PATHS["CONFIG_FOLDER"].joinpath("control_variables.ini"),
    "JSON": PATHS["CONFIG_FOLDER"].joinpath("config.json"),
    "EXCEL": PATHS["CONFIG_FOLDER"].joinpath("languages.xlsx"),
    "ENV": PATHS["CONFIG_FOLDER"].joinpath(".env"),
}

ICONS = {
    "Windows": PATHS["ICON_FOLDER"].joinpath("icon-Windows.ico"),
    "Darwin": PATHS["ICON_FOLDER"].joinpath("icon-macOS.icns"),
    "Linux": PATHS["ICON_FOLDER"].joinpath("icon-Linux.png"),
}

INVALID_CHARS = {"Windows": r'[<>:/\\"|?*]', "Darwin": r"[:/]", "Linux": r"[/]"}

SYSTEM_NAME = system()
