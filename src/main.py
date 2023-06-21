"""Start the app"""

from threading import Thread

from flet import Page, CrossAxisAlignment, app

from backend import Download, Validations, ShutdownHandler, Update
from components import IndexUI, ErrorDialog, UpdateDialog
from config import GetConfigJson, EnvironmentVariables, ExcelTextLoader
from control import ControlVariables
from modify_gui import ChangeTheme
from osutils import FileHandler
from utils import LoggingManagement, check_type, ENABLED_TYPE_CHECKING


class Main:
    def __init__(self, app_page: Page):
        # Class instantiation
        self.control_variables = ControlVariables()
        self.validations = Validations()
        self.updater = Update(page=app_page, update_dialog=None)

        # Set initial theme and language
        ChangeTheme.set_initial_theme(app_page)
        EnvironmentVariables.set_initial_language(app_page)

        # Instantiation of classes that depend on the window to start
        self.error_dialog = ErrorDialog(app_page=app_page, overlay=self.__overlay)
        self.shutdown_handler = ShutdownHandler(app_page)
        self.update_dialog = UpdateDialog(
            app_page=app_page, overlay=self.__overlay, update=self.updater.update
        )
        self.updater.update_dialog = self.update_dialog

        # Set initial values
        self.control_variables.set_initial_values(app_page)

        # Set window properties
        self.__configure_window(app_page)

        # Create index items
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

        # Add items to the page in a separate thread
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

        # Overlay dialogs
        Thread(target=self.__overlay, args=[app_page], daemon=False).start()

        # Run the check for available updates in a separate thread
        if self.checkbox.get_value():
            Thread(target=self.__check_updates, args=[app_page], daemon=False).start()

    @check_type
    def __configure_window(self, app_page: Page):
        """
        Configures the window properties of the app page.

        :param app_page: Reference to the app window
        """
        app_page.title = GetConfigJson.get_config_json("WINDOW", "TITLE")
        app_page.window_width = GetConfigJson.get_config_json("WINDOW", "WIDTH")
        app_page.window_height = GetConfigJson.get_config_json("WINDOW", "HIGH")
        app_page.window_center()
        app_page.horizontal_alignment = CrossAxisAlignment.CENTER
        app_page.vertical_alignment = CrossAxisAlignment.CENTER
        app_page.window_resizable = False
        app_page.window_maximizable = False
        app_page.theme_mode = ChangeTheme.get_theme(app_page)
        app_page.window_prevent_close = True
        app_page.on_window_event = lambda e: self.__event_close_window(
            event=e, app_page=app_page
        )

    def __event_close_window(self, event, app_page):
        """
        Event handler for the window close event.

        :param event: Window event data
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
        Download the video if the parameter "download video" is true, otherwise it'll download the audio of the video

        :param app_page: Is a reference to the app window

        :param download_video: boolean, if it's true it'll download the video, if it's false it'll download the audio of the video
        """

        url = self.input_url.get_value()

        self.control_variables.set_control_variable(
            control_variable="URL_VIDEO", value=url
        )

        try:
            url = self.control_variables.get_control_variable("URL_VIDEO")
            video_location = self.control_variables.get_control_variable(
                "VIDEO_LOCATION"
            )

            validations_passed = (
                self.validations.check_if_a_url_has_been_entered(url)
                and self.validations.check_if_is_url_youtube(url)
                and self.validations.check_if_directory_is_selected(
                    input_directory=self.input_directory,
                    page=app_page,
                    video_location=video_location,
                )
                and self.validations.check_internet_connection()
                and self.validations.check_if_the_video_is_available(url)
            )

            if validations_passed:
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

        :param app_page: Reference to the app window
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

        :param app_page: Reference to the app window
        """
        self.button_directory.toggle_state(app_page)
        self.button_download_video.toggle_state(app_page)
        self.button_download_audio.toggle_state(app_page)
        self.input_url.toggle_state(app_page)

    @check_type
    def __check_updates(self, app_page: Page, is_main: bool = True):
        """
        Checks for updates and shows a dialog if a new release is available.

        Retrieves the latest version information using the `is_new_release_available` method of the `updater` instance.

        If a new release is available, it shows the update dialog.
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


if __name__ == "__main__":
    if ENABLED_TYPE_CHECKING:
        LoggingManagement.initialize_logging()

    app(target=Main)
