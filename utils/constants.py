"""
Constants needed for the application
"""

from pathlib import Path
from platform import system

from from_root import from_root

DESKTOP_PATH = Path.home().joinpath("Desktop")

CONFIG_FILES = {
    "INI": from_root("config/control_variables.ini"),
    "JSON": from_root("config/config.json"),
    "EXCEL": from_root("config/languages.xlsx"),
    "ENV": from_root("config/.env"),
}

ICONS = {
    "Windows": from_root("icon/icon-Windows.ico"),
    "Darwin": from_root("icon/icon-macOS.icns"),
    "Linux": from_root("icon/icon-Linux.png"),
}

INVALID_CHARS = {"Windows": r'[<>:/\\"|?*]', "Darwin": r"[:/]", "Linux": r"[/]"}

SYSTEM_NAME = system()

ENABLED_TYPE_CHECKING = True
