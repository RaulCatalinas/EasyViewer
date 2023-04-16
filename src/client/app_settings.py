"""Set the app settings"""

from configparser import ConfigParser
from json import load
from os import environ
from threading import Lock
from threading import Thread

from dotenv import load_dotenv, set_key
from pandas import read_excel

from config.get_files import get_files_path

(
    _languages_file_path,
    _environment_variables_path,
    _control_variables_json_path,
    _config_json_path,
    _token_github,
) = get_files_path()

LANGUAGES = read_excel(_languages_file_path)

load_dotenv(_environment_variables_path)


class AppSettings:
    """Read a JSON file and an Excel file, and return the value of a key to be able to configure the app"""

    def __init__(self):
        self.lock = Lock()

        self.config = ConfigParser()
        self.config.read(_token_github, encoding="utf-8")

        with open(_config_json_path, encoding="utf-8") as f:
            self.config_json = load(f)

    def get_config_json(self, section: str, data: str) -> str | int:
        """
        Returns the value of a key in a dictionary, which is inside another dictionary

        :param section: is the section of the json file
        :param data: is the name of the parameter you want to get from the json file
        :return: The value of the "data" key in the "section" section of the json file.
        """

        return self.config_json[section][data]

    def get_config_excel(self, excel_column_number: int) -> str:
        """
        Returns the value of the cell in the column of the excel file that corresponds to the language that the
        user has selected

        :param excel_column_number: The number of the column in the Excel file
        :return: The value of the cell in the column of the language being used.
        """

        LANGUAGE = self.get_language()
        return LANGUAGES.loc[excel_column_number][LANGUAGE]

    def set_language(self, language: str, page) -> None:
        """
        Sets the value of the LANGUAGE variable in the system environment variables

        :param language: The language to set
        """

        environ["LANGUAGE"] = language

        self.save(page=page, language=language)

        set_key(
            _environment_variables_path, key_to_set="LANGUAGE", value_to_set=language
        )

    @staticmethod
    def get_language() -> str:
        """Gets the language of the app saved in the environment variable"""

        LANGUAGE = environ.get("LANGUAGE")
        return LANGUAGE

    @staticmethod
    def get_file_control_variables() -> str:
        """
        Returns the json path of the control variables.
        :return: The son path of the control variables.
        """

        return _control_variables_json_path

    def save(self, page, language):
        with self.lock:
            Thread(
                target=page.client_storage.set,
                args=["language", language],
                daemon=False,
            ).start()

    def set_environment_variable(self, page):
        LANGUAGE = page.client_storage.get("language") or "English"

        environ["LANGUAGE"] = LANGUAGE

        set_key(
            _environment_variables_path,
            key_to_set="LANGUAGE",
            value_to_set=LANGUAGE,
        )

    def get_token(self):
        return self.config["Token"]["token"]
