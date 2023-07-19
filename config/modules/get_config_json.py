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

    @staticmethod
    @check_type
    def get_config_json(section: str, data: str) -> str | int:
        """
        Gets the configuration saved in the JSON

        Args:
            section (str): Section from which you wanna obtain the data
            data (str): Data that you wanna obtain

        Returns:
            str | int: The data obtained
        """

        config_json = GetConfigJson._read_json()

        return config_json[section][data]

    @staticmethod
    def _read_json() -> dict:
        """
        Load the JSON data into a dictionary

        Returns:
            dict: The content of the JSON in the form of a dictionary
        """

        json_file_path = GetPaths.get_config_file("json")

        with open(json_file_path, encoding="utf-8") as f:
            return load(f)
