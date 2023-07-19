from .type_checker import check_type
from enum import Enum


class EnumHelper:
    @staticmethod
    @check_type
    def get_enum_value(enum_instance: Enum) -> str:
        """
        Gets the value of an Enum..

        Args:
            enum_instance (Enum): Enum from which you want to get its value.

        Returns:
            str: The value of the enum.
        """

        return enum_instance.value
