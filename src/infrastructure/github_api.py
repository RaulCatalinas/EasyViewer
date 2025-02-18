# Third-Party libraries
from requests import get
from requests.exceptions import RequestException

# Constants
from constants import GITHUB_API_URL, DEFAULT_MESSAGE, GITHUB_VERSION_TAG_KEY

# Logging
from app_logging import LoggingManager

# App enums
from app_enums import LOG_LEVELS


logging_manager = LoggingManager()


def get_latest_github_release():
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
        logging_manager.write_log(LOG_LEVELS.ERROR, str(e))

        return f"Error fetching release: {e}"
