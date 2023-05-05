from enum import Enum
from pathlib import Path
from platform import system


class Paths(Enum):
    DESKTOP = Path.home().joinpath("Desktop")
    CONFIG_FOLDER = Path("../config").resolve()
    ICON_FOLDER = Path("../icon").resolve()


class ConfigFiles(Enum):
    INI = Paths.CONFIG_FOLDER.value.joinpath("control_variables.ini")
    JSON = Paths.CONFIG_FOLDER.value.joinpath("config.json")
    EXCEL = Paths.CONFIG_FOLDER.value.joinpath("languages.xlsx")
    ENV = Paths.CONFIG_FOLDER.value.joinpath(".env")


class Icons(Enum):
    WINDOWS = Paths.ICON_FOLDER.value.joinpath("icon-Windows.ico")
    MACOS = Paths.ICON_FOLDER.value.joinpath("icon-macOS.icns")
    LINUX = Paths.ICON_FOLDER.value.joinpath("icon-Linux.png")


class InvalidChars(Enum):
    WINDOWS = r'[<>:/\\"|?*]'
    MACOS = r"[:/]"
    LINUX = r"[/]"


class System(Enum):
    NAME = system()
