from json import load, dump, JSONDecodeError
from os.path import exists
from time import time

from utils import CACHE_FILE, LoggingManagement


class CacheManager:
    @staticmethod
    def read_cache():
        if not exists(CACHE_FILE):
            CacheManager.__create_json_cache()

        with open(CACHE_FILE, mode="r", encoding="utf-8") as file:
            try:
                return load(file)

            except JSONDecodeError as exc:
                LoggingManagement.write_error(str(exc))

                raise JSONDecodeError(str(exc), doc=CACHE_FILE) from exc

    @staticmethod
    def write_cache(key, data):
        try:
            array = CacheManager.read_cache()
            cached_data = {key: data, "timestamp": int(time())}

            array.append(cached_data)

            with open(CACHE_FILE, mode="w", encoding="utf-8") as file:
                dump(array, file)

        except Exception as e:
            LoggingManagement.write_error(str(e))

    @staticmethod
    def __create_json_cache():
        try:
            with open(CACHE_FILE, mode="w", encoding="utf-8") as file:
                file.write("[]")

        except Exception as e:
            LoggingManagement.write_error(str(e))
