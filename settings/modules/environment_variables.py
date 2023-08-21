"""
Controls the logic of environment variables
"""

# Standard library
from os import environ
from threading import Lock, Thread

# Third-Party libraries
from dotenv import set_key
from flet import Page

# Osutils
from osutils import GetPaths

# Utils
from utils import check_type


class EnvironmentVariables:
    """
    Controls the logic of environment variables
    """

    ENVIRONMENT_VARIABLES_FILE = GetPaths.get_config_file("env")
    LOCK = Lock()

    @classmethod
    @check_type
    def set_language(cls, language: str, page: Page):
        """
        Sets the value of the "LANGUAGE" environment variable

        Args:
            language (str): Language to be set
            page (flet.Page): Reference to the application window.
        """

        environ["LANGUAGE"] = language

        cls.save(page=page, language_to_save=language)

    @classmethod
    def get_language(cls):
        """
        Gets the language saved in the environment variable

        Returns:
            str: The language saved in the environment variable
        """

        return environ.get("LANGUAGE")

    @classmethod
    @check_type
    def save(cls, page: Page, language_to_save: str):
        """
        Saves the language selected by the user to the client storage.

        Args:
            page (flet.Page): Reference to the application window.
            language_to_save (str): Language to save in client storage.
        """

        def set_key_thread():
            set_key(
                cls.ENVIRONMENT_VARIABLES_FILE,
                key_to_set="LANGUAGE",
                value_to_set=language_to_save,
            )

        with cls.LOCK:
            Thread(
                target=page.client_storage.set,
                args=["language", language_to_save],
                daemon=False,
            ).start()

            Thread(target=set_key_thread, daemon=False).start()

    @classmethod
    @check_type
    def set_initial_language(cls, page: Page):
        """
        Set the environment variable "LANGUAGE"

        Args:
            page (flet.Page): Reference to the application window.
        """
        language_for_the_app = page.client_storage.get("language") or "English"

        environ["LANGUAGE"] = language_for_the_app
