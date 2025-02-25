# Core
from .download_validations import DownloadValidations
from .interact_api_pytubefix import InteractAPIPytube
from .download_data_store import DownloadDataStore

# App enums
from app_enums import DownloadInfoKeys, UserPreferencesKeys

# User preferences
from user_preferences import UserPreferencesManager


class DownloadManager:
    def __init__(self) -> None:
        self.download_data_store = DownloadDataStore()
        self.interact_api_pytubefix = InteractAPIPytube()
        self.user_preferences_manager = UserPreferencesManager()

    def validate_download(self) -> bool:
        url_to_validate: str = self.download_data_store.get_download_info(
            DownloadInfoKeys.URL
        )

        DownloadValidations.check_internet_connection()
        DownloadValidations.check_if_youtube_url(url_to_validate)
        DownloadValidations.is_youtube_video_available(url_to_validate)

        return True

    def download(self, download_video: bool):
        url_to_download: str = self.download_data_store.get_download_info(
            DownloadInfoKeys.URL
        )
        download_name: str = self.download_data_store.get_download_info(
            DownloadInfoKeys.DOWNLOAD_NAME
        )
        download_directory = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY
        )

        video_stream = self.interact_api_pytubefix.get_video(
            url_to_download, download_video
        )

        if video_stream is None:
            return

        video_stream.download(download_directory, download_name)
