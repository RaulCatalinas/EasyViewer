"""Checks to perform before downloading the video and/or the audio"""

from os import environ
from os.path import isdir, join

import requests
from pytube import YouTube

from client.get_config import Config
from logging_management import LoggingManagement

log = LoggingManagement()
config = Config()


class Validations:
    """Required validations before downloading a video"""

    @staticmethod
    def check_if_directory_is_selected(download_directory):
        """
        Check if a directory is selected, otherwise it puts a default directory
        """

        if download_directory.get() != "" and isdir(download_directory.get()):
            log.write_log("A directory has been selected to save the video")
            return True

        log.write_error("Default directory set")
        download_directory.set(join(join(environ["USERPROFILE"]), "Desktop"))
        return True

    @staticmethod
    def check_if_is_url_youtube(url):
        """
        Check if the URL is from YouTube
        """
        if (
            "https:www.youtube.comwatch?v=" in url.get()
            or "https:youtu.be" in url.get()
            or "https:www.youtube.comshorts" in url.get()
        ):
            log.write_log("The URL is from YouTube")
            return True

        log.write_error("The URL is not from YouTube")
        raise Exception(config.get_config_execel(17))

    @staticmethod
    def check_internet_connection():
        """
        Check if there is internet connection
        """
        try:
            requests.get("https:www.google.com", timeout=5)
        except (requests.ConnectionError, requests.Timeout) as exc:
            log.write_error("No internet connection")
            raise Exception(config.get_config_execel(16)) from exc

        log.write_log("If there is internet connection")
        return True

    @staticmethod
    def check_if_a_url_has_been_entered(url):
        """
        Check if a URL has been entered
        """
        if url.get() == "":
            log.write_error("No URL entered")
            raise Exception(config.get_config_execel(15))

        log.write_log("A URL has been entered")
        return True

    @staticmethod
    def check_if_the_video_is_available(url):
        """
        Check if the video is available
        """
        try:
            YouTube(url.get()).check_availability()
            log.write_log("The video is available")
            return True

        except Exception as exc:
            log.write_error(str(exc))
            raise Exception(str(exc)) from exc
