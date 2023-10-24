# Standard library
from re import sub

# Strings utils
from .strings_utils import remove_empty_strings

# Constants
from constants import HTTPS_PATTERN, SPACE_BEFORE_HTTPS

# Third-Party libraries
from pytube import YouTube

# Osutils
from osutils import FileHandler

# Utils
from utils import check_type

# Constants
from constants import (
    EXTENSION_FILE_VIDEO,
    EXTENSION_FILE_AUDIO,
)


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

    urls_with_spaces = sub(HTTPS_PATTERN, SPACE_BEFORE_HTTPS, urls).replace(" ", "\n")

    return remove_empty_strings(urls_with_spaces.splitlines())


@check_type
def get_video_title(url: str, download_video: bool):
    """
    Returns the title of a YouTube video, with characters not allowed in OS file names removed, and with the corresponding file extension

    Args:
        url (str): URL of the video whose title you want.
        download_video (bool): Whether to use the extension '.mp4' or '.mp3'.

    Returns:
        str: The title of the video without characters not allowed in OS filenames and with the corresponding file extension.

    Example:
    >>> title = get_video_title("https://www.youtube.com/watch?v=abc123", True)
    >>> print(title)
    "My_Video_Title.mp4"

    >>> title = get_video_title("https://www.youtube.com/watch?v=xyz456", False)
    >>> print(title)
    "My_Audio_Title.mp3"
    """

    youtube = YouTube(url)
    video_title = youtube.title

    title_for_the_file = FileHandler.clean_invalid_chars(video_title)

    extension_file = EXTENSION_FILE_VIDEO if download_video else EXTENSION_FILE_AUDIO

    return f"{title_for_the_file}.{extension_file}"
