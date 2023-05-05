"""
Start the app
"""

from threading import Thread

from flet import (
    Page,
    icons,
    CrossAxisAlignment,
    KeyboardType,
    TextAlign,
    app,
    MainAxisAlignment,
)

from backend import SelectDirectory, Download, Validations
from config import GetConfigJson, GetConfigExcel, EnvironmentVariables
from control import ReadControlVariables, WriteControlVariables
from create_widgets import (
    CreateDialog,
    CreateIconButton,
    CreateElevatedButton,
    CreateInputs,
    CreateProgressBar,
    TaskBar,
)
from modify_gui import ChangeTheme
from osutils import FileHandler
from shutdown_handler import ShutdownHandler


class Main(Validations):
    """
    Start the app
    """

    def __init__(self, page: Page):
        super().__init__()

        EnvironmentVariables.set_initial_language(page)
        WriteControlVariables.set_initial_values(page)

        self.shutdown_handler = ShutdownHandler(page)

        if ChangeTheme.get_theme(page) is None:
            ChangeTheme.set_default_theme(page)

        VIDEO_LOCATION = ReadControlVariables.get("VIDEO_LOCATION")

        # Set the window title and resize it
        page.title = GetConfigJson.get_config_json("WINDOW", "TITLE")
        page.window_width = GetConfigJson.get_config_json("WINDOW", "WIDTH")
        page.window_height = GetConfigJson.get_config_json("WINDOW", "HIGH")

        # Center window
        page.window_center()

        # Center elements
        page.horizontal_alignment = CrossAxisAlignment.CENTER
        page.vertical_alignment = CrossAxisAlignment.CENTER

        # Set window size
        page.window_resizable = False
        page.window_maximizable = False

        # Set user selected color theme
        page.theme_mode = ChangeTheme.get_theme(page)

        # Window close confirmation
        page.window_prevent_close = True

        def __event_close_window(event):
            if event.data == "close":
                self.__overlay(page)
                page.dialog = self.shutdown_handler

                if self.error_dialog.open:
                    self.error_dialog.change_state(page)

                self.shutdown_handler.change_state(page)

        page.on_window_event = __event_close_window

        # Error dialog
        self.button_close_dialog = CreateElevatedButton(
            text_button="Ok", function=lambda e: None
        )

        self.error_dialog = CreateDialog(
            icon=True,
            title_dialog=icons.ERROR,
            title_size=1.3,
            content_dialog="",
            content_size=23,
            actions_dialog=[self.button_close_dialog],
            actions_alignment_dialog=MainAxisAlignment.END,
        )

        self.input_url = CreateInputs(
            placeholder_input=GetConfigExcel.get_config_excel(14),
            text_size_input=20,
            keyboard_type_input=KeyboardType.URL,
            text_align_input=TextAlign.CENTER,
            autofocus_input=True,
        )

        self.input_directory = CreateInputs(
            placeholder_input=GetConfigExcel.get_config_excel(15),
            text_size_input=20,
            text_align_input=TextAlign.CENTER,
            read_only_input=True,
            offset_y=0.5,
            value_input=VIDEO_LOCATION if VIDEO_LOCATION != "None" else None,
        )

        self.select_directory = SelectDirectory(
            page=page,
            input_directory=self.input_directory,
            set_control_variable_in_ini=WriteControlVariables.set,
        )

        self.button_directory = CreateIconButton(
            icon_button=icons.FOLDER,
            function=lambda e: self.select_directory.select_directory(),
            offset_y=1.5,
            scale_button=2.5,
        )

        self.button_download_video = CreateIconButton(
            icon_button=icons.VIDEO_FILE,
            function=lambda e: [
                Thread(target=self.__download, args=[page, True], daemon=True).start()
            ],
            offset_x=-0.9,
            offset_y=2.5,
            scale_button=2.5,
        )

        self.button_download_audio = CreateIconButton(
            icon_button=icons.AUDIO_FILE,
            function=lambda e: [
                Thread(target=self.__download, args=[page, False], daemon=True).start()
            ],
            offset_x=1,
            offset_y=1.3,
            scale_button=2.5,
        )

        self.progress_bar = CreateProgressBar(
            color_progressbar=GetConfigJson.get_config_json("COLORS", "GREEN"),
            value_progressbar=0,
            offset_y=23,
        )

        self.taskbar = TaskBar(
            page=page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=self.shutdown_handler,
            button_exit_the_app=self.shutdown_handler.button_exit_the_app,
        )

        Thread(target=self.__add, args=[page], daemon=False).start()
        Thread(target=self.__overlay, args=[page], daemon=False).start()

    def __download(self, page, download_video):
        """
        Download the video if the parameter "download video" is true, otherwise it'll download the audio of the video

        :param page: Is a reference to the app window

        :param download_video: boolean, if it's true it'll download the video, if it's false it'll download the audio of the video
        """

        WriteControlVariables.set("URL_VIDEO", self.input_url.get_value())

        URL = ReadControlVariables.get("URL_VIDEO")
        VIDEO_LOCATION = ReadControlVariables.get("VIDEO_LOCATION")

        try:
            if (
                self.check_if_a_url_has_been_entered(URL)
                and self.check_if_is_url_youtube(URL)
                and self.check_if_directory_is_selected(
                    input_directory=self.input_directory,
                    page=page,
                    video_location=VIDEO_LOCATION,
                )
                and self.check_internet_connection()
                and self.check_if_the_video_is_available(URL)
            ):
                Download(
                    button_select_location=self.button_directory,
                    button_download_video=self.button_download_video,
                    button_download_audio=self.button_download_audio,
                    input_url=self.input_url,
                    download_video=download_video,
                    page=page,
                    change_state_widgets=self.__change_state_widgets,
                    reset_control_variables=self.reset,
                    update_progressbar=self.progress_bar.update_progress_bar,
                )

        except Exception as exception:
            self.__show_dialog_error(error=exception, page=page)

            FileHandler.delete_file(
                path_to_the_file=ReadControlVariables.get("VIDEO_LOCATION"),
                download_name=ReadControlVariables.get("DOWNLOAD_NAME"),
            )

            self.__change_state_widgets(page)

    def __show_dialog_error(self, error, page):
        """
        Displays a dialog with the error occurred

        :param page: Is a reference to the app window

        :param error: Error that has occurred
        """

        self.button_close_dialog.change_function(self.error_dialog.change_state, page)
        self.error_dialog.content_text.change_text(error)

        self.__overlay(page)
        page.dialog = self.error_dialog

        self.error_dialog.change_state(page)

    def __add(self, page):
        """
        Adds a list of items to a given page.

        :param page: Is a reference to the app window
        """

        ITEMS_TO_ADD_TO_THE_PAGE = [
            self.input_url,
            self.input_directory,
            self.button_directory,
            self.button_download_video,
            self.button_download_audio,
            self.progress_bar,
            self.taskbar,
            self.select_directory,
        ]

        for item in ITEMS_TO_ADD_TO_THE_PAGE:
            page.add(item)

    def __overlay(self, page):
        """
        Adds a list of dialogs to the overlay of a given page.

        :param page: Is a reference to the app window
        """

        TO_ADD_TO_THE_OVERLAY_OF_THE_PAGE = [
            self.shutdown_handler,
            self.error_dialog,
        ]

        for i in TO_ADD_TO_THE_OVERLAY_OF_THE_PAGE:
            page.overlay.append(i)

    def __change_state_widgets(self, page):
        """
        If the widgets are activated they deactivate it and vice versa

        :param page: Is a reference to the app window
        """

        self.button_directory.change_state(page)
        self.button_download_video.change_state(page)
        self.button_download_audio.change_state(page)
        self.input_url.change_state(page)


if __name__ == "__main__":
    app(target=Main)
