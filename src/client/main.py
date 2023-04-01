"""Start the app"""

from add_to_pythonpath import add_to_pythonpath

add_to_pythonpath()


from threading import Thread

import flet as ft

from app_logic.confirm_close import ConfirmClose
from app_logic.control_variables import ControlVariables
from app_logic.download import Download
from app_logic.select_directory import SelectDirectory
from app_logic.validations import Validations
from app_settings import AppSettings
from create_buttons import CreateIconButton, CreateElevatedButton
from create_inputs import CreateInputs
from progressbar import CreateProgressBar
from taskbar import TaskBar
from create_dialog import CreateDialog


class Main(AppSettings, Validations, ControlVariables):
    def __init__(self, page: ft.Page):
        AppSettings.__init__(self)
        Validations.__init__(self)
        ControlVariables.__init__(self)

        VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

        # Set the window title and resize it
        page.title = self.get_config_json("WINDOW", "TITLE")
        page.window_width = self.get_config_json("WINDOW", "WIDTH")
        page.window_height = self.get_config_json("WINDOW", "HIGH")

        # Center window
        page.window_center()

        # Center elements
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.CrossAxisAlignment.CENTER

        # Set window size
        page.window_resizable = False
        page.window_maximizable = False

        # Set user selected color theme
        page.theme_mode = page.client_storage.get("theme")

        # Window close confirmation
        page.window_prevent_close = True

        self.confirm_dialog = ConfirmClose(page)

        def __event_close_window(event):
            if event.data == "close":
                page.dialog = self.confirm_dialog
                self.confirm_dialog.show_close_dialog(page)

        page.on_window_event = __event_close_window

        self.input_url = CreateInputs(
            placeholder_input=self.get_config_excel(14),
            text_size_input=20,
            keyboard_type_input=ft.KeyboardType.URL,
            text_align_input=ft.TextAlign.CENTER,
            autofocus_input=True,
        )

        self.input_directory = CreateInputs(
            placeholder_input=self.get_config_excel(15),
            text_size_input=20,
            text_align_input=ft.TextAlign.CENTER,
            read_only_input=True,
            offset_input=ft.Offset(0, 0.5),
            value_input=VIDEO_LOCATION if VIDEO_LOCATION != "" else None,
        )

        self.button_directory = CreateIconButton(
            icon_button=ft.icons.FOLDER,
            function=lambda e: SelectDirectory(
                page=page,
                confirm_dialog=self.confirm_dialog,
                input_directory=self.input_directory,
            ),
            offset_button=ft.Offset(0, 1.5),
            scale_button=2.5,
        )

        self.button_download_video = CreateIconButton(
            icon_button=ft.icons.VIDEO_FILE,
            function=lambda e: [
                Thread(target=self.download_video(page), daemon=True).start()
            ],
            offset_button=ft.Offset(-0.9, 2.5),
            scale_button=2.5,
        )

        self.button_download_audio = CreateIconButton(
            icon_button=ft.icons.AUDIO_FILE,
            function=lambda e: [
                Thread(target=self.download_audio(page), daemon=True).start()
            ],
            offset_button=ft.Offset(1, 1.3),
            scale_button=2.5,
        )

        self.progress_bar = CreateProgressBar(
            color_progressbar=self.get_config_json("COLORS", "GREEN"),
            value_progressbar=0,
            offset_progressbar=ft.Offset(0, 23),
        )

        self.taskbar = TaskBar(
            page=page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=self.confirm_dialog,
        )

        page.add(
            self.input_url,
            self.input_directory,
            self.button_directory,
            self.button_download_video,
            self.button_download_audio,
            self.progress_bar,
            self.taskbar,
        )

    def download_video(self, page):
        self.set_control_variable("URL_VIDEO", self.input_url.value)

        URL = self.get_control_variables("URL_VIDEO")
        VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

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
                    download_video=False,
                )
        except Exception as exc:
            self.__show_dialog_error(error=str(exc), page=page)

    def download_audio(self, page):
        self.set_control_variable("URL_VIDEO", self.input_url.value)

        URL = self.get_control_variables("URL_VIDEO")
        VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

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
                    download_video=False,
                )
        except Exception as exc:
            self.__show_dialog_error(error=str(exc), page=page)

    def __show_dialog_error(self, error, page):
        button_close_dialog = CreateElevatedButton(
            text_button="Ok", function=lambda e: __change_state_dialog()
        )

        dialog_error = CreateDialog(
            icon=True,
            title_dialog=ft.icons.ERROR,
            title_size=1.3,
            content_dialog=error,
            content_size=23,
            actions_dialog=[button_close_dialog],
            actions_alignment_dialog=ft.MainAxisAlignment.END,
        )

        dialog_error.change_state_dialog(page)

        def __change_state_dialog():
            return dialog_error.change_state_dialog(page)


ft.app(target=Main)
