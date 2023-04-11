from os import remove

from client.logging_management import LoggingManagement

log = LoggingManagement


def delete_file(path_to_video, download_name, reset):
    """
    Cancel the download of the video and/or audio and then delete it
    """

    try:
        remove(f"{path_to_video}/{download_name}")

    finally:
        reset()
