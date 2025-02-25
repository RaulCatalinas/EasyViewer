def remove_empty_strings(input_list: list[str]) -> list[str]:
    """
    Remove empty strings from a list.

    This function takes a list of strings and removes any empty strings present in the list.

    Args:
        input_list (list[str]): A list of strings that may contain empty strings.

    Returns:
        list[str]: A new list with empty strings removed.

    Example:
        >>> string_list = ["apple", "", "banana", "", "cherry"]
        >>> remove_empty_strings(string_list)
        ['apple', 'banana', 'cherry']
    """

    return list(filter(lambda item: item != "", input_list))
