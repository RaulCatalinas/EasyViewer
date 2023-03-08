"""Shows the download progress"""

from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar


class ProgressionBar:
    """Create a progress bar and increase the progress of it"""

    def __init__(
        self,
        window,
        x_axis_position,
        y_axis_position,
    ):
        self.window = window
        self.x_axis_position = x_axis_position
        self.y_axis_position = y_axis_position
        self.download_progression_bar = Progressbar(
            self.window, orient=HORIZONTAL, length=800
        )
        self.download_progression_bar.place(
            x=self.x_axis_position, y=self.y_axis_position
        )

    def execute_progression_bar(self):
        """
        Starts a progress bar.
        """
        self.bar_progression_download.start()

    def stop_progression_bar(self):
        """
        Stops the progress bar.
        """
        self.bar_progression_download.stop()
