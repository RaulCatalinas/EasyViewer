# Osutils
from osutils import GetPaths

# Logging management
from .logging_management import LoggingManagement

# Control variables
from control_variables import VideoLocation

# Standard library
from os.path import isdir


video_location_instance = VideoLocation()


def configure_directory(input_directory, page) -> bool:
    """
    Set a default if none is selected, or use the selected one.

    Args:
        input_directory (flet.TextField): Entry for the default directory.
        page (flet.Page): Reference to the app window.
        video_location (str): The location to save the video.

    Returns:
        bool: True to indicate that everything went well.
    """

    video_location = video_location_instance.get()

    if not video_location or not isdir(video_location):
        default_directory = str(GetPaths.get_desktop_path())

        input_directory.set_value(default_directory)

        video_location_instance.set(default_directory)

        LoggingManagement.write_log("Default directory set")

        page.update(input_directory)

    else:
        LoggingManagement.write_log("A directory has been selected to save the video")

    return True
