# Standard library
from datetime import datetime, timedelta


# App enums
from app_enums import UserPreferencesKeys

# Constants
from constants import CHECK_INTERVAL_DAYS


def has_one_month_passed() -> bool:
    """
    Checks if at least one month (30 days) has passed since the last update check.

    Returns:
        bool: True if a month has passed, False otherwise.
    """

    if "UserPreferencesManager" not in globals():
        from user_preferences.user_preferences_manager import (
            UserPreferencesManager,
        )

    user_preferences_manager = UserPreferencesManager()

    last_check_str = user_preferences_manager.get_preference(
        UserPreferencesKeys.LAST_UPDATE_CHECK
    )

    last_check_date = datetime.strptime(last_check_str, "%Y-%m-%d")

    next_check_date = last_check_date + timedelta(days=CHECK_INTERVAL_DAYS)

    return datetime.now() >= next_check_date
