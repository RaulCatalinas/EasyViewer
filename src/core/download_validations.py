# Standard library
from urllib.parse import urlsplit

# Constants
from constants import ALLOW_HOSTS, GOOGLE

# Third-Party libraries
from pytubefix import YouTube
from requests import ConnectionError, Timeout, head
from pytubefix.exceptions import (
    AgeRestrictedError,
    LiveStreamError,
    MembersOnly,
    VideoPrivate,
    VideoRegionBlocked,
    VideoUnavailable,
    LoginRequired,
)

# App logging
from app_logging import LoggingManager

# App enums
from app_enums import LogLevels, ExcelTextLoaderKeys

# i18n
from i18n import ExcelTextLoader

logging_manager = LoggingManager()
excel_text_loader = ExcelTextLoader()


class DownloadValidations:
    """
    Validating various aspects of a YouTube video download request
    """

    @staticmethod
    def validate_non_empty_url(url: str):
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
            logging_manager.write_log(LogLevels.WARNING, "No URL entered")

            raise ValueError(
                excel_text_loader.get_text(ExcelTextLoaderKeys.ERROR_EMPTY_URL)
            )

    @staticmethod
    def check_if_youtube_url(url: str):
        """
        Checks if a given URL is from YouTube.

        Args:
            url (str): URL to check if it is from YouTube

        Raises:
            ValueError: Error thrown if the url is not from YouTube

        Returns:
            bool: True if the url is from YouTube
        """

        host = urlsplit(url).hostname

        if host not in ALLOW_HOSTS:
            logging_manager.write_log(
                LogLevels.WARNING, "The URL is not from YouTube"
            )

            raise ValueError(
                excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_YOUTUBE_URL
                )
            )

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
            head(GOOGLE, timeout=5)

        except (ConnectionError, Timeout) as e:
            logging_manager.write_log(
                LogLevels.ERROR, f"Internet connection issue: {e}"
            )

            raise ConnectionError(
                excel_text_loader.get_text(ExcelTextLoaderKeys.ERROR_CONNECTION)
            )

        return True

    @staticmethod
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

            return True

        except (
            AgeRestrictedError,
            LiveStreamError,
            MembersOnly,
            VideoPrivate,
            VideoRegionBlocked,
            VideoUnavailable,
        ) as e:
            logging_manager.write_log(LogLevels.WARNING, str(e))

            error_message = {
                AgeRestrictedError: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_AGE_RESTRICTED
                ),
                LiveStreamError: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_LIVE_STREAM
                ),
                MembersOnly: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_ONLY_MEMBERS
                ),
                VideoPrivate: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_PRIVATE_VIDEO
                ),
                VideoRegionBlocked: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_BLOCKED_REGION
                ),
                VideoUnavailable: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_DEFAULT
                ),
                LoginRequired: excel_text_loader.get_text(
                    ExcelTextLoaderKeys.ERROR_DEFAULT
                ),
            }

            raise ValueError(error_message.get(type(e))) from e

        except Exception as e:
            logging_manager.write_log(LogLevels.CRITICAL, str(e))

            raise Exception(
                excel_text_loader.get_text(ExcelTextLoaderKeys.ERROR_DEFAULT)
            ) from e
