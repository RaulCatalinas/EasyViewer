# Download name
from .download_name import DownloadName

# Urls
from .urls import URLs

download_name = DownloadName()
urls = URLs()


def reset():
    """
    Resets the value of the control variables
    """

    download_name.set("")
    urls.set("")
