# Third party libraries
from flet import Page, app

# Managers
from managers import WindowManager
from managers import MainUIManager

# Dialogs
from components.dialogs.warnings import CloseAppDialog

# Handlers
from handlers import handle_close_window_event


class Main:
    def __init__(self, page: Page):
        self.app = page
        self.close_app_dialog = CloseAppDialog(self.app)

        WindowManager(
            self.app,
            lambda event: handle_close_window_event(
                event, self.close_app_dialog.show_dialog
            ),
        )
        MainUIManager(self.app)


if __name__ == "__main__":
    app(Main)
