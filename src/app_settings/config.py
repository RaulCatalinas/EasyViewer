from enum import Enum, StrEnum


class WindowSettings(Enum):
    TITLE = "EasyViewer"
    WIDTH = 830
    HIGH = 575
    PREVENT_CLOSE = True
    RESIZABLE = False
    MAXIMIZABLE = False


class AppColors(StrEnum):
    PROGRESS_BAR_COLOR = "00FF00"
    APP_BAR_BG_COLOR_THEME_DARK = "#191e25"
    APP_BAR_BG_COLOR_THEME_LIGHT = "#cfd2e3"
