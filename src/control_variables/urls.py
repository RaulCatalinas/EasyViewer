# Core
from .core import Core


class URLs(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> str:
        return self._get_control_variable("URL_VIDEO")

    def set(self, url):
        self._set_control_variable("URL_VIDEO", url)
