from enum import StrEnum


class UserPreferencesKeys(StrEnum):
    THEME = "theme"
    AUTOMATIC_NOTIFICATIONS = "automatic_notifications"
    LANGUAGE = "language"
    LATEST_GITHUB_VERSION = "latest_github_version"
    DISCLAIMER_SHOWN = "disclaimer_shown"
    LAST_UPDATE_CHECK = "last_update_check"
    DOWNLOAD_DIRECTORY = "download_directory"
    UPGRADE_AVAILABLE = "upgrade_available"
