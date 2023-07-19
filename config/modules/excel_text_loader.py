"""
Gets the app texts from the Excel file
"""

from pandas import DataFrame, read_excel

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
        Returns the text saved in the Excel based on the language of the application

        Args:
            excel_column_number (int): Column of which we wanna obtain the text

        Returns:
            str: The text saved in the Excel
        """

        language = EnvironmentVariables.get_language()
        languages_dataframe = cls._read_excel()

        return languages_dataframe.loc[excel_column_number][language]

    @staticmethod
    def _read_excel() -> DataFrame:
        """
        Reads an Excel file and returns the data as a DataFrame.

        Returns:
            DataFrame: The data read from the Excel as a DataFrame.
        """

        excel_file_path = GetPaths.get_config_file("excel")
        return read_excel(excel_file_path)
