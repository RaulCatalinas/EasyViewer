from json import load

from utils import ConfigFiles


class GetConfigJson:
    def __init__(self):
        pass

    @classmethod
    def get_config_json(cls, section: str, data: str) -> str | int:
        """
        Returns the value of a key in a dictionary, which is inside another dictionary

        :param section: is the section of the json file

        :param data: is the name of the parameter you want to get from the json file

        :return: The value of the "data" key in the "section" section of the json file.
        """

        cls.config_json = cls._read_json()

        return cls.config_json[section][data]

    @classmethod
    def _read_json(cls):
        with open(
            ConfigFiles.JSON.value,
            encoding="utf-8",
            mode="r",
        ) as f:
            return load(f)
