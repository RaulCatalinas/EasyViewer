"""
Returns the names of the configuration files
"""

from os import chdir
from os.path import dirname


def get_configuration_files() -> tuple[str, str]:
    """
    Returns the names of the configuration files.

    :return: A tuple with the names of configuration files.
    """

    chdir(dirname(__file__))

    return (
        "languages.xlsx",
        ".env",
        "control_variables.ini",
        "config.json",
        "token_github.ini",
    )
