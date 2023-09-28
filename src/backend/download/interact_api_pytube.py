"""
Interact with the Pytube API.
"""

# Third-Party libraries
from pytube import YouTube
from pytube.exceptions import (
    AgeRestrictedError,
    LiveStreamError,
    MembersOnly,
    PytubeError,
    VideoPrivate,
    VideoRegionBlocked,
)

# Control variables
from control_variables import ControlVariables

# Osutils
from osutils import FileHandler

# Settings
from settings import ExcelTextLoader

# Utils
from utils import LoggingManagement, check_type


class InteractAPIPytube:
    """
    Interact with the Pytube API.
    """

    def __init__(self):
        self.control_variables = ControlVariables()

    @check_type
    def get_video(self, download_video: bool):
        """
        Get the video to download

        Args:
            download_video (bool): Specify to download the video or only the audio

        Raises:
            Exception: Error occurred while obtaining the video

        Returns:
            pytube.Stream | None: The information of the video to download
        """

        url = self.control_variables.get_control_variable("URL_VIDEO")

        try:
            video_id = YouTube(url)
            title = video_id.title
            stream = video_id.streams

            title_for_the_file = FileHandler.clean_invalid_chars(title)

            extension_file = "mp3" if not download_video else "mp4"
            downloaded_file_type = "audio" if not download_video else "video"

            self.control_variables.set_control_variable(
                control_variable="DOWNLOAD_NAME",
                value=f"{title_for_the_file}.{extension_file}",
            )

            LoggingManagement.write_log(
                f"The {downloaded_file_type} will be downloaded."
            )

            return (
                stream.get_highest_resolution()
                if download_video
                else stream.get_audio_only()
            )

        except AgeRestrictedError as age_error:
            LoggingManagement.write_error(str(age_error))

            raise Exception(ExcelTextLoader.get_text(23)) from age_error

        except LiveStreamError as live_error:
            LoggingManagement.write_error(str(live_error))

            raise Exception(ExcelTextLoader.get_text(24)) from live_error

        except MembersOnly as member_error:
            LoggingManagement.write_error(str(member_error))

            raise Exception(ExcelTextLoader.get_text(25)) from member_error

        except VideoPrivate as video_private_error:
            LoggingManagement.write_error(str(video_private_error))

            raise Exception(ExcelTextLoader.get_text(26)) from video_private_error

        except VideoRegionBlocked as video_region_blocked_error:
            LoggingManagement.write_error(str(video_region_blocked_error))

            raise Exception(
                ExcelTextLoader.get_text(27)
            ) from video_region_blocked_error

        except PytubeError as pytube_error:
            LoggingManagement.write_error(str(pytube_error))

            raise Exception(ExcelTextLoader.get_text(29)) from pytube_error
