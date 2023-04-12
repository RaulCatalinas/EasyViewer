from os import remove


def delete_file(path_to_video, download_name, reset):
    """
    Cancel the download of the video and/or audio and then delete it
    """

    try:
        remove(f"{path_to_video}/{download_name}")

    finally:
        reset()
