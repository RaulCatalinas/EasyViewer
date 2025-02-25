# Standard library
from typing import Any

# App enums
from app_enums import DownloadInfoKeys

DOWNLOAD_INFO: dict[DownloadInfoKeys, Any] = {
    DownloadInfoKeys.URL: "",
    DownloadInfoKeys.DOWNLOAD_NAME: "",
}

EXTENSION_FILE_AUDIO = "mp3"
EXTENSION_FILE_VIDEO = "mp4"
