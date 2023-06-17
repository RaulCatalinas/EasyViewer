from logging import info, basicConfig, error
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

        :param message: The message to write to the log file.
        """

        info(message)

    @classmethod
    def write_error(cls, message: str):
        """
        Write an error message to the log file.

        :param message: The message to write to the log file.
        """

        error(message)

    @classmethod
    def initialize_logging(cls):
        """
        Initializes the logging configuration.

        It creates a folder called "Log" if it doesn't exist, then creates a log file called "App.log" in that folder
        and configures the logging module to write logs to that file.
        """

        if not exists("Log"):
            mkdir("Log")

        basicConfig(
            filemode="w+",
            filename="Log/App.log",
            format="%(asctime)s -> %(levelname)s: %(message)s",
        )
