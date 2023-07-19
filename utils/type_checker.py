from typing import Callable, get_type_hints

from utils import ENABLED_TYPE_CHECKING


def check_type(func: Callable) -> Callable:
    """
    Validates the types of the arguments.

    Args:
        func (Callable): (function, method, etc.) of which we wanna validate the types

    Raises:
        TypeError: Exception thrown if parameter types don't match expected types

    Returns:
        Callable: Original function call
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
