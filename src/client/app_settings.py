"""Set the app settings"""

from json import load
from os import environ
from pathlib import Path

from dotenv import load_dotenv, set_key
from pandas import read_excel

_project_path = Path(__file__).parent.parent.parent

_config_path = Path(_project_path, "config")
_config_json_path = Path(_config_path, "config.json")
_languages_file_path = Path(_config_path, "languages.xlsx")
_environment_variables_path = Path(_config_path, ".env")
_control_variables_json_path = Path(_config_path, "control_variables.json")

_icon_path = Path(_project_path, "icon", "icon.png")

print(
    f"""
    {_project_path = }
    
    {_config_path = }
    {_config_json_path = }
    {_languages_file_path = }
    {_environment_variables_path = }
    {_control_variables_json_path = }
    
    {_icon_path = }
    """
)

languages = read_excel(_languages_file_path)
print(languages)
print()

load_dotenv(_environment_variables_path)


class AppSettings:
    """Read a JSON file and an Excel file, and return the value of a key to be able to configure the app"""

    def __init__(self):
        with open(_config_json_path, encoding="utf-8") as json:
            self.config_json = load(json)

        print(self.config_json)

    def get_config_json(self, section, data):
        """
        Returns the value of a key in a dictionary, which is inside another dictionary

        :param section: is the section of the json file
        :param data: is the name of the parameter you want to get from the json file
        :return: The value of the "data" key in the "section" section of the json file.
        """
        return self.config_json[section][data]

    def get_config_excel(self, excel_column_number):
        """
        Returns the value of the cell in the column of the excel file that corresponds to the language that the
        user has selected

        :param excel_column_number: The number of the column in the Excel file
        :return: The value of the cell in the column of the language being used.
        """
        print(languages.loc[excel_column_number][self.get_language()])

        return languages.loc[excel_column_number][self.get_language()]

    @staticmethod
    def set_language(language):
        """
        Sets the value of the LANGUAGE variable in the system environment variables

        :param language: The language to set
        """
        # Store selected language temporarily
        environ["LANGUAGE"] = language

        # Save the selected language in the environment variable
        set_key(
            _environment_variables_path, key_to_set="LANGUAGE", value_to_set=language
        )

    @staticmethod
    def get_language():
        print()
        print(f'App language: {environ.get("LANGUAGE")}')
        print()
        return environ.get("LANGUAGE")

    @staticmethod
    def get_icon():
        """
        Returns the path of the icon.
        :return: The path of the icon.
        """
        return _icon_path

    @staticmethod
    def get_file_control_variables():
        """
        Returns the json path of the control variables.
        :return: The son path of the control variables.
        """

        return _control_variables_json_path
