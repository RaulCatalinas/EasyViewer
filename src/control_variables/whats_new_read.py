# Core
from .core import Core


class WhatsNewRead(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> bool | None:
        return self._get_control_variable("whats_new_read", get_bool=True)

    def set(self, whats_new_read):
        self._set_control_variable("whats_new_read", whats_new_read)
