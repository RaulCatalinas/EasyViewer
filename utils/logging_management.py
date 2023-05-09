"""Manage app logs"""

from logging import info, basicConfig, error
from os import mkdir
from os.path import exists


class LoggingManagement:
    """Create a folder called "Log" if it doesn't exist, then create a log file called "App.log" in that folder and write to that log when the function in charge of it is called"""

    @classmethod
    def write_log(cls, message: str):
        """
        Writes a log message to the log file.

        :param message: The message to write to the log file
        """

        info(message)

    @classmethod
    def write_error(cls, message: str):
        """
        Write an error message to the log file.

        :param message: The message to write to the log file
        """

        error(message)

    @classmethod
    def initialize_logging(cls):
        """Initializes the registry configuration"""

        if not exists("Log"):
            mkdir("Log")

        basicConfig(
            filemode="w+",
            filename="Log/App.log",
            format="%(asctime)s -> %(levelname)s: %(message)s",
        )
