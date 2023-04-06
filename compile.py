"""Build the app"""

from subprocess import run


def compile_app():
    """Compile the app to generate the executable file"""

    COMMAND = """flet pack src/client/main.py -n EasyViewer -i icon/icon.png --product-name EasyViewer 
    --product-version "0.2.1" --copyright "Copyright (c) 2023 Raul Catalinas Esteban" --add-data config;config 
    --add-data icon;icon --add-data src/app_logic;app_logic --add-data src/client;client --images;images"""

    execute = run(COMMAND, capture_output=True, check=True)

    if execute.returncode == 0:
        return print("App compiled successfully")

    return print(f"Could not compile, this is the reason: {execute.stderr}")


compile_app()
