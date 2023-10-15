# Standard library
from typing import Callable, get_type_hints, Type

# Constants
from constants import ENABLED_TYPE_CHECKING


def check_type(func: Callable) -> Callable:
    def validate_type(*args, **kwargs):
        if not ENABLED_TYPE_CHECKING:
            return func(*args, **kwargs)

        hints = get_type_hints(func)

        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in hints:
                expected_type = hints[arg_name]
                if isinstance(expected_type, Type):
                    # Handling non-union types
                    if not isinstance(arg_value, expected_type):
                        raise TypeError(
                            f"{arg_name} should be of type {expected_type.__name__}"
                        )
                else:
                    # Handling union types
                    expected_types = expected_type.__args__
                    if not any(isinstance(arg_value, t) for t in expected_types):
                        expected_type_names = [t.__name__ for t in expected_types]
                        raise TypeError(
                            f"{arg_name} should be one of these types: {', '.join(expected_type_names)}"
                        )

        return func(*args, **kwargs)

    return validate_type
