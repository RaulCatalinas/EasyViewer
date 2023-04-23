"""Build the app"""

from subprocess import run

from src.client.get_paths import get_icon_path

__version__ = "1.0.3"


def compile_app():
    """Compile the app to generate the executable file"""

    icon = get_icon_path("./")

    COMMAND = f"""flet pack src/client/main.py -n EasyViewer -i {icon} --product-name EasyViewer --file-description EasyViewer --file-version {__version__} --product-version {__version__} --copyright "Copyright (c) 2023 Raul Catalinas Esteban" --add-data config;config --add-data "{icon};icon" --add-data src/app_logic;app_logic --add-data src/client;client --add-data pyproject.toml;. --add-data poetry.lock;."""

    execute = run(COMMAND, capture_output=True, check=True)

    if execute.returncode == 0:
        return print("App compiled successfully")

    return print(f"Could not compile, this is the reason: {execute.stderr}")


compile_app()
