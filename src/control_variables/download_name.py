# Core
from .core import Core


class DownloadName(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> str:
        return self._get_control_variable("DOWNLOAD_NAME")

    def set(self, download_name):
        self._set_control_variable("DOWNLOAD_NAME", download_name)
