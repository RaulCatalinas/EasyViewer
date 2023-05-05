def check_type(variable, expected_type):
    if not isinstance(variable, expected_type):
        raise TypeError(f"The variable {variable} must be of type {expected_type}")
