# Standard library
from logging import Logger, FileHandler, Formatter, DEBUG
from os import mkdir
from os.path import exists

# Type checker
from .type_checker import check_type


class LoggingManagement:
    logger = Logger("EasyViewer", DEBUG)

    @classmethod
    @check_type
    def write_log(cls, message: str):
        cls.logger.info(message)

    @classmethod
    @check_type
    def write_error(cls, message: str):
        cls.logger.error(message)

    @classmethod
    @check_type
    def initialize_logging(cls):
        if not exists("Log"):
            mkdir("Log")

        handler = FileHandler("Log/App.log")

        formatter = Formatter(
            "%(asctime)s -> %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M",
        )

        handler.setFormatter(formatter)

        cls.logger.addHandler(handler)
