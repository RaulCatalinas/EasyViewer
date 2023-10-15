# Video location
from .video_location import VideoLocation

# Checkbox
from .checkbox import CheckBox

# Local storage
from local_storage import LocalStorage

video_location_instance = VideoLocation()
checkbox_instance = CheckBox()


def store_control_variables(page):
    """
    Saves the video location to the user's local storage.

    Args:
        page (flet.Page): Reference to the app windowcls._
    """

    local_storage = LocalStorage(page)

    video_location = video_location_instance.get()
    checkbox_update = checkbox_instance.get("update")

    local_storage.set("video_location", video_location)
    local_storage.set("checkbox_update", checkbox_update)
