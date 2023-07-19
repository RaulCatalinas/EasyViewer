from flet import Offset, Page, ProgressBar

from utils import check_type


class CreateProgressBar(ProgressBar):
    """Create a progress bar UI"""

    @check_type
    def __init__(
        self,
        color: str,
        value: int | None,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        super().__init__(
            color=color,
            value=value,
            offset=Offset(offset_x, offset_y),
        )

    @check_type
    def update_value(self, new_value: int | None, page: Page):
        """
        Update the value of the progress bar.

        Args:
            new_value (int | None): The new value for the progress bar
            page (flet.Page): Reference to the app window
        """

        self.value = new_value
        page.update(self)
