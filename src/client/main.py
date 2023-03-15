"""Create the GUI of the program"""

from threading import Thread
from tkinter.messagebox import showerror

from app_logic.close import Close
from app_logic.download import Download
from app_logic.select_directory import SelectDirectory
from app_logic.validations import Validations
from client.app_settings import AppSettings
from create_buttons import CreateButton
from create_entrys import CreateEntrys
from create_labels import CreateLabel
from create_window import CreateWindow
from options_menu import OptionsMenu
from progression_bar import ProgressionBar
from taskbar import TaskBar

app_settings = AppSettings()
validations = Validations()

window = CreateWindow(
    background_color=app_settings.get_config_json("COLORS", "BLACK"),
    window_title=app_settings.get_config_json("WINDOW", "TITLE"),
    width=app_settings.get_config_json("WINDOW", "WIDTH"),
    high=app_settings.get_config_json("WINDOW", "HIGH"),
    icon=app_settings.get_icon(),
)

from app_logic.control_variables import LINK_VIDEO, VIDEO_LOCATION

Close(
    parent=window,
    background_color=app_settings.get_config_json("COLORS", "BLACK"),
    color_exit_button_mouse_in=app_settings.get_config_json("COLORS", "RED"),
    color_button_exit_mouse_out=app_settings.get_config_json("COLORS", "DARK_RED"),
    color_button_minimize_mouse_in=app_settings.get_config_json("COLORS", "ORANGE"),
    color_button_minimize_mouse_out=app_settings.get_config_json(
        "COLORS", "DARK_ORANGE"
    ),
    color_button_cancel_mouse_in=app_settings.get_config_json("COLORS", "YELLOW"),
    color_button_cancel_mouse_out=app_settings.get_config_json("COLORS", "DARK_YELLOW"),
    width=app_settings.get_config_json("WINDOW_CONTROL_CLOSE", "WIDTH"),
    high=app_settings.get_config_json("WINDOW_CONTROL_CLOSE", "HIGH"),
    color_label=app_settings.get_config_json("COLORS", "BLUE_LABELS"),
)

menu = OptionsMenu(window=window, text_to_copy=LINK_VIDEO)


class Main:
    """
    Create the GUI for the program.
    """

    def __init__(self):
        TaskBar(window=window, update_text_widgets=self.__update_text_widgets)

        self.label_url = CreateLabel(
            text=app_settings.get_config_excel(excel_column_number=0),
            y_axis_position=10,
            width=30,
            background_color=app_settings.get_config_json("COLORS", "BLUE_LABELS"),
            font="Helvetica",
            font_size=18,
            window=window,
        )

        self.entry_url = CreateEntrys(
            window=window,
            textvariable=LINK_VIDEO,
            font="Helvetica",
            font_size=15,
            width=70,
            y_axis_position=20,
        )

        window.bind("<Button-3>", menu.create_menu_of_options)

        self.label_location_video = CreateLabel(
            text=app_settings.get_config_excel(excel_column_number=1),
            y_axis_position=10,
            width=30,
            background_color=app_settings.get_config_json("COLORS", "BLUE_LABELS"),
            font="Helvetica",
            font_size=18,
            window=window,
        )

        self.entry_location_video = CreateEntrys(
            window=window,
            textvariable=VIDEO_LOCATION,
            font="Helvetica",
            font_size=15,
            width=70,
            y_axis_position=20,
        )

        self.button_select_location = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=2),
            y_axis_position=10,
            width=20,
            background_color=app_settings.get_config_json("COLORS", "DARK_GREEN"),
            function=lambda: [SelectDirectory(VIDEO_LOCATION)],
            font="Helvetica",
            font_size=16,
            window=window,
            color_mouse_in=app_settings.get_config_json("COLORS", "GREEN"),
            color_mouse_out=app_settings.get_config_json("COLORS", "DARK_GREEN"),
            absolute_position=True,
        )

        self.button_download_video = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=3),
            x_axis_position=220,
            y_axis_position=322,
            width=15,
            background_color=app_settings.get_config_json("COLORS", "DARK_YELLOW"),
            function=lambda: [
                Thread(target=self.__download_video, daemon=True).start()
            ],
            font="Helvetica",
            font_size=15,
            window=window,
            color_mouse_in=app_settings.get_config_json("COLORS", "YELLOW"),
            color_mouse_out=app_settings.get_config_json("COLORS", "DARK_YELLOW"),
            absolute_position=False,
        )

        self.button_download_audio = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=4),
            x_axis_position=420,
            y_axis_position=322,
            width=15,
            background_color=app_settings.get_config_json("COLORS", "DARK_YELLOW"),
            function=lambda: [
                Thread(target=self.__download_audio, daemon=True).start()
            ],
            font="Helvetica",
            font_size=15,
            window=window,
            color_mouse_in=app_settings.get_config_json("COLORS", "YELLOW"),
            color_mouse_out=app_settings.get_config_json("COLORS", "DARK_YELLOW"),
            absolute_position=False,
        )

        # Create the progress bar label
        self.label_progression_download = CreateLabel(
            text=app_settings.get_config_excel(excel_column_number=5),
            y_axis_position=97,
            width=20,
            background_color=app_settings.get_config_json("COLORS", "BLUE_LABELS"),
            font="Helvetica",
            font_size=18,
            window=window,
        )

        self.progression_bar = ProgressionBar(
            window=window,
            x_axis_position=13,
            y_axis_position=470,
        )

    def __download_video(self, *args, **kwargs):
        print(args)
        print()
        print(kwargs)

        try:
            if (
                validations.check_if_a_url_has_been_entered(LINK_VIDEO)
                and validations.check_if_is_url_youtube(LINK_VIDEO)
                and validations.check_if_directory_is_selected(
                    VIDEO_LOCATION,
                )
                and validations.check_internet_connection()
                and validations.check_if_the_video_is_available(LINK_VIDEO)
            ):
                Download(
                    progress_bar=self.progression_bar,
                    video_download_button=self.button_download_video,
                    audio_download_button=self.button_download_audio,
                    button_select_location=self.button_select_location,
                    entry_url=self.entry_url,
                    entry_location_video=self.entry_location_video,
                    download_video=True,
                )
        except Exception as e:
            showerror("Error", str(e))

    def __download_audio(self, *args, **kwargs):
        print(args)
        print()
        print(kwargs)

        try:
            if (
                validations.check_if_a_url_has_been_entered(LINK_VIDEO)
                and validations.check_if_is_url_youtube(LINK_VIDEO)
                and validations.check_if_directory_is_selected(
                    VIDEO_LOCATION,
                )
                and validations.check_internet_connection()
                and validations.check_if_the_video_is_available(LINK_VIDEO)
            ):
                Download(
                    progress_bar=self.progression_bar,
                    video_download_button=self.button_download_video,
                    audio_download_button=self.button_download_audio,
                    button_select_location=self.button_select_location,
                    entry_url=self.entry_url,
                    entry_location_video=self.entry_location_video,
                    download_video=False,
                )
        except Exception as e:
            showerror("Error", str(e))

    def __update_text_widgets(self):
        self.label_url.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=0)
        )
        self.label_location_video.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=1)
        )
        self.button_select_location.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=2)
        )
        self.button_download_video.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=3)
        )
        self.button_download_audio.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=4)
        )
        self.label_progression_download.update_text(
            new_text=app_settings.get_config_excel(excel_column_number=5)
        )


Main()

window.update_window()
