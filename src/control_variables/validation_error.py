# Core
from .core import Core


class ValidationError(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> bool | None:
        return self._get_control_variable("validation_error", get_bool=True)

    def set(self, validation_error):
        self._set_control_variable("validation_error", validation_error)
