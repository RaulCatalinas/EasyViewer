# Core
from .core import Core


class CheckBox(Core):
    def __init__(self):
        super().__init__()

    def get(self, checkbox) -> bool:
        return self._get_control_variable(f"checkbox_{checkbox}", get_bool=True)

    def set(self, checkbox, value):
        self._set_control_variable(f"checkbox_{checkbox}", value)
