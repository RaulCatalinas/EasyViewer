"""
Controls the logic of environment variables
"""

from os import environ
from threading import Thread, Lock

from dotenv import set_key
from flet import Page

from utils import CONFIG_FILES, check_type


class EnvironmentVariables:
    """
    Controls the logic of environment variables
    """

    ENVIRONMENT_VARIABLES_FILE = CONFIG_FILES["ENV"]
    LOCK = Lock()

    @classmethod
    @check_type
    def set_language(cls, language: str, page: Page) -> None:
        """
        Sets the value of the "LANGUAGE" environment variable

        :param page: Is a reference to the app window
        :param language: The language to set
        """

        environ["LANGUAGE"] = language

        cls.save(page=page, language_to_save=language)

    @classmethod
    def get_language(cls) -> str:
        """
        Gets the language saved in the environment variable

        :return: The value of the environment variable "LANGUAGE"
        """

        return environ.get("LANGUAGE")

    @classmethod
    @check_type
    def save(cls, page: Page, language_to_save: str) -> None:
        """
        Saves the language of the app in a frontend storage using a separate thread.

        :param page: Is a reference to the app window
        :param language_to_save: Language of the app being saved. It's used as a key to store it in the user's storage.
        """

        def set_key_thread():
            set_key(
                cls.ENVIRONMENT_VARIABLES_FILE,
                key_to_set="LANGUAGE",
                value_to_set=language_to_save,
            )

        with cls.LOCK:
            Thread(
                target=page.client_storage.set_control_variable_in_ini,
                args=["language", language_to_save],
                daemon=False,
            ).start()

            Thread(target=set_key_thread, daemon=False).start()

    @classmethod
    @check_type
    def set_initial_language(cls, page: Page):
        """
        Sets the "LANGUAGE" environment variable to the value saved in frontend storage. Defaults to "English" if nothing is saved.

        :param page: Is a reference to the app window
        """

        language_for_the_app = page.client_storage.get("language") or "English"

        environ["LANGUAGE"] = language_for_the_app
