# Third party libraries
from flet import Icons, Page

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar
from components.dialogs.updates import UpdateDialog

# Managers
from .settings_ui_manager import SettingsUIManager

# App settings
from app_settings import AppColors

# Update manager
from update import UpdateManager


class MainUIManager:
    def __init__(self, app: Page):
        self.app = app
        update_dialog = UpdateDialog(app, self.update_manager.update)
        self.update_manager = UpdateManager(update_dialog)

        self._initialize_ui()

    def _initialize_ui(self):
        """Initialises the UI elements and adds them to the app."""

        SettingsUIManager(self.app, self.update_manager)
        self.app.add(
            Input(
                placeholder="Video URL",
                text_size=20,
                autofocus=True,
                is_multiline=True,
                max_height=2,
                offset_y=0.5,
            ),
            Input(
                placeholder="Directory",
                text_size=20,
                read_only=True,
                offset_y=1,
            ),
            IconButton(
                icon=Icons.FOLDER,
                function=lambda _: print("Selecting directory"),
                offset_x=9.42,
                offset_y=2.02,
                scale=2.5,
            ),
            IconButton(
                icon=Icons.AUDIO_FILE,
                function=lambda _: print("Downloading audio"),
                offset_x=8.4,
                offset_y=2.79,
                scale=2.5,
            ),
            IconButton(
                icon=Icons.VIDEO_FILE,
                function=lambda _: print("Downloading video"),
                offset_x=10.45,
                offset_y=1.56,
                scale=2.5,
            ),
            ProgressBar(
                color=AppColors.PROGRESS_BAR_COLOR.value,
                offset_y=25,
                app=self.app,
            ),
        )
