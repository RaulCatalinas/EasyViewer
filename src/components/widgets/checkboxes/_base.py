# Standard library
from typing import Callable, Optional

# Third-party libraries
from flet import Checkbox as FletCheckbox, Offset, LabelPosition

# User Preferences
from user_preferences import UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys


class BaseCheckbox(FletCheckbox):
    """
    Base class for custom checkboxes.
    """

    def __init__(
        self,
        label: str,
        storage_key: UserPreferencesKeys,
        callback: Callable,
        default_value: bool,
        label_position: Optional[LabelPosition] = None,
        offset_x: float = 0,
        offset_y: float = 0,
    ):
        self.user_preferences_manager = UserPreferencesManager()
        self.storage_key = storage_key
        self.callback = callback
        initial_value = self._load_value(default_value)

        super().__init__(
            label=label,
            offset=Offset(offset_x, offset_y),
            value=initial_value,
            on_change=lambda _: self._on_change(),
            label_position=label_position,
        )

    def set_label(self, new_label: str):
        """Sets a new label for the checkbox."""

        self.label = new_label

    def change_offset(self, offset_x: int, offset_y: int):
        """Changes the checkbox offset."""

        self.offset = Offset(offset_x, offset_y)

    def _load_value(self, default_value: bool) -> bool:
        """
        Loads the checkbox value from storage.

        Args:
            default_value (bool): Default value if key is not found.

        Returns:
            bool: Retrieved value or default.
        """

        return self.user_preferences_manager.get_preference(self.storage_key)

    def get_value(self):
        """Returns the current value of the checkbox."""

        return self.value

    def _on_change(self):
        """Executes functions when the checkbox value changes."""

        self.user_preferences_manager.set_preference(
            self.storage_key, self.value
        )
        self.callback()
