# Standard library
from logging import basicConfig, error, info
from os import mkdir
from os.path import exists


class LoggingManagement:
    """
    Manage app logs
    """

    @classmethod
    def write_log(cls, message: str):
        """
        Writes a log message to the log file.

        Args:
            message (str): The message to write to the log file.
        """

        info(message)

    @classmethod
    def write_error(cls, message: str):
        """
        Write an error message to the log file.

        Args:
            message (str): The message to write to the log file.
        """

        error(message)

    @classmethod
    def initialize_logging(cls):
        """
        Initializes the logging configuration.
        """

        if not exists("Log"):
            mkdir("Log")

        basicConfig(
            filemode="w+",
            filename="Log/App.log",
            format="%(asctime)s -> %(levelname)s: %(message)s",
        )
