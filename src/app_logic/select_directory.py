"""Prompts the user to select a directory for the downloaded file"""

from tkinter.filedialog import askdirectory


class SelectDirectory:
    """Controls the logic that selects a directory for the video"""

    def __init__(self, video_location):
        self.video_location = video_location

        return self.video_location.set(askdirectory(initialdir="Selected directory"))
