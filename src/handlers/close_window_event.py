# Standard library
from typing import Callable

# Third party libraries
from flet import WindowEvent, WindowEventType


def handle_close_window_event(event: WindowEvent, on_close_callback: Callable):
    """Handle the close window event."""

    if event.type == WindowEventType.CLOSE:
        on_close_callback()
