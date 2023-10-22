"""Start the app"""

# Standard library
from threading import Thread
from os import startfile

# Backend
from backend import Download, ShutdownHandler, Update, Validations

# Components
from components.dialog import ErrorDialog, UpdateDialog
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

# Modify GUI
from frontend.modify_gui import ChangeTheme

# Osutils
from osutils import FileHandler

# Settings
from settings import EnvironmentVariables, ExcelTextLoader, GetConfigJson

# Utils
from utils import EnumHelper, LoggingManagement, check_type


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
        self.updater = Update(page=app_page, update_dialog=None)

        self.__initialize_app(app_page)
        self.__configure_window(app_page)
        self.__add_items_to_page(app_page)

    def __initialize_app(self, app_page: Page):
        """
        Initialize the application

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        ChangeTheme.set_initial_theme(app_page)
        EnvironmentVariables.set_initial_language(app_page)

        self.error_dialog = ErrorDialog(app_page=app_page, overlay=self.__overlay)
        self.shutdown_handler = ShutdownHandler(app_page)
        self.update_dialog = UpdateDialog(
            app_page=app_page, overlay=self.__overlay, update=self.updater.update
        )
        self.updater.update_dialog = self.update_dialog

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
        app_page.theme_mode = ChangeTheme.get_theme(app_page)
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

        video_location = self.video_location.get()

        index_ui = IndexUI(
            page=app_page,
            download=self.__download,
            video_location=video_location if video_location is not None else None,
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
            ],
            daemon=False,
        ).start()

        Thread(target=self.__overlay, args=[app_page], daemon=False).start()

        if self.checkbox.get_value():
            Thread(target=self.__check_updates, args=[app_page], daemon=False).start()

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

        urls_to_download = self.input_url.get_value()
        video_location = self.video_location.get()

        def download_one_video(url_to_download: str):
            self.urls.set(url_to_download)

            url = self.urls.get()

            can_download_video = self.__validate_download(url, app_page)

            if can_download_video:
                self.download.download(download_video)

        def download_several_videos(urls_to_download: list[str]):
            def update_gui(url_to_remove):
                urls_to_download.remove(url_to_remove)

                self.input_url.set_value("\n".join(urls_to_download))

                app_page.update(self.input_url)

            while len(urls_to_download) > 0:
                try:
                    url_to_download = urls_to_download[0]

                    self.urls.set(url_to_download)

                    url = self.urls.get()

                    can_download_video = self.__validate_download(url, app_page)

                    if can_download_video:
                        self.download.download(download_video)

                    update_gui(url)

                except Exception as error:
                    LoggingManagement.write_error(str(error))

                    url = self.urls.get()

                    if url is None:
                        return

                    update_gui(url)

                finally:
                    reset()

        try:
            Validations.validate_non_empty_url(urls_to_download)

            list_urls_to_download: list[str] = urls_to_download.splitlines()

            if len(list_urls_to_download) == 1:
                LoggingManagement.write_log("Just one video will be downloaded")
                download_one_video(list_urls_to_download[0])

            else:
                LoggingManagement.write_log("Several videos will be downloaded")
                download_several_videos(list_urls_to_download)

        except Exception as exception:
            self.error_dialog.show_error_dialog(str(exception))

            video_location = self.video_location.get()
            download_name = self.download_name.get()

            if video_location is None or download_name is None:
                return

            FileHandler.delete_file(
                path_to_file=video_location,
                download_name=download_name,
                callback=reset,
            )

        else:
            if video_location is None:
                return

            startfile(video_location)

            self.input_url.set_value("")

        finally:
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

        to_add_to_the_overlay_of_the_page = [self.shutdown_handler, self.error_dialog]

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
    def __check_updates(self, app_page: Page, is_main: bool = True):
        """
        Checks for updates and shows a dialog if a new release is available.

        Args:
            app_page (flet.Page): Reference to the app window.
            is_main (bool): Indicates if it's the main update check (default is True).
        """

        is_new_release_available = self.updater.is_new_release_available()

        if is_new_release_available:
            self.update_dialog.show_update_dialog()

        elif not is_new_release_available and not is_main:
            self.update_dialog.update_title(ExcelTextLoader.get_text(21))
            self.update_dialog.update_content(ExcelTextLoader.get_text(22))
            self.update_dialog.button_update.change_text("Ok")
            self.update_dialog.button_update.change_function(
                self.update_dialog.change_state, app_page
            )
            self.update_dialog.actions = [self.update_dialog.button_update]
            self.update_dialog.show_update_dialog()

    @check_type
    def __validate_download(self, url: str, app_page: Page) -> bool:
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
            Validations.validate_non_empty_url(url)
            and Validations.set_default_directory_or_check_selected(
                input_directory=self.input_directory,
                page=app_page,
            )
            and Validations.check_if_youtube_url(url, self.input_url)
            and Validations.check_internet_connection()
            and Validations.is_youtube_video_available(url, self.input_url)
        )


if __name__ == "__main__":
    LoggingManagement.initialize_logging()

    app(target=Main)
