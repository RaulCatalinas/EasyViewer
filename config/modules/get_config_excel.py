from pandas import read_excel

from utils import ConfigFiles
from .environment_variables import EnvironmentVariables


class GetConfigExcel:
    @classmethod
    def get_config_excel(cls, excel_column_number: int) -> str:
        cls.language = EnvironmentVariables.get_language()

        cls.__languages_dataframe = cls._read_excel()

        return cls.__languages_dataframe.loc[excel_column_number][cls.language]

    @classmethod
    def _read_excel(cls):
        excel_file_path = ConfigFiles.EXCEL.value
        return read_excel(excel_file_path)
