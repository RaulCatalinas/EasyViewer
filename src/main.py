"""Start the app"""

from threading import Thread

from backend import Download, ShutdownHandler, Update, Validations
from flet import MainAxisAlignment, Page, app
from frontend.components import ErrorDialog, IndexUI, UpdateDialog
from frontend.modify_gui import ChangeTheme

from constants import ENABLED_TYPE_CHECKING
from control_variables import ControlVariables
from osutils import FileHandler
from settings import EnvironmentVariables, ExcelTextLoader, GetConfigJson
from utils import EnumHelper, LoggingManagement, check_type


class Main:
    def __init__(self, app_page: Page):
        """
        Initializes the Main class.

        Args:
            app_page (flet.Page): Reference to the app window.
        """

        self.control_variables = ControlVariables()
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

        self.control_variables.set_initial_values(app_page)

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

        index_ui = IndexUI(
            page=app_page,
            download=self.__download,
            video_location=self.control_variables.get_control_variable(
                "VIDEO_LOCATION"
            ),
            shutdown_handler=self.shutdown_handler,
            check_updates=self.__check_updates,
        )

        (
            self.input_url,
            self.input_directory,
            self.button_directory,
            self.button_download_video,
            self.button_download_audio,
            progress_bar,
            _,
            _,
        ) = index_ui.get_elements()

        self.checkbox = index_ui.get_checkbox()

        self.download = Download(
            page=app_page,
            toggle_state_widgets=self.__toggle_state_widgets,
            update_progressbar=progress_bar.update_value,
        )

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

        url_to_save = self.input_url.get_value()
        self.control_variables.set_control_variable(
            control_variable="URL_VIDEO", value=url_to_save
        )

        try:
            url = self.control_variables.get_control_variable("URL_VIDEO")
            video_location = self.control_variables.get_control_variable(
                "VIDEO_LOCATION"
            )

            if self.__validate_download(url, app_page, video_location):
                self.download.download(download_video)

        except Exception as exception:
            self.error_dialog.show_error_dialog(str(exception))
            video_location = self.control_variables.get_control_variable(
                "VIDEO_LOCATION"
            )
            download_name = self.control_variables.get_control_variable("DOWNLOAD_NAME")
            FileHandler.delete_file(
                path_to_file=video_location,
                download_name=download_name,
                callback=self.control_variables.reset,
            )
            self.__toggle_state_widgets(app_page)
            self.control_variables.reset()

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
    def __validate_download(
        self, url: str, app_page: Page, video_location: str
    ) -> bool:
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
            and Validations.check_if_youtube_url(url)
            and Validations.set_default_directory_or_check_selected(
                input_directory=self.input_directory,
                page=app_page,
                video_location=video_location,
            )
            and Validations.check_internet_connection()
            and Validations.is_youtube_video_available(url)
        )


if __name__ == "__main__":
    if ENABLED_TYPE_CHECKING:
        LoggingManagement.initialize_logging()

    app(target=Main)
