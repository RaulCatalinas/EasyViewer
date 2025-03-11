# Standard library
from typing import ClassVar, Dict
from pathlib import Path
from os.path import dirname, abspath

# Third-Party libraries
from pandas import read_excel, DataFrame

# User preferences
from user_preferences import UserPreferencesManager

# App enums
from app_enums import UserPreferencesKeys, ExcelTextLoaderKeys


class ExcelTextLoader:
    """
    Gets the app texts from the Excel file
    """

    _instance = None
    _script_dir = Path(dirname(abspath(__file__)))
    LANGUAGES_FILE: ClassVar[Path] = _script_dir.joinpath("languages.xlsx")
    user_preferences_manager: ClassVar[UserPreferencesManager] = (
        UserPreferencesManager()
    )
    _text_dictionary: Dict[str, Dict[str, str]] = {}
    _is_loaded: bool = False
    _current_language: str = ""

    def __new__(cls):
        """Ensures only one instance of ExcelTextLoader exists."""

        if cls._instance is None:
            cls._instance = super(ExcelTextLoader, cls).__new__(cls)
            cls._load_texts()

        return cls._instance

    @classmethod
    def _load_texts(cls) -> None:
        """
        Loads all texts from the Excel file into memory.
        """
        if not cls._is_loaded:
            languages_dataframe = cls._read_excel()

            # Assume first column contains keys
            keys_column = languages_dataframe.iloc[:, 0]

            # For each row in the dataframe
            for i, key in enumerate(keys_column):
                cls._text_dictionary[key] = {}

                # For each language column (skipping the first key column)
                for lang in languages_dataframe.columns[1:]:
                    cls._text_dictionary[key][lang] = languages_dataframe.iloc[
                        i
                    ][lang]

            cls._is_loaded = True

    @classmethod
    def reload_texts(cls) -> None:
        """
        Forces a reload of all texts from the Excel file.
        Useful when the Excel file has been updated.
        """

        cls._is_loaded = False
        cls._text_dictionary = {}
        cls._load_texts()

    @classmethod
    def get_text(cls, text_key: ExcelTextLoaderKeys) -> str:
        """
        Returns the text saved in the dictionary based on the language of the application

        Args:
            text_key (ExcelTextLoaderKeys): Key identifier for the text

        Returns:
            str: The text in the current language
        """

        language: str = cls.user_preferences_manager.get_preference(
            UserPreferencesKeys.LANGUAGE
        )

        # Check if key exists
        if text_key not in cls._text_dictionary:
            return f"Missing text: {text_key}"

        # Check if language exists for this key
        if language not in cls._text_dictionary[text_key]:
            # Fallback to first available language
            fallback_lang = next(iter(cls._text_dictionary[text_key]))

            return cls._text_dictionary[text_key][fallback_lang]

        return cls._text_dictionary[text_key][language]

    @classmethod
    def _read_excel(cls) -> DataFrame:
        """
        Reads an Excel file and returns the data as a DataFrame.

        Returns:
            DataFrame: The data read from the Excel as a DataFrame.
        """

        print("📚 Excel file loaded successfully.")

        return read_excel(cls.LANGUAGES_FILE)
