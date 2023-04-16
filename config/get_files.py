from os import chdir
from os.path import dirname


def get_files_path() -> tuple[str, str]:
    """
    The function returns a tuple of file paths for "languages.xlsx", ".env" "control_variables.json", and "config.json" after changing the current working directory to the directory of the current file.

    :return: A tuple of four strings: "languages.xlsx", ".env", "control_variables.json", and "config.json".
    """

    chdir(dirname(__file__))

    return (
        "languages.xlsx",
        ".env",
        "control_variables.ini",
        "config.json",
        "token_github.ini",
    )
