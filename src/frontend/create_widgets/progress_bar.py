"""Create a progress bar"""

from flet import ProgressBar, Offset, Page

from utils import check_type


class CreateProgressBar(ProgressBar):
    """Create a progress bar"""

    @check_type
    def __init__(
        self,
        color_progressbar: str,
        value_progressbar: int | None,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        self.color_progressbar = color_progressbar
        self.value_progressbar = value_progressbar
        self.offset_x = offset_x
        self.offset_y = offset_y

    def _build(self):
        return super().__init__(
            color=self.color_progressbar,
            value=self.value_progressbar,
            offset=Offset(self.offset_x, self.offset_y),
        )

    @check_type
    def update_progress_bar(self, new_value: int | None, page: Page):
        """
        Updates the progress bar

        :param new_value: The new value to set to the progress bar.

        :param page: Is a reference to the app window
        """

        self.value = new_value

        page.update(self)
