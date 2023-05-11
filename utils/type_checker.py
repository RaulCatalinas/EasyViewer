"""
Check the types that receive parameters
"""

from typing import get_type_hints, Callable

from utils import ENABLED_TYPE_CHECKING


def check_type(func: Callable):
    """
    Takes a function and returns a wrapper function that validates the types of the arguments passed to the original function.

    :param func: A callable object (function, method, etc.) that we want to validate the input types for parameters

    :return: Returns a new function `validate_type` that wraps the original function passed as an argument. The new function performs type checking on the arguments passed to the original function using the type hints specified in the function signature. If any argument does not match its expected type, a `TypeError` is raised. If all arguments pass the type check, the original function is called with the
    """

    def validate_type(*args, **kwargs):
        if not ENABLED_TYPE_CHECKING:
            return func(*args, **kwargs)

        hints = get_type_hints(func)

        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in hints:
                expected_type = hints[arg_name]

                if not isinstance(arg_value, expected_type):
                    raise TypeError(
                        f"{arg_name} should be of type {expected_type.__name__}"
                    )

        return func(*args, **kwargs)

    return validate_type
