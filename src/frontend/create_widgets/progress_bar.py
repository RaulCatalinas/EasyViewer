"""Create a progress bar"""

from flet import ProgressBar, Offset


class CreateProgressBar(ProgressBar):
    """Create a progress bar"""

    def __init__(self, color_progressbar, value_progressbar, offset_x=0, offset_y=0):
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

    def update_progress_bar(self, new_value, page):
        """
        Updates the progress bar

        :param new_value: The new value to set to the progress bar.

        :param page: Is a reference to the app window
        """

        self.value = new_value

        page.update(self)
