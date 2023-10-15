# Standard library
from typing import Any

# Third-Party libraries
from flet_core.client_storage import ClientStorage


class LocalStorage(ClientStorage):
    def __init__(self, page):
        super().__init__(page)

    def set(self, key: str, value: Any):
        if value is None:
            return

        super().set(key, value)

    def get(self, key: str):
        return super().get(key)
