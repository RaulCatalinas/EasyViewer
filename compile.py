"""Build the app"""

from subprocess import run

from osutils import GetPaths
from utils import ENABLED_TYPE_CHECKING

__version__ = "2.0.0"


def compile_app():
    """Compile the app to generate the executable file"""

    if not ENABLED_TYPE_CHECKING:
        print("Type checking off")

    icon = GetPaths.get_icon_path()

    COMMAND = f"""flet pack src/main.py -n EasyViewer -i {icon} --product-name EasyViewer --file-description "App to download youtube videos" --file-version {__version__} --product-version {__version__} --copyright "Copyright (c) 2023 Raul Catalinas Esteban" --add-data config;config --add-data "{icon};icon" --add-data src;src --add-data control;control --add-data osutils;osutils --add-data utils;utils"""

    execute = run(COMMAND, capture_output=True, check=True)

    if execute.returncode == 0:
        return print("App compiled successfully")

    return print(f"Could not compile, this is the reason: {execute.stderr}")


compile_app()
