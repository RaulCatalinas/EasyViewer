"""
Control the application cache
"""

from datetime import datetime, timedelta
from json import JSONDecodeError, dump, load
from time import time
from typing import Any

from utils import CACHE_FILE, LoggingManagement


class CacheManager:
    """
    Control the application cache
    """

    @staticmethod
    def read_cache():
        """
        Get the data from the cache

        Raises:
            JSONDecodeError: Error occurred during data collection

        Returns:
            Any: The cache data
        """

        with open(CACHE_FILE, mode="r", encoding="utf-8") as file:
            try:
                return load(file)

            except JSONDecodeError as exc:
                LoggingManagement.write_error(str(exc))

                raise JSONDecodeError(str(exc), doc=CACHE_FILE, pos=0) from exc

    @staticmethod
    def write_cache(key: str, data: Any):
        """
        Writes data to the cache, along with a timestamp.

        Args:
            key (str): Key with which the data will be saved
            data (Any): Data to save
        """

        try:
            array = CacheManager.read_cache()
            cached_data = {key: data, "timestamp": int(time())}

            array.append(cached_data)

            with open(CACHE_FILE, mode="w", encoding="utf-8") as file:
                dump(array, file)

        except Exception as e:
            LoggingManagement.write_error(str(e))

    @staticmethod
    def create_json_cache():
        """
        Creates an empty JSON cache file.
        """

        try:
            with open(CACHE_FILE, mode="w", encoding="utf-8") as file:
                file.write("[]")

        except Exception as e:
            LoggingManagement.write_error(str(e))

    @staticmethod
    def reset_cache_if_expired():
        """
        Check if cached data has expired and reset it if necessary
        """

        with open(CACHE_FILE, mode="r", encoding="utf-8") as file:
            try:
                cache_data = load(file)

                if len(cache_data) == 0:
                    return

                current_time = datetime.now()

                for data in cache_data:
                    timestamp = data.get("timestamp")
                    cache_time = datetime.fromtimestamp(timestamp)
                    expiration_time = cache_time + timedelta(days=30)

                    if current_time > expiration_time:
                        CacheManager.create_json_cache()

            except (JSONDecodeError, KeyError) as e:
                LoggingManagement.write_error(str(e))