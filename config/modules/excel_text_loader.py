"""
Gets the app texts from the Excel file
"""

from pandas import read_excel

from osutils import GetPaths
from utils import check_type
from .environment_variables import EnvironmentVariables


class ExcelTextLoader:
    """
    Gets the app texts from the Excel file
    """

    @classmethod
    @check_type
    def get_text(cls, excel_column_number: int) -> str:
        """
        Returns a string value from a specific column based on the language specified in the environment variables.

        :param excel_column_number: An integer representing the column number in the Excel file from which to retrieve the configuration value

        :type excel_column_number: int

        :return: Returns a string value that is located in the specified
        column number of the `__languages_dataframe` dataframe for the language specified in the`language` class variable.
        """

        cls.language = EnvironmentVariables.get_language()

        cls.__languages_dataframe = cls._read_excel()

        return cls.__languages_dataframe.loc[excel_column_number][cls.language]

    @classmethod
    def _read_excel(cls):
        """
        Reads an Excel file

        :return: Returns the data read from an Excel file
        """

        excel_file_path = GetPaths.get_config_file("excel")

        return read_excel(excel_file_path)
