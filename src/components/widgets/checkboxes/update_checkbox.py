# Standard library
from typing import Callable

# Third-Party libraries
from flet import LabelPosition

# Base
from ._base import BaseCheckbox

# App enums
from app_enums import UserPreferencesKeys, ExcelTextLoaderKeys

# i18n
from i18n import ExcelTextLoader


class UpdateCheckbox(BaseCheckbox):
    """
    Custom checkbox with additional functionality.
    """

    def __init__(
        self, callback: Callable, offset_x: float = 0, offset_y: float = 0
    ):
        self.excel_text_loader = ExcelTextLoader()
        super().__init__(
            label=self.excel_text_loader.get_text(
                ExcelTextLoaderKeys.CHECK_UPDATES
            ),
            storage_key=UserPreferencesKeys.AUTOMATIC_NOTIFICATIONS,
            callback=callback,
            default_value=True,
            label_position=LabelPosition.LEFT,
            offset_x=offset_x,
            offset_y=offset_y,
        )
