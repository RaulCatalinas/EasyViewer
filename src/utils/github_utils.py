# Third-Party libraries
from requests import get
from requests.exceptions import RequestException

# Constants
from constants import GITHUB_API_URL, DEFAULT_MESSAGE, GITHUB_VERSION_TAG_KEY

# Logging
from app_logging import LoggingManager

# App enums
from app_enums import LOG_LEVELS, UserPreferencesKeys

# Utils
from .time_utils import has_one_month_passed

logging_manager = LoggingManager()


def _get_latest_github_release_version():
    """
    Fetches the latest release version from a GitHub repository.

    Returns:
        str: Latest release tag or an error message.
    """

    try:
        response = get(GITHUB_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        latest_version: str = data.get(GITHUB_VERSION_TAG_KEY, DEFAULT_MESSAGE)

        return latest_version.replace("v", "")

    except RequestException as e:
        logging_manager.write_log(
            LOG_LEVELS.ERROR, f"Error fetching latest release: {e}"
        )

        return f"Error fetching latest release: {e}"


def get_github_version() -> str:
    if "UserPreferencesManager" not in globals():
        from user_preferences.user_preferences_manager import (
            UserPreferencesManager,
        )

    user_preferences_manager = UserPreferencesManager()

    if has_one_month_passed():
        latest_github_release_version = _get_latest_github_release_version()

        user_preferences_manager.set_preference(
            UserPreferencesKeys.LATEST_GITHUB_VERSION,
            latest_github_release_version,
        )

        return latest_github_release_version

    return user_preferences_manager.get_preference(
        UserPreferencesKeys.LATEST_GITHUB_VERSION
    )
