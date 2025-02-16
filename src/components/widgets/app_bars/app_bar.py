# Standard library
from typing import Optional

# Third-Party libraries
from flet import AppBar as FletAppBar, Control


class AppBar(FletAppBar):
    def __init__(
        self,
        window_elements: list[Control],
        height: int,
        bg_color: Optional[str] = None,
    ):
        super().__init__(
            actions=window_elements, toolbar_height=height, bgcolor=bg_color
        )
