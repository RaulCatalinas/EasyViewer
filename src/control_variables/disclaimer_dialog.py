# Core
from .core import Core


class DisclaimerDialogControlVariable(Core):
    def __init__(self):
        super().__init__()

    def get(self) -> bool | None:
        return self._get_control_variable("disclaimer_dialog", get_bool=True)

    def set(self, disclaimer_dialog):
        self._set_control_variable("disclaimer_dialog", disclaimer_dialog)
