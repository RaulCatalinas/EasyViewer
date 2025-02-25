# Standard library
from typing import Any

# App enums
from app_enums import DownloadInfoKeys

# Constants
from constants import DOWNLOAD_INFO


class DownloadDataStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DownloadDataStore, cls).__new__(cls)

        return cls._instance

    def set_download_info(self, key: DownloadInfoKeys, value: Any):
        """
        Set download details

        Args:
            key (DownloadInfoKeys): The download info key.
            value (Any): The new value for the download info.
        """

        DOWNLOAD_INFO[key] = value

    def get_download_info(self, key: DownloadInfoKeys) -> Any:
        """
        Retrieve current download state

        Args:
            key (DownloadInfoKeys): The download info key.
        """

        return DOWNLOAD_INFO.get(key)

    def reset_download_info(self):
        """Resets download information to default values"""

        DOWNLOAD_INFO[DownloadInfoKeys.URL] = ""
        DOWNLOAD_INFO[DownloadInfoKeys.DOWNLOAD_NAME] = ""
