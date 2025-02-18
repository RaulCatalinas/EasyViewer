from enum import StrEnum


class UserPreferencesKeys(StrEnum):
    THEME = "theme"
    AUTOMATIC_NOTIFICATIONS = "automatic_notifications"
    LANGUAGE = "language"
    PREVIOUS_APP_VERSION = "previous_app_version"
    DISCLAIMER_SHOWN = "disclaimer_shown"
