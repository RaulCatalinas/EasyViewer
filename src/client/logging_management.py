"""Manage app logs"""

from logging import DEBUG, info, basicConfig, error
from os import mkdir
from os.path import exists


class LoggingManagement:
    """Create a folder called "Log" if it doesn't exist, then create a log file called "App.log" in that folder and write to that log when the function in charge of it is called"""

    def __init__(self):

        if not exists("Log"):
            mkdir("Log")

        basicConfig(
            level=DEBUG,
            filemode="w+",
            filename="Log/App.log",
            format="%(asctime)s -> %(levelname)s: %(message)s",
        )

    @staticmethod
    def write_log(message):
        """
        Writes a log message to the log file.

        :param message: The message to write to the log file
        """
        info(message)

    @staticmethod
    def write_error(message):
        """
        Write an error message to the log file.

        :param message: The message to write to the log file
        """
        error(message)
