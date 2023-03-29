"""Control variables for the operation of the app"""


class ControlVariables:
    """Control variables for the app"""

    def __init__(self):
        self._video_location = ""
        self._url_video = ""
        self._download_name = ""
        self._downloaded_successfully = None

    @property
    def video_location(self):
        """
        Returns the location selected by the user
        :return: The location selected by the user
        """

        return self._video_location

    @video_location.setter
    def video_location(self, location):
        self._video_location = location

    @property
    def download_name(self):
        """
        Returns the name of the download
        :return: The name of the download
        """

        return self._download_name

    @download_name.setter
    def download_name(self, name):
        """Set the name for the downloaded video"""

        self._download_name = name

    @property
    def downloaded_successfully(self):
        """
        Returns if a video has been downloaded well or not
        :return: Whether a video downloaded well or not
        """

        return self._downloaded_successfully

    @downloaded_successfully.setter
    def downloaded_successfully(self, downloaded):
        """
        Establishes if a video or audio has been downloaded well or not
        """

        self._downloaded_successfully = downloaded

    @property
    def url_video(self):
        """
        Returns the url of the video
        :return: The url of the video
        """

        return self._url_video

    @url_video.setter
    def url_video(self, url):
        self._url_video = url
