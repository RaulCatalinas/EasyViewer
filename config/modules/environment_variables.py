from os import environ
from threading import Thread, Lock

from dotenv import load_dotenv, set_key
from flet import Page

from utils import check_type, ConfigFiles


class EnvironmentVariables:
    """
    Controls the logic of environment variables
    """

    ENVIRONMENT_VARIABLES_FILE = ConfigFiles.ENV.value
    LOCK = Lock()

    def __init__(self):
        load_dotenv(EnvironmentVariables.ENVIRONMENT_VARIABLES_FILE)

    @classmethod
    def set_language(cls, language: str, page: Page) -> None:
        """
        Sets the value of the "LANGUAGE" environment variable

        :param page: Is a reference to the app window

        :param language: The language to set
        """

        check_type(page, Page)
        check_type(language, str)

        environ["LANGUAGE"] = language

        cls.save(page=page, language_to_save=language)

        set_key(
            cls.ENVIRONMENT_VARIABLES_FILE, key_to_set="LANGUAGE", value_to_set=language
        )

    @classmethod
    def get_language(cls) -> str:
        """
        Gets the language saved in the environment variable

        :return: The value of the environment variable "LANGUAGE"
        """

        return environ.get("LANGUAGE")

    @classmethod
    def save(cls, page: Page, language_to_save: str) -> None:
        """
        Saves the language of the app in a frontend storage using a separate thread.

        :param page: Is a reference to the app window

        :param language_to_save: Language of the app being saved. It's used as a key to store it in the frontend's storage.
        """

        check_type(page, Page)
        check_type(language_to_save, str)

        with cls.LOCK:
            Thread(
                target=page.client_storage.set,
                args=["language", language_to_save],
                daemon=False,
            ).start()

    @classmethod
    def set_initial_language(cls, page: Page):
        """
        Sets the "LANGUAGE" environment variable to the value saved in frontend storage. Defaults to "English" if nothing is saved.

        :param page: Is a reference to the app window
        """

        check_type(page, Page)

        language_for_the_app = page.client_storage.get("language") or "English"

        environ["LANGUAGE"] = language_for_the_app

        set_key(
            cls.ENVIRONMENT_VARIABLES_FILE,
            key_to_set="LANGUAGE",
            value_to_set=language_for_the_app,
        )
