from pathlib import Path


def get_default_download_directory():
    """
    Returns the default download directory (Desktop) in a cross-platform way.
    """

    return str(Path.home() / "Desktop")
