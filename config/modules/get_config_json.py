"""
Gets the app texts from the JSON file
"""

from json import load

from osutils import GetPaths
from utils import check_type


class GetConfigJson:
    """
    Gets the app texts from the JSON file
    """

    @classmethod
    @check_type
    def get_config_json(cls, section: str, data: str) -> str | int:
        """
        Reads a JSON file and returns a value from a specified section and
        data key.

        :param section: A string representing the section of the JSON configuration file to retrieve data from
        :param data: The key for the value that needs to be retrieved from the JSON configuration file

        :return: Returns a value of type `str` or `int`, depending on the value stored in the JSON file for the given `section` and `data`.
        """

        config_json = cls._read_json()

        return config_json[section][data]

    @staticmethod
    def _read_json() -> dict:
        """
        Reads a JSON file and returns its contents as a dictionary.

        :return: Returns the contents of a JSON file as a dictionary.
        """

        json_file_path = GetPaths.get_config_file("json")

        with open(json_file_path, encoding="utf-8") as f:
            return load(f)
