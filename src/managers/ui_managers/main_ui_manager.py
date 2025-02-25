# Standard library
from threading import Thread

# Third party libraries
from flet import Icons, Page

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar
from components.dialogs.updates import UpdateDialog
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
        update_dialog = UpdateDialog(app, lambda: ())
        self.update_manager = UpdateManager(update_dialog)

        self.user_preferences_manager = UserPreferencesManager()

        self.download_manager = DownloadManager()
        self.interact_api_pytube = InteractAPIPytube()
        self.download_data_store = DownloadDataStore()

        self.error_dialog = ErrorDialog(self.app)
        self.logging_manager = LoggingManager()

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

        update_dialog.update_function = self.update_manager.update

        self._initialize_ui()

    def _initialize_ui(self):
        """Initialises the UI elements and adds them to the app."""

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
        self._toggle_state_widgets()

        self.progress_bar.update_value(None)

        download_directory: str = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY
        )

        if download_directory != "" and verify_download_directory(
            download_directory
        ):
            default_download_directory = get_default_download_directory()

            self.input_directory.set_value(default_download_directory)

            self.user_preferences_manager.set_preference(
                UserPreferencesKeys.DOWNLOAD_DIRECTORY,
                default_download_directory,
            )

        urls_to_download = self.input_url.get_value()

        if urls_to_download is None:
            return

        videos_downloaded_successfully: list[str] = []

        try:
            DownloadValidations.validate_non_empty_url(urls_to_download)

            list_urls_to_download = separate_urls(urls_to_download)

            self.input_url.set_value("\n".join(list_urls_to_download))

            while len(list_urls_to_download) > 0:
                try:
                    url = list_urls_to_download[0]
                    self.download_data_store.set_download_info(
                        DownloadInfoKeys.URL, url
                    )

                    can_download_video = (
                        self.download_manager.validate_download()
                    )

                    if can_download_video:
                        self.download_data_store.set_download_info(
                            DownloadInfoKeys.DOWNLOAD_NAME,
                            self.interact_api_pytube.get_video_title(
                                url, download_video
                            ),
                        )

                        self.download_manager.download(download_video)

                        videos_downloaded_successfully.append(url)

                except Exception as e:
                    self.error_dialog.show_dialog(str(e))

                    download_directory = (
                        self.user_preferences_manager.get_preference(
                            UserPreferencesKeys.DOWNLOAD_DIRECTORY
                        )
                    )

                    download_name: str = (
                        self.download_data_store.get_download_info(
                            DownloadInfoKeys.DOWNLOAD_NAME
                        )
                    )

                    delete_file(download_directory, download_name)

                finally:
                    list_urls_to_download.pop(0)

                    self.input_url.set_value("\n".join(list_urls_to_download))

                    self.download_data_store.reset_download_info()

        except Exception as e:
            self.logging_manager.write_log(LOG_LEVELS.CRITICAL, str(e))

            self.error_dialog.show_dialog(str(e))

        finally:
            if len(videos_downloaded_successfully) > 0:
                open_directory(
                    self.user_preferences_manager.get_preference(
                        UserPreferencesKeys.DOWNLOAD_DIRECTORY
                    )
                )

            self.progress_bar.update_value(0)
            self.input_url.set_value("")

            self._toggle_state_widgets()

    def _toggle_state_widgets(self):
        """Toggles widget state (enabled/disabled)"""

        self.input_url.toggle_state()
        self.button_select_directory.toggle_state()
        self.button_download_audio.toggle_state()
        self.button_download_video.toggle_state()
