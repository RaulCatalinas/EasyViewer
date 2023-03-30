"""Control variables for the operation of the app"""

from json import load, dump

from client.app_settings import AppSettings


class ControlVariables(AppSettings):
    """Control variables for the app"""

    def __init__(self):
        self.control_variables_file = self.get_file_control_variables()

        super().__init__()

        with open(self.control_variables_file, encoding="utf-8") as read_json:
            self.dict_control_variables = load(read_json, parse_constant=True)
            print()
            print(self.dict_control_variables)

    def get_control_variables(self, control_variable):
        return self.dict_control_variables[control_variable]

    def set_control_variable(self, control_variable, value):
        try:
            self.dict_control_variables[control_variable] = value
            print()
            print(self.dict_control_variables)

            VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

            with open(
                self.control_variables_file, mode="w", encoding="utf-8"
            ) as set_json:
                dump(
                    {
                        "VIDEO_LOCATION": VIDEO_LOCATION,
                        "DOWNLOAD_NAME": "",
                        "URL_VIDEO": "",
                        "DOWNLOADED_SUCCESSFULLY": False,
                    },
                    set_json,
                )
        except Exception as exc:
            raise Exception(str(exc)) from exc
