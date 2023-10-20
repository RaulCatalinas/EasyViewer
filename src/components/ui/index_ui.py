# Standard library
from threading import Thread

# Third-Party libraries
from flet import KeyboardType, TextAlign, icons

# Create widgets
from frontend.create_widgets import (
    CreateIconButton,
    CreateInputs,
    CreateProgressBar,
    TaskBar,
)

# Settings
from settings import ExcelTextLoader, GetConfigJson

# Taskbar UI
from .taskbar_ui import TaskBarUI


class IndexUI:
    def __init__(self, page, download, shutdown_handler, check_updates, video_location):
        # Backend
        from backend import SelectDirectory

        self.input_url = CreateInputs(
            placeholder=ExcelTextLoader.get_text(14),
            text_size=20,
            keyboard_type=KeyboardType.URL,
            text_align=TextAlign.CENTER,
            autofocus=True,
            is_multiline=True,
            max_height=2,
        )

        self.input_directory = CreateInputs(
            placeholder=ExcelTextLoader.get_text(15),
            text_size=20,
            text_align=TextAlign.CENTER,
            read_only=True,
            offset_y=0.5,
            value_input=video_location if video_location != "None" else None,
        )

        self.select_directory = SelectDirectory(
            page=page, input_directory=self.input_directory
        )

        self.button_directory = CreateIconButton(
            icon=icons.FOLDER,
            function=lambda e: self.select_directory.select_directory(),
            offset_y=1.5,
            scale=2.5,
        )

        self.button_download_video = CreateIconButton(
            icon=icons.VIDEO_FILE,
            function=lambda e: [
                Thread(target=download, args=[page, True], daemon=True).start()
            ],
            offset_x=-0.9,
            offset_y=2.5,
            scale=2.5,
        )

        self.button_download_audio = CreateIconButton(
            icon=icons.AUDIO_FILE,
            function=lambda e: [
                Thread(target=download, args=[page, False], daemon=True).start()
            ],
            offset_x=1,
            offset_y=1.3,
            scale=2.5,
        )

        self.progress_bar = CreateProgressBar(
            color=GetConfigJson.get_config_json("COLORS", "GREEN"),
            value=0,
            offset_y=18.5,
        )

        self.taskbar_ui = TaskBarUI(
            page=page,
            input_url=self.input_url,
            input_directory=self.input_directory,
            close_dialog=shutdown_handler,
            button_exit_the_app=shutdown_handler.button_exit_the_app,
            check_updates=check_updates,
        )

        self.taskbar = TaskBar(self.taskbar_ui.get_elements())

        self.taskbar_ui.dropdown_contact.appbar = self.taskbar
        self.taskbar_ui.dropdown_language.appbar = self.taskbar

    def get_elements(self):
        return [
            self.input_url,
            self.input_directory,
            self.button_directory,
            self.button_download_video,
            self.button_download_audio,
            self.progress_bar,
            self.taskbar,
            self.select_directory,
        ]

    def get_checkbox(self):
        """
        Get the automatic check for updates checkbox

        Returns:
            CreateCheckbox: The automatic check for updates checkbox
        """

        return self.taskbar_ui.checkbox

    def get_icon_update(self):
        """
        Get button check for updates

        Returns:
            CreateIconButton: The check button for updates
        """

        return self.taskbar_ui.icon_update
