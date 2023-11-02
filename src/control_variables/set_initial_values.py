# Video location
from .video_location import VideoLocation

# Checkbox
from .checkbox import CheckBox

# Local storage
from local_storage import LocalStorage

# Whats new read
from .whats_new_read import WhatsNewRead

video_location_instance = VideoLocation()
checkbox_instance = CheckBox()
whats_new_read_instance = WhatsNewRead()


def set_initial_values(page):
    """
    Sets initial values for control variables

    Args:
        page (flet.Page): Reference to the app window
    """

    local_storage = LocalStorage(page)

    video_location = local_storage.get("video_location")
    checkbox = local_storage.get("checkbox_update")
    whats_new_read = local_storage.get("whats_new_read")

    video_location_instance.set(video_location)
    checkbox_instance.set("update", checkbox)
    whats_new_read_instance.set(whats_new_read)
