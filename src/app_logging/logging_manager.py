# Standard library
from logging import INFO, getLogger, Formatter, FileHandler
from pathlib import Path
from atexit import register
from typing import Callable, Dict, ClassVar
from threading import Lock
from functools import lru_cache

# App enums
from app_enums import LogLevels


class LoggingManager:
    """Singleton logging manager to handle application-wide logging with automatic log flushing on exit."""

    _instance = None
    _lock = Lock()

    LOG_DIR: ClassVar[Path] = Path("logs")
    LOG_FILE: ClassVar[Path] = LOG_DIR.joinpath("app.log")

    def __new__(cls):
        """Ensures only one instance of LoggingManager is created (Singleton pattern)."""

        # Double-checked locking pattern for better performance in multi-threaded environments
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(LoggingManager, cls).__new__(cls)
                    cls._instance._initialize_logger()

        return cls._instance

    def _initialize_logger(self) -> None:
        """Initializes the logging system, ensuring the log directory and file exist."""

        self._ensure_log_directory()

        logger_name = "EasyViewer"

        self.logger = getLogger(logger_name)

        if not self.logger.handlers:
            self.logger.setLevel(INFO)

            log_formatter = Formatter(
                "%(asctime)s - %(levelname)s: %(message)s"
            )

            # Efficient file handler creation with buffering for better I/O performance
            file_handler = FileHandler(
                self.LOG_FILE, mode="a", encoding="utf-8", delay=True
            )
            file_handler.setFormatter(log_formatter)
            self.logger.addHandler(file_handler)

            # Register flush at exit just once
            register(self._flush_logs)

        self.log_levels: Dict[LogLevels, Callable] = {
            LogLevels.INFO: self.logger.info,
            LogLevels.WARNING: self.logger.warning,
            LogLevels.ERROR: self.logger.error,
            LogLevels.CRITICAL: self.logger.critical,
        }

    @staticmethod
    @lru_cache(
        maxsize=1
    )  # Cache this result since it won't change during runtime
    def _ensure_log_directory() -> None:
        """Ensures the logs directory and log file exist before writing."""

        LoggingManager.LOG_DIR.mkdir(parents=True, exist_ok=True)

        log_file = LoggingManager.LOG_FILE

        if not log_file.exists():
            log_file.touch()

    def _flush_logs(self) -> None:
        """Flushes and closes all log handlers to ensure all logs are written to disk."""

        for handler in self.logger.handlers:
            # Check if handler is still active before flushing
            if hasattr(handler, "close") and callable(handler.close):
                handler.flush()
                handler.close()

    def write_log(self, level: LogLevels, message: str) -> None:
        """
        Logs a message at the specified level.

        Args:
            level (LOG_LEVELS): The logging level.
            message (str): The message to log.
        """

        log_function = self.log_levels.get(level)

        if log_function:
            log_function(message)

        else:
            self.logger.warning(
                f"Attempted to log with invalid level '{level}': {message}"
            )
