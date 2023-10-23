# Standard library
from re import sub

# Strings utils
from .strings_utils import remove_empty_strings

# Check type
from .type_checker import check_type


@check_type
def separate_urls(urls: str):
    urls_with_spaces = sub(r"(https://)", r" \1", urls).replace(" ", "\n")

    return remove_empty_strings(urls_with_spaces.splitlines())
