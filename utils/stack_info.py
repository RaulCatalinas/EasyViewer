"""
Gets information about the file name, error line, and parameter name from the stack trace.
"""

from inspect import stack


def get_stack_info():
    """
    Retrieves information about the file name, error line, and parameter name from the stack trace.

    :return: Returns a tuple containing the name of the file where the error occurred, the line number where the error occurred, and the name of the parameter that caused the error.
    """

    frames = stack()

    file_name = frames[3].filename
    error_line = frames[3].lineno
    param_name = frames[2].code_context[0].split("(")[1].split(",")[0].strip()

    return file_name, error_line, param_name
