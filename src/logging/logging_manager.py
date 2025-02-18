# Standard library
from logging import INFO, getLogger, Formatter, FileHandler
from pathlib import Path
from atexit import register
from typing import Callable
from threading import Lock

# App enums
from app_enums import LOG_LEVELS


class LoggingManager:
    """Singleton logging manager to handle application-wide logging with automatic log flushing on exit."""

    _instance = None
    _lock = Lock()

    LOG_DIR = Path("logs")
    LOG_FILE = LOG_DIR / "app.log"

    def __new__(cls):
        """Ensures only one instance of LoggingManager is created (Singleton pattern)."""
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self) -> None:
        """Initializes the logging system, ensuring the log directory and file exist."""
        self._ensure_log_directory()
        self.logger = getLogger("EasyViewer")
        self.logger.setLevel(INFO)

        log_formatter = Formatter("%(asctime)s - %(levelname)s: %(message)s")

        file_handler = FileHandler(self.LOG_FILE, mode="a", encoding="utf-8")
        file_handler.setFormatter(log_formatter)
        self.logger.addHandler(file_handler)

        self.log_levels: dict[LOG_LEVELS, Callable] = {
            LOG_LEVELS.INFO: self.logger.info,
            LOG_LEVELS.WARNING: self.logger.warning,
            LOG_LEVELS.ERROR: self.logger.error,
            LOG_LEVELS.CRITICAL: self.logger.critical,
        }
        register(self._flush_logs)

    def _ensure_log_directory(self) -> None:
        """Ensures the logs directory and log file exist before writing."""
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)
        if not self.LOG_FILE.exists():
            self.LOG_FILE.touch()

    def _flush_logs(self) -> None:
        """Flushes and closes all log handlers to ensure all logs are written to disk."""

        for handler in self.logger.handlers:
            handler.flush()
            handler.close()

    def write_log(self, level: LOG_LEVELS, message: str) -> None:
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
