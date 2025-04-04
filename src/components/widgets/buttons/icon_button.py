# Standard Library
from typing import Callable, Optional

# Third-Party libraries
from flet import IconButton as FletIconButton, Offset, Alignment, Icons, Page

# Base
from ._base import BaseButton


class IconButton(FletIconButton, BaseButton):
    """
    Creates a button of type IconButton.
    """

    def __init__(
        self,
        app: Page,
        icon: Icons,
        function: Callable,
        offset_x: float = 0,
        offset_y: float = 0,
        scale: float = 1,
        alignment: Optional[Alignment] = None,
        visible: Optional[bool] = None,
        tooltip_text: Optional[str] = None,
    ):
        BaseButton.__init__(self, app)

        super().__init__(
            icon=icon,
            on_click=function,
            scale=scale,
            offset=Offset(offset_x, offset_y),
            alignment=alignment,
            visible=visible,
            tooltip=tooltip_text,
        )

    def change_icon(self, new_icon: Icons):
        """
        Change the button icon

        Args:
            new_icon (Icons): The new icon for the button.
        """

        self.icon = new_icon
