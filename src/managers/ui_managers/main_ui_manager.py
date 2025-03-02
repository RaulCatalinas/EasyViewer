# Standard library
from errno import ENOSPC
from threading import Thread
from typing import Optional

# Third party libraries
from flet import Icons, Page

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar
from components.dialogs.errors import ErrorDialog

# Managers
from .settings_ui_manager import SettingsUIManager
from ..window_managers import SelectDirectoryManager

# App settings
from app_settings import AppColors

# Update manager
from update import UpdateManager

# App enums
from app_enums import UserPreferencesKeys, DownloadInfoKeys, LOG_LEVELS

# User preferences
from user_preferences import UserPreferencesManager

# Core
from core import (
    DownloadManager,
    InteractAPIPytube,
    DownloadDataStore,
    DownloadValidations,
)

# Utils
from utils import (
    get_default_download_directory,
    verify_download_directory,
    separate_urls,
    delete_file,
    open_directory,
)

# App logging
from app_logging import LoggingManager


class MainUIManager:
    def __init__(self, app: Page):
        self.app = app

        self.update_manager = UpdateManager(self.app)
        self.logging_manager = LoggingManager()
        self.user_preferences_manager = UserPreferencesManager()

        self.download_manager = DownloadManager()
        self.interact_api_pytube = InteractAPIPytube()
        self.download_data_store = DownloadDataStore()

        self.error_dialog = ErrorDialog(self.app)

        self.input_directory = Input(
            app=self.app,
            placeholder="Directory",
            text_size=20,
            read_only=True,
            offset_y=1,
            initial_value=self.user_preferences_manager.get_preference(
                UserPreferencesKeys.DOWNLOAD_DIRECTORY
            ),
        )
        self.input_url = Input(
            app=self.app,
            placeholder="Video URL",
            text_size=20,
            autofocus=True,
            is_multiline=True,
            max_height=2,
            offset_y=0.5,
        )
        self.button_download_audio = IconButton(
            app=self.app,
            icon=Icons.AUDIO_FILE,
            function=lambda _: Thread(
                target=self._initialize_download, args=[False], daemon=True
            ).start(),
            offset_x=8.4,
            offset_y=2.79,
            scale=2.5,
        )
        self.button_download_video = IconButton(
            app=self.app,
            icon=Icons.VIDEO_FILE,
            function=lambda _: Thread(
                target=self._initialize_download, args=[True], daemon=True
            ).start(),
            offset_x=10.45,
            offset_y=1.56,
            scale=2.5,
        )
        self.button_select_directory = IconButton(
            app=self.app,
            icon=Icons.FOLDER,
            function=lambda _: self.select_directory_manager.select_directory(),
            offset_x=9.42,
            offset_y=2.02,
            scale=2.5,
        )

        self.progress_bar = ProgressBar(
            color=AppColors.PROGRESS_BAR_COLOR.value, offset_y=25, app=self.app
        )

        self.select_directory_manager = SelectDirectoryManager(
            self.input_directory
        )

        self.update_manager.show_post_update_dialogs_in_background()

        self._initialize_ui()

    def _initialize_ui(self):
        """Initializes the UI elements and adds them to the app."""
        SettingsUIManager(self.app, self.update_manager)
        self.app.add(
            self.select_directory_manager,
            self.input_url,
            self.input_directory,
            self.button_select_directory,
            self.button_download_audio,
            self.button_download_video,
            self.progress_bar,
        )

    def _initialize_download(self, download_video: bool):
        """Initializes the download process."""

        self._toggle_state_widgets()
        self.progress_bar.update_value(None)

        self._get_or_set_download_directory()

        urls_to_download = self.input_url.get_value()

        if urls_to_download is None:
            return

        videos_downloaded_successfully = self._process_downloads(
            urls_to_download, download_video
        )

        self._finalize_download(videos_downloaded_successfully)
        self._toggle_state_widgets()

    def _get_or_set_download_directory(self) -> str:
        """Gets the user-selected download directory or sets the default one."""

        download_directory = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY
        )

        if download_directory and verify_download_directory(download_directory):
            return download_directory

        default_download_directory = get_default_download_directory()
        self.input_directory.set_value(default_download_directory)
        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY, default_download_directory
        )

        return default_download_directory

    def _process_downloads(
        self, urls_to_download: str, download_video: bool
    ) -> Optional[list[str]]:
        """Processes the list of URLs and handles the download process."""

        try:
            DownloadValidations.validate_non_empty_url(urls_to_download)

            list_urls_to_download = separate_urls(urls_to_download)

            self.input_url.set_value("\n".join(list_urls_to_download))

            videos_downloaded_successfully: list[str] = []

            while list_urls_to_download:
                url = list_urls_to_download.pop(0)

                self.input_url.set_value("\n".join(list_urls_to_download))

                self._process_single_download(
                    url, download_video, videos_downloaded_successfully
                )

        except Exception as e:
            self.logging_manager.write_log(LOG_LEVELS.CRITICAL, str(e))
            self.error_dialog.show_dialog(str(e))

        else:
            return videos_downloaded_successfully

    def _process_single_download(
        self,
        url: str,
        download_video: bool,
        videos_downloaded_successfully: list[str],
    ):
        """Handles the validation and downloading of a single video."""

        try:
            self.download_data_store.set_download_info(
                DownloadInfoKeys.URL, url
            )

            if self.download_manager.validate_download():
                self.download_data_store.set_download_info(
                    DownloadInfoKeys.DOWNLOAD_NAME,
                    self.interact_api_pytube.get_video_title(
                        url, download_video
                    ),
                )

                self.download_manager.download(download_video)

                videos_downloaded_successfully.append(url)

        except OSError as e:
            if e.errno == ENOSPC:
                self._handle_download_error(
                    "Insufficient space to save download"
                )

        except Exception as e:
            self._handle_download_error(str(e))

        finally:
            self.download_data_store.reset_download_info()

    def _handle_download_error(self, error: str):
        """Handles errors that occur during the download process."""

        self.error_dialog.show_dialog(error)

        download_directory: str = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY
        )
        download_name: str = self.download_data_store.get_download_info(
            DownloadInfoKeys.DOWNLOAD_NAME
        )

        delete_file(download_directory, download_name)

    def _finalize_download(
        self, videos_downloaded_successfully: Optional[list[str]]
    ):
        """Finalizes the download process by opening the directory and resetting UI elements."""

        if videos_downloaded_successfully is not None:
            open_directory(
                self.user_preferences_manager.get_preference(
                    UserPreferencesKeys.DOWNLOAD_DIRECTORY
                )
            )

        self.progress_bar.update_value(0)
        self.input_url.set_value("")

    def _toggle_state_widgets(self):
        """Toggles widget state (enabled/disabled)."""

        self.input_url.toggle_state()
        self.button_select_directory.toggle_state()
        self.button_download_audio.toggle_state()
        self.button_download_video.toggle_state()
