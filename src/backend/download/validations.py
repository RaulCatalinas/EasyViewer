"""
Validating various aspects of a YouTube video download request
"""
# Standard library
from urllib.parse import urlparse

# Third-Party libraries
from flet import Page
from pytube import YouTube
from requests import ConnectionError, Timeout, get

# Constants
from constants import ALLOW_HOSTS, GOOGLE

# Control variables
from control_variables import ControlVariables

# Create widgets
from frontend.create_widgets import CreateInputs

# Osutils
from osutils import GetPaths

# Settings
from settings import ExcelTextLoader

# Utils
from utils import LoggingManagement, check_type


class Validations:
    """
    Validating various aspects of a YouTube video download request
    """

    @staticmethod
    @check_type
    def validate_non_empty_url(url: str) -> bool:
        """
        Checks if a URL has been entered.

        Args:
            url (str): URL to be checked if it's not an empty string

        Raises:
            ValueError: Error thrown if the given url is an empty string

        Returns:
            bool: True if the given string is not empty
        """

        if not url:
            LoggingManagement.write_error("No URL entered")
            raise ValueError(ExcelTextLoader.get_text(9))

        LoggingManagement.write_log("A URL has been entered")

        return True

    @staticmethod
    @check_type
    def check_if_youtube_url(url: str) -> bool:
        """
        Checks if a given URL is from YouTube.

        Args:
            url (str): URL to check if it is from YouTube

        Raises:
            ValueError: Error thrown if the url is not from YouTube

        Returns:
            bool: True if the url is from YouTube
        """

        host = urlparse(url).hostname

        if host in ALLOW_HOSTS:
            LoggingManagement.write_log("The URL is from YouTube")

            return True

        LoggingManagement.write_error("The URL is not from YouTube")

        raise ValueError(ExcelTextLoader.get_text(11))

    @staticmethod
    @check_type
    def set_default_directory_or_check_selected(
        input_directory: CreateInputs,
        page: Page,
        video_location: str,
    ) -> bool:
        """
        Check if a directory is selected, or set a default.

        Args:
            input_directory (flet.TextField): Entry for the default directory.
            page (flet.Page): Reference to the app window.
            video_location (str): The location to save the video.

        Returns:
            bool: True to indicate that everything went well.
        """

        if not video_location or video_location == "None":
            default_directory = GetPaths.get_desktop_path()

            input_directory.set_value(default_directory)
            ControlVariables().set_control_variable(
                option="VIDEO_LOCATION", value=default_directory
            )

            LoggingManagement.write_log("Default directory set")
            page.update(input_directory)

        else:
            LoggingManagement.write_log(
                "A directory has been selected to save the video"
            )

        return True

    @staticmethod
    def check_internet_connection() -> bool:
        """
        Check internet connection availability.

        Raises:
            ConnectionError: Error thrown if there is no internet connection

        Returns:
            bool: True if there is internet connection
        """

        try:
            get(GOOGLE, timeout=5)

        except (ConnectionError, Timeout) as exc:
            LoggingManagement.write_error("No internet connection")

            raise ConnectionError(ExcelTextLoader.get_text(10)) from exc

        LoggingManagement.write_log("Internet connection is available")

        return True

    @staticmethod
    @check_type
    def is_youtube_video_available(url: str) -> bool:
        """
        Check if YouTube video is available

        Args:
            url (str): Video URL to check

        Raises:
            ValueError: Error thrown if the video is not available

        Returns:
            bool: True if video is available
        """

        try:
            YouTube(url).check_availability()

            LoggingManagement.write_log("The video is available")
            return True

        except Exception as exception:
            LoggingManagement.write_error(str(exception))
            raise ValueError(str(exception)) from exception
