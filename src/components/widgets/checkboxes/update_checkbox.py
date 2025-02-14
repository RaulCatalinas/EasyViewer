# Standard library
from typing import Callable

# Third-party libraries
from flet import LabelPosition

# Base
from ._base import BaseCheckbox


class UpdateCheckbox(BaseCheckbox):
    """
    Custom checkbox with additional functionality.
    """

    def __init__(
        self,
        label: str,
        label_position: LabelPosition,
        callback: Callable,
        offset_x=0,
        offset_y=0,
    ):
        self.label_position = label_position
        super().__init__(label, "update", callback, True, offset_x, offset_y)
