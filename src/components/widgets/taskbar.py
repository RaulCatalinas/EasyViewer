"""
Control the logic of the taskbar
"""

# Third-Party libraries
from flet import AppBar

# Utils
from utils import check_type


class TaskBar(AppBar):
    """
    Create a taskbar
    """

    @check_type
    def __init__(self, items: list):
        super().__init__(
            actions=items,
            toolbar_height=63,
        )

    @check_type
    def change_height(self, new_height: int):
        """
        Changes the height of the taskbar.

        Args:
            new_height (int): The new height for the taskbar
        """

        self.toolbar_height = new_height
