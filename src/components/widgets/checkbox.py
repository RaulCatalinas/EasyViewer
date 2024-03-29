# Standard library
from typing import Callable

# Third-Party libraries
from flet import LabelPosition, Offset, Page, Checkbox as FletCheckbox

# Control variables
from control_variables import CheckBox

# Utils
from utils import check_type


class Checkbox(FletCheckbox):
    @check_type
    def __init__(
        self,
        label: str,
        label_position: LabelPosition,
        page: Page,
        callback: Callable,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        self.page = page
        self.callback = callback
        self.checkbox_instance = CheckBox()

        super().__init__(
            label=label,
            label_position=label_position,
            offset=Offset(offset_x, offset_y),
            on_change=lambda e: self.__on_change(),
            value=self.__get_value_from_ini("update", True),
        )

    def get_value(self):
        """
        Gets the value of the checkbox

        Returns:
            bool: The value of the checkbox
        """

        return self.value

    @check_type
    def set_label(self, new_label: str):
        """
        Set a new label for the checkbox

        Args:
            new_label (str): The new label for the checkbox
        """

        self.label = new_label

    @check_type
    def change_offset(self, offset_x: int, offset_y: int):
        """
        Change the checkbox offset

        Args:
            offset_x (int): Offset in x-axis
            offset_y (int): Offset in the y-axis
        """

        self.offset = Offset(offset_x, offset_y)

    def __on_change(self):
        """
        Functions that are executed when the value of the checkbox changes
        """
        self.callback()
        self.checkbox_instance.set("update", self.value)

    def __get_value_from_ini(self, key: str, default_value: bool) -> bool:
        """
        Gets the value of the checkbox from the INI file

        Args:
            key (str): _description_
            default_value (bool): Default value for the checkbox

        Returns:
            bool: The value of the checkbox
        """

        value = self.checkbox_instance.get(key)

        return value if value is not None else default_value
