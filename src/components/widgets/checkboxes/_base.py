# Standard library
from typing import Callable

# Third-party libraries
from flet import Checkbox as FletCheckbox, Offset

# Control variables
from control_variables import CheckBox


class BaseCheckbox(FletCheckbox):
    """
    Base class for custom checkboxes.
    """

    def __init__(
        self,
        label: str,
        storage_key: str,
        callback: Callable,
        default_value: bool,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        self.storage = CheckBox()
        self.storage_key = storage_key
        self.callback = callback
        initial_value = self._load_value(storage_key, default_value)

        super().__init__(
            label=label,
            offset=Offset(offset_x, offset_y),
            value=initial_value,
            on_change=lambda e: self._on_change(),
        )

    def set_label(self, new_label: str):
        """Sets a new label for the checkbox."""

        self.label = new_label

    def change_offset(self, offset_x: int, offset_y: int):
        """Changes the checkbox offset."""

        self.offset = Offset(offset_x, offset_y)

    def _load_value(self, storage_key: str, default_value: bool) -> bool:
        """
        Loads the checkbox value from storage.

        Args:
            storage_key (str): Storage key.
            default_value (bool): Default value if key is not found.

        Returns:
            bool: Retrieved value or default.
        """
        return self.storage.get(storage_key) or default_value

    def get_value(self):
        """Returns the current value of the checkbox."""

        return self.value

    def _on_change(self):
        """Executes functions when the checkbox value changes."""

        self.callback()
        self.storage.set(self.storage_key, self.value)
