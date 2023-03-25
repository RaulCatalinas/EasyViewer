from flet import ProgressBar


class CreateProgressBar(ProgressBar):
    def __init__(self, color_progressbar, value_progressbar, offset_progressbar):
        self.color_progressbar = color_progressbar
        self.value_progressbar = value_progressbar
        self.offset_progressbar = offset_progressbar

    def _build(self):
        return super().__init__(
            color=self.color_progressbar,
            value=self.value_progressbar,
            offset=self.offset_progressbar,
        )
