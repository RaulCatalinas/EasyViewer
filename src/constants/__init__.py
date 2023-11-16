# Cache
from .cache import CACHE_FILE, DAYS_FOR_THE_CACHE_TO_EXPIRE

# Chars
from .chars import INVALID_CHARS, SYSTEM_NAME

# Download settings
from .download_settings import (
    EXTENSION_FILE_AUDIO,
    EXTENSION_FILE_VIDEO,
)

# GitHub API
from .github_api import GITHUB_REPO, GITHUB_USER, LATEST_RELEASE_URL

# Hosts
from .hosts import ALLOW_HOSTS, GOOGLE

# Paths
from .paths import CONFIG_FILES, DESKTOP_PATH, ROOT_PATH, USER_HOME

# Regex
from .regex import HTTPS_PATTERN, SPACE_BEFORE_HTTPS

# Social networks
from .social_networks import SOCIAL_NETWORKS

# Type checking
from .type_checking import ENABLED_TYPE_CHECKING

# Versions
from .versions import USER_VERSION

# Whats new
from .whats_new import WHATS_NEW_MESSAGE_ES, WHATS_NEW_MESSAGE_EN

__all__ = [
    "CACHE_FILE",
    "DAYS_FOR_THE_CACHE_TO_EXPIRE",
    "INVALID_CHARS",
    "SYSTEM_NAME",
    "EXTENSION_FILE_AUDIO",
    "EXTENSION_FILE_VIDEO",
    "GITHUB_REPO",
    "GITHUB_USER",
    "LATEST_RELEASE_URL",
    "ALLOW_HOSTS",
    "GOOGLE",
    "CONFIG_FILES",
    "DESKTOP_PATH",
    "ROOT_PATH",
    "USER_HOME",
    "HTTPS_PATTERN",
    "SPACE_BEFORE_HTTPS",
    "SOCIAL_NETWORKS",
    "ENABLED_TYPE_CHECKING",
    "USER_VERSION",
    "WHATS_NEW_MESSAGE_ES",
    "WHATS_NEW_MESSAGE_EN",
]
