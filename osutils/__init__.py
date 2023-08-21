"""
Provides a set of utilities for interacting with the operating system of the user.
"""

# File handler
from .file_handler import FileHandler

# Get paths
from .get_paths import GetPaths

__all__ = ["GetPaths", "FileHandler"]
