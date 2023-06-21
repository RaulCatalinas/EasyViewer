from typing import Callable

from flet import Checkbox, Offset, Page

from control import ControlVariables
from utils import check_type


class CreateCheckbox(Checkbox):
    @check_type
    def __init__(
        self,
        label: str,
        label_position: str,
        page: Page,
        callback: Callable,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        self.page = page
        self.callback = callback
        self.control_variables = ControlVariables()

        super().__init__(
            label=label,
            label_position=label_position,
            offset=Offset(offset_x, offset_y),
            on_change=lambda e: [
                self.callback(),
                self.control_variables.set_control_variable(
                    "checkbox_value", self.value
                ),
            ],
            value=self.control_variables.get_control_variable("checkbox_value"),
        )

    def get_value(self):
        return self.value

    @check_type
    def set_label(self, new_label: str):
        self.label = new_label

    @check_type
    def change_offset(self, offset_x: int, offset_y: int):
        self.offset = Offset(offset_x, offset_y)
