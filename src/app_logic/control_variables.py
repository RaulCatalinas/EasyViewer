"""Control variables for the operation of the app"""

from tkinter import StringVar, BooleanVar

VIDEO_LOCATION = StringVar()
LINK_VIDEO = StringVar()
DOWNLOAD_NAME = StringVar()
DOWNLOADED_SUCCESSFULLY = BooleanVar()


class ControlVariables:
    """Control variables for the app"""

    @staticmethod
    def get_location_video():
        """
        Returns the location selected by the user
        :return: The location selected by the user
        """

        return VIDEO_LOCATION.get()

    @staticmethod
    def get_download_name():
        """
        Returns the name of the download
        :return: The name of the download
        """

        return DOWNLOAD_NAME.get()

    @staticmethod
    def set_download_name(name):
        """Set the name for the downloaded video"""

        DOWNLOAD_NAME.set(name)

    @staticmethod
    def set_downloaded_successfully(downloaded):
        """
        Establishes if a videoaudio has been downloaded well or not
        """

        DOWNLOADED_SUCCESSFULLY.set(downloaded)

    @staticmethod
    def get_downloaded_successfully():
        """
        Returns if a video has been downloaded well or not
        :return: Whether a video downloaded well or not
        """

        return DOWNLOADED_SUCCESSFULLY.get()

    @staticmethod
    def get_url_video():
        """
        Returns the url of the video
        :return: The url of the video
        """

        return LINK_VIDEO.get()
