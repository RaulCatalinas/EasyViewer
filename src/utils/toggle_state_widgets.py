# Utils
from utils import check_type

# Third-Party libraries
from flet import Page


@check_type
def toggle_state_widgets(widgets: list, app_page: Page):
    """
    Toggle the state of various widgets.

    Args:
        widgets (list): list of widgets to toggle state
        app_page (flet.Page): Reference to the app window.
    """

    for widget in widgets:
        widget.toggle_state(app_page)
