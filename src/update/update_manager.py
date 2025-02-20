# Standard library
from threading import Thread
from datetime import datetime, timedelta
from webbrowser import open_new_tab

# App enums
from app_enums import UserPreferencesKeys

# Utils
from utils import get_github_version

# User preferences
from user_preferences import UserPreferencesManager

# Constants
from constants import INSTALLED_VERSION, CHECK_INTERVAL_DAYS, DOWNLOAD_PAGE_URL

# Components
from components.dialogs.updates import UpdateDialog


class UpdateManager:
    """Manages update checks in a background thread, running once per month."""

    def __init__(self, update_dialog: UpdateDialog):
        self.update_dialog = update_dialog
        self.user_preferences_manager = UserPreferencesManager()

        self._start_background_update_check()

    def _start_background_update_check(self) -> None:
        """Starts a background thread to check for updates if needed."""

        Thread(target=self._check_for_updates_if_needed, daemon=True).start()

    def _check_for_updates_if_needed(self) -> None:
        """Checks if an update check is needed before querying the API."""

        last_check_str: str = self.user_preferences_manager.get_preference(
            UserPreferencesKeys.LAST_UPDATE_CHECK
        )

        last_check_date = datetime.strptime(last_check_str, "%Y-%m-%d")

        next_check_date = last_check_date + timedelta(days=CHECK_INTERVAL_DAYS)

        if datetime.now() >= next_check_date:
            self._an_update_is_available()

    def _an_update_is_available(self):
        """Fetches the latest release from GitHub and updates preferences if needed."""

        latest_github_version = get_github_version()

        today_str = datetime.now().strftime("%Y-%m-%d")

        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.LAST_UPDATE_CHECK, today_str
        )

        return INSTALLED_VERSION < latest_github_version

    def _notify_update(self, an_update_is_available: bool) -> None:
        """
        Displays the update dialog to notify the user about available updates.

        Args:
            an_update_is_available (bool): True if an update is available, False otherwise.
        """
        self.update_dialog.show_dialog(an_update_is_available)

    def update(self) -> None:
        """
        Opens the download page for the latest version in a new browser tab.
        """

        open_new_tab(DOWNLOAD_PAGE_URL)

    def check_updates(self, checking_for_updates_manually=False) -> None:
        """
        Checks for available updates and notifies the user only when necessary.

        Args:
            checking_for_updates_manually (bool): True if the user manually triggered the check, False if automatic.
        """

        an_update_is_available = self._an_update_is_available()

        if an_update_is_available:
            self._notify_update(True)

        elif checking_for_updates_manually:
            self._notify_update(False)
