# Standard library
from platform import system

INVALID_CHARS = {"Windows": r'[<>:/\\"|?*]', "Darwin": r"[:/]", "Linux": r"[/]"}

SYSTEM_NAME = system()
