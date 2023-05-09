"""
Gets the app texts from the JSON file
"""

from json import load

from utils import CONFIG_FILES, check_type


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

        :type section: str

        :param data: The `data` parameter is a string that represents the key for the value that needs to be retrieved from the JSON configuration file

        :type data: str

        :return: Returns a value of type `str` or `int`, depending on the value stored in the JSON file for the given `section` and `data`.
        """

        cls.config_json = cls._read_json()

        return cls.config_json[section][data]

    @classmethod
    def _read_json(cls):
        """
        Reads a JSON file and returns its contents as a dictionary.

        :return: Returns the contents of a JSON file as a dictionary.
        """

        with open(
            CONFIG_FILES["JSON"],
            encoding="utf-8",
            mode="r",
        ) as f:
            return load(f)
