"""Build the app"""

from subprocess import run

command = """flet pack src/client/main.py -n EasyViewer -i icon/icon.png --product-name EasyViewer --product-version "0.2.1" --copyright "Copyright (c) 2023 Raul Catalinas Esteban" --add-data src;* --add-data icon;* --add-data config;config"""

execute = run(command, capture_output=True, text=True, check=True)

if execute.returncode == 0:
    print("App compiled successfully")
else:
    print(f"Could not compile, this is the reason: {execute.stderr}")
