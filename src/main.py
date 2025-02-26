# Third party libraries
from flet import Page, app

# Managers
from managers.window_managers import WindowManager
from managers.ui_managers import MainUIManager

# Dialogs
from components.dialogs.warnings import CloseAppDialog

# Handlers
from handlers import handle_close_window_event


class Main:
    def __init__(self, page: Page):
        app = page
        close_app_dialog = CloseAppDialog(app)

        WindowManager(
            app,
            lambda event: handle_close_window_event(
                event, close_app_dialog.show_dialog
            ),
        )

        MainUIManager(app)


if __name__ == "__main__":
    app(Main)
