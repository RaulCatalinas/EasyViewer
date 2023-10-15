# Core
from .core import Core


class VideoLocation(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> str | None:
        return self._get_control_variable("VIDEO_LOCATION")

    def set(self, video_location):
        self._set_control_variable("VIDEO_LOCATION", video_location)
