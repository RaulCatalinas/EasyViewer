# Standard library
from re import sub

# Strings utils
from .strings_utils import remove_empty_strings


def separate_urls(urls: str):
    """
    Separate URLs in a string and return them as a list.

    Takes a string containing URLs and separates them into a list.

    It first adds a space before each "https://" to ensure proper separation and then splits the string into individual URLs using line breaks.

    It also removes any empty strings that might result from the splitting.

    Args:
        urls (str): A string containing URLs.

    Returns:
        list[str]: A list of separated URLs.

    Example:
        >>> urls = "https://example.com https://another-url.comhttps://another-url.com"
        >>> separate_urls(urls)
        ['https://example.com', 'https://another-url.com', 'https://another-url.com']
    """

    urls_with_spaces = sub(r"(https://)", r" \1", urls).replace(" ", "\n")

    return remove_empty_strings(urls_with_spaces.splitlines())
