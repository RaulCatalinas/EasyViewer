"""
Gets the app texts from the Excel file
"""

# Third-Party libraries
from pandas import read_excel

# Osutils
from osutils import GetPaths

# Utils
from utils import check_type

# Envrioment variables
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
    def _read_excel():
        """
        Reads an Excel file and returns the data as a DataFrame.

        Returns:
            DataFrame: The data read from the Excel as a DataFrame.
        """

        excel_file_path = GetPaths.get_config_file("excel")
        return read_excel(excel_file_path)
