# Osutils
from osutils import GetPaths

ROOT_PATH = GetPaths.get_project_root_path()

USER_HOME = GetPaths.get_user_home_path()

DESKTOP_PATH = USER_HOME.joinpath("Desktop")

CONFIG_FILES = {
    "INI": ROOT_PATH.joinpath("settings_files/control_variables.ini"),
    "JSON": ROOT_PATH.joinpath("settings_files/settings.json"),
    "EXCEL": ROOT_PATH.joinpath("settings_files/languages.xlsx"),
    "ENV": ROOT_PATH.joinpath("settings_files/.env"),
}
