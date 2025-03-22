# Standard library
from json import dump, load
from os.path import exists, abspath, dirname
from atexit import register
from typing import Any, Dict

# App enums
from app_enums import UserPreferencesKeys

# Utils
from utils import create_empty_json_file

# Constants
from constants import DEFAULT_USER_PREFERENCES, USER_PREFERENCES_FILE


class UserPreferencesManager:
    """
    Singleton class that manages user preferences in memory during the app session.
    Preferences are only saved to disk when the app is closed.
    """

    _instance = None
    _script_dir = dirname(abspath(__file__))
    USER_PREFERENCES_FILE_PATH = f"{_script_dir}/{USER_PREFERENCES_FILE}.json"

    def __new__(cls):
        """Ensures only one instance of UserPreferencesManager exists."""
        if cls._instance is None:
            cls._instance = super(UserPreferencesManager, cls).__new__(cls)
            cls._instance._initialize()

        return cls._instance

    def _initialize(self) -> None:
        """Initializes the preferences manager, loading data from file or setting defaults."""

        self.preferences = self._load_preferences()

        # Ensure preferences are saved when the app closes
        register(self._save_preferences)

    def _load_preferences(self) -> Dict[UserPreferencesKeys, Any]:
        """
        Loads user preferences from the JSON file or creates a new one if it doesn't exist.

        Returns:
            dict: A dictionary containing the user preferences.
        """

        if not exists(self.USER_PREFERENCES_FILE_PATH):
            print("🔄 Creating new user preferences file...")

            self._create_default_preferences()

        with open(self.USER_PREFERENCES_FILE_PATH, "r", encoding="utf-8") as f:
            return load(f)

    def _create_default_preferences(self) -> None:
        """Creates the default preferences file if it doesn't exist."""

        create_empty_json_file(
            self._script_dir, f"{self._script_dir}/{USER_PREFERENCES_FILE}"
        )

        with open(self.USER_PREFERENCES_FILE_PATH, "w", encoding="utf-8") as f:
            dump(DEFAULT_USER_PREFERENCES, f, indent=2)

    def get_preference(self, key: UserPreferencesKeys) -> Any:
        """
        Retrieves a specific user preference.

        Args:
            key (UserPreferencesKeys): The preference key.

        Returns:
            Any: The value of the preference or None if not found.
        """

        return self.preferences.get(key)

    def set_preference(self, key: UserPreferencesKeys, value: Any):
        """
        Updates a user preference in memory.

        Args:
            key (UserPreferencesKeys): The preference key.
            value (Any): The new value for the preference.
        """

        self.preferences[key] = value

    def _save_preferences(self) -> None:
        """Saves the current user preferences to user_preferences.json."""

        with open(self.USER_PREFERENCES_FILE_PATH, "w", encoding="utf-8") as f:
            dump(self.preferences, f, indent=4)

        print("💾 User preferences saved successfully!")
