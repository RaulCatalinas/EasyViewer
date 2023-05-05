"""
The osutils package provides a set of utilities for interacting with the operating system of the user.
"""

from .file_handler import FileHandler
from .get_paths import GetPaths

__all__ = ["GetPaths", "FileHandler"]
