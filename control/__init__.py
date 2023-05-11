"""
Read and write control variables in the INI file
"""

from .read_control_variables import get_control_variable
from .write_control_variables import WriteControlVariables

__all__ = ["get_control_variable", "WriteControlVariables"]
