"""Start the app"""

# Standard library
from threading import Thread
from os import startfile

# Backend
from backend import Download, ShutdownHandler, Update, Validations

# Components
from components.dialog import ErrorDialog, UpdateDialog, WhatsNewDialog
from components.ui import IndexUI

# Control variables
from control_variables import (
    URLs,
    VideoLocation,
    DownloadName,
    set_initial_values,
    reset,
)

# Third-Party libraries
from flet import MainAxisAlignment, Page, app

# Osutils
from osutils import FileHandler

# Settings
from settings import EnvironmentVariables, GetConfigJson, Theme

# Utils
from utils import (
    EnumHelper,
    LoggingManagement,
    check_type,
    separate_urls,
    get_video_title,
    configure_directory,
)


class Main:
    def __init__(self, app_page: Page):
        """
        Initializes the Main class.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        self.urls = URLs()
        self.video_location = VideoLocation()
        self.download_name = DownloadName()

        self.updater = Update(page=app_page, update_dialog=None, whats_new_dialog=None)

        self.__initialize_app(app_page)
        self.__configure_window(app_page)
        self.__add_items_to_page(app_page)

    def __initialize_app(self, app_page: Page):
        """
        Initialize the application

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        Theme.set_initial_theme(app_page)
        EnvironmentVariables.set_initial_language(app_page)

        self.shutdown_handler = ShutdownHandler(app_page, self.__overlay)

        self.error_dialog = ErrorDialog(app_page=app_page, overlay=self.__overlay)
        self.update_dialog = UpdateDialog(
            app_page=app_page, overlay=self.__overlay, update=self.updater.update
        )
        self.whats_new_dialog = WhatsNewDialog(
            app_page=app_page, overlay=self.__overlay
        )

        self.updater.update_dialog = self.update_dialog
        self.updater.whats_new_dialog = self.whats_new_dialog

        set_initial_values(app_page)

    def __configure_window(self, app_page: Page):
        """
        Configures the window properties of the app page.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        app_page.title = GetConfigJson.get_config_json("WINDOW", "TITLE")
        app_page.window_width = GetConfigJson.get_config_json("WINDOW", "WIDTH")
        app_page.window_height = GetConfigJson.get_config_json("WINDOW", "HIGH")
        app_page.window_center()
        app_page.horizontal_alignment = EnumHelper.get_enum_value(
            MainAxisAlignment.CENTER
        )
        app_page.vertical_alignment = EnumHelper.get_enum_value(
            MainAxisAlignment.CENTER
        )
        app_page.window_resizable = False
        app_page.window_maximizable = False
        app_page.theme_mode = Theme.get_theme(app_page)
        app_page.window_prevent_close = True
        app_page.on_window_event = lambda e: self.__event_close_window(
            event=e, app_page=app_page
        )

    def __add_items_to_page(self, app_page: Page):
        """
        Adds items to the app page.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        index_ui = IndexUI(
            page=app_page,
            download=self.__download,
            video_location=self.video_location.get(),
            shutdown_handler=self.shutdown_handler,
            check_updates=self.__check_updates,
        )

        (
            self.input_url,
            self.input_directory,
            self.button_directory,
            self.button_download_video,
            self.button_download_audio,
            self.progress_bar,
            _,
            _,
        ) = index_ui.get_elements()

        self.checkbox = index_ui.get_checkbox()

        self.download = Download(app_page)

        Thread(
            target=app_page.add,
            args=[
                *index_ui.get_elements(),
                self.error_dialog,
                self.shutdown_handler,
                self.update_dialog,
                self.whats_new_dialog,
            ],
            daemon=False,
        ).start()

        Thread(target=self.__overlay, args=[app_page], daemon=False).start()

        if self.checkbox.get_value():
            self.__check_updates(True)

        self.updater.user_has_updated()

    def __event_close_window(self, event, app_page):
        """
        Event handler for the window close event.

        Args:
            event (EventData): Window event data.
            app_page (flet.Page): Reference to the app window.
        """

        if event.data == "close":
            self.__overlay(app_page)
            app_page.dialog = self.shutdown_handler

            if self.error_dialog.is_open():
                self.error_dialog.change_state(app_page)

            self.shutdown_handler.change_state(app_page)

    @check_type
    def __download(self, app_page: Page, download_video: bool):
        """
        Download the video if `download_video` is True, otherwise download the audio.

        Args:
            app_page (flet.Page): Reference to the app window.
            download_video (bool): Indicates whether to download the video or audio.
        """
        self.__toggle_state_widgets(app_page)
        self.progress_bar.update_value(None, app_page)

        configure_directory(self.input_directory, app_page)

        urls_to_download = self.input_url.get_value()

        video_location = self.video_location.get()

        if video_location is None:
            return

        videos_downloaded_successfully: list[str] = []

        try:
            Validations.validate_non_empty_url(urls_to_download)

            list_urls_to_download = separate_urls(urls_to_download)

            self.input_url.set_value("\n".join(list_urls_to_download))

            app_page.update(self.input_url)

            while len(list_urls_to_download) > 0:
                try:
                    url_to_download = list_urls_to_download[0]

                    self.urls.set(url_to_download)

                    url = self.urls.get()

                    if url is None:
                        return

                    can_download_video = self.__validate_download(url)

                    if can_download_video:
                        self.download_name.set(get_video_title(url, download_video))

                        self.download.download(download_video)

                        videos_downloaded_successfully.append(url)

                except Exception as error:
                    LoggingManagement.write_error(str(error))

                    self.error_dialog.show(str(error))

                finally:
                    url = self.urls.get()

                    if url is None:
                        return

                    list_urls_to_download.remove(url)

                    self.input_url.set_value("\n".join(list_urls_to_download))

                    app_page.update(self.input_url)

                    reset()

        except Exception as exception:
            self.error_dialog.show(str(exception))

            download_name = self.download_name.get()

            if download_name is None:
                return

            FileHandler.delete_file(
                path_to_file=video_location,
                download_name=download_name,
                callback=reset,
            )

        else:
            if len(videos_downloaded_successfully) > 0:
                startfile(video_location)

            self.input_url.set_value("")

        finally:
            videos_downloaded_successfully.clear()

            self.__toggle_state_widgets(app_page)
            reset()
            self.progress_bar.update_value(0, app_page)

    @check_type
    def __overlay(self, app_page: Page):
        """
        Add dialogs to the overlay of the specified page.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        to_add_to_the_overlay_of_the_page = [
            self.shutdown_handler,
            self.error_dialog,
        ]

        for dialog in to_add_to_the_overlay_of_the_page:
            app_page.overlay.append(dialog)

    @check_type
    def __toggle_state_widgets(self, app_page: Page):
        """
        Toggle the state of various widgets.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        self.button_directory.toggle_state(app_page)
        self.button_download_video.toggle_state(app_page)
        self.button_download_audio.toggle_state(app_page)
        self.input_url.toggle_state(app_page)

    @check_type
    def __check_updates(self, is_main: bool):
        """
        Checks for updates and shows a dialog if a new release is available.
        """

        is_new_release_available = self.updater.is_new_release_available()

        if is_new_release_available is None:
            return

        self.update_dialog.show(is_new_release_available, is_main)

    @check_type
    def __validate_download(self, url: str) -> bool:
        """
        Validates the download parameters.

        Args:
            url (str): The URL of the video.
            app_page (flet.Page): Reference to the app window.
            video_location (str): The location to save the video.

        Returns:
            bool: True if all validations pass, False otherwise.
        """

        return (
            Validations.check_if_youtube_url(url, self.input_url)
            and Validations.check_internet_connection()
            and Validations.is_youtube_video_available(url, self.input_url)
        )


if __name__ == "__main__":
    LoggingManagement.initialize_logging()

    app(target=Main)
