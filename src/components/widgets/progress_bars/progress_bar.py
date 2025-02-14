# Third-Party libraries
from flet import Offset, Page, ProgressBar as FletProgressBar

# Standard library
from typing import Optional


class ProgressBar(FletProgressBar):
    """Create a progress bar UI"""

    def __init__(
        self,
        color: str,
        app: Page,
        value: Optional[int] = 0,
        offset_x: float = 0,
        offset_y: float = 0,
    ):
        self.app = app
        super().__init__(
            color=color, value=value, offset=Offset(offset_x, offset_y)
        )

    def update_value(self, new_value: Optional[int]):
        """
        Update the value of the progress bar.

        Args:
            new_value (int | None): The new value for the progress bar
        """

        self.value = new_value

        self.app.update(self)
