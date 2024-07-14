# Video location
from .video_location import VideoLocation

# Checkbox
from .checkbox import CheckBox

# Local storage
from local_storage import LocalStorage

# Whats new read
from .whats_new_read import WhatsNewRead

# Disclaimer dialog
from .disclaimer_dialog import DisclaimerDialogControlVariable

video_location_instance = VideoLocation()
checkbox_instance = CheckBox()
whats_new_read_instance = WhatsNewRead()
disclaimer_dialog_instance = DisclaimerDialogControlVariable()


def store_control_variables(page):
    """
    Saves the video location to the user's local storage.

    Args:
        page (flet.Page): Reference to the app window.
    """

    local_storage = LocalStorage(page)

    video_location = video_location_instance.get()
    checkbox_update = checkbox_instance.get("update")
    whats_new_read = whats_new_read_instance.get()
    disclaimer_dialog = disclaimer_dialog_instance.get()

    save_to_local_storage = [
        ("video_location", video_location),
        ("checkbox_update", checkbox_update),
        ("whats_new_read", whats_new_read),
        ("disclaimer_dialog", disclaimer_dialog),
    ]

    for key, value in save_to_local_storage:
        local_storage.set(key, value)
