# Third party libraries
from flet import Icons, Page

# Components
from components.widgets.buttons import IconButton
from components.widgets.inputs import Input
from components.widgets.progress_bars import ProgressBar
from components.dialogs.updates import UpdateDialog

# Managers
from .settings_ui_manager import SettingsUIManager
from ..window_managers import SelectDirectoryManager

# App settings
from app_settings import AppColors

# Update manager
from update import UpdateManager

# App enums
from app_enums import UserPreferencesKeys

# User preferences
from user_preferences import UserPreferencesManager


class MainUIManager:
    def __init__(self, app: Page):
        self.app = app
        update_dialog = UpdateDialog(app, lambda: ())
        self.update_manager = UpdateManager(update_dialog)

        user_preferences_manager = UserPreferencesManager()

        self.input_directory = Input(
            app=self.app,
            placeholder="Directory",
            text_size=20,
            read_only=True,
            offset_y=1,
            initial_value=user_preferences_manager.get_preference(
                UserPreferencesKeys.DOWNLOAD_DIRECTORY
            ),
        )

        self.select_directory_manager = SelectDirectoryManager(
            self.input_directory
        )

        update_dialog.update_function = self.update_manager.update

        self._initialize_ui()

    def _initialize_ui(self):
        """Initialises the UI elements and adds them to the app."""

        SettingsUIManager(self.app, self.update_manager)
        self.app.add(
            self.select_directory_manager,
            Input(
                app=self.app,
                placeholder="Video URL",
                text_size=20,
                autofocus=True,
                is_multiline=True,
                max_height=2,
                offset_y=0.5,
            ),
            self.input_directory,
            IconButton(
                icon=Icons.FOLDER,
                function=lambda _: self.select_directory_manager.select_directory(),
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
