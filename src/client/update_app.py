"""
Update the app to the latest available version
"""

from os.path import abspath

from flet import MainAxisAlignment
from tomlkit import load

from app_settings import AppSettings
from create_buttons import CreateElevatedButton, CreateOutlinedButton
from create_dialog import CreateDialog
from interact_api_github import InteractApiGitHub


class UpdateApp(InteractApiGitHub, AppSettings):
    """
    Update the app to the latest available version
    """

    def __init__(self):
        AppSettings.__init__(self)
        InteractApiGitHub.__init__(self)

        self.connect_to_api()

        self.download_url = self.get_download_url()

        self.release_name = self.get_release_name()
        self.release_version = self.get_release_version()
        self.user_version = self.__get_user_version()

        self.button_update = CreateElevatedButton(
            function=lambda e: self.__update(), text_button=self.get_config_excel(4)
        )
        self.button_update_later = CreateOutlinedButton(
            function=None, text_button=self.get_config_excel(20)
        )
        self.button_updated = CreateElevatedButton(function=None, text_button="Ok")
        self.buttons_update = [self.button_update, self.button_update_later]

        self.update_dialog = CreateDialog(
            title_dialog=self.get_config_excel(21),
            content_dialog="",
            title_size=20,
            content_size=18,
            actions_alignment_dialog=MainAxisAlignment.END,
            actions_dialog=None,
        )

    def __get_user_version(self):
        """
        Reads the version number of the file "pyproject.toml".

        :return: The version number of the app.
        """

        pyproject_path = abspath("../pyproject.toml")

        with open(pyproject_path, "r", encoding="utf-8") as f:
            self.toml = load(f)

        return self.toml["tool"]["poetry"]["version"]

    def check_updates(self, page):
        """
        Check if there are available updates.

        :param page: Is a reference to the app window.
        """

        the_user_has_the_latest_version = self.user_version == self.release_version

        self.__show_dialog_update(
            text=(
                self.get_config_excel(18)
                if the_user_has_the_latest_version
                else self.get_config_excel(19)
            ),
            latest_version=the_user_has_the_latest_version,
            page=page,
        )

    def __show_dialog_update(self, text, latest_version, page):
        """
        Displays a dialog box to the user with the notification that the application can be updated or that it has the latest version depending on whether the "latest_version" parameter is true or false.

        :param text: The text to be displayed in the dialog

        :param latest_version: A boolean value indicating whether the current version of the app is the latest version available

        :param page: The "page" parameter is a reference to the app window where the update dialog will be displayed
        """

        self.button_update_later.change_function(self.update_dialog.change_state, page)
        self.button_updated.change_function(self.update_dialog.change_state, page)

        self.update_dialog.content_text.change_text(text)
        self.update_dialog.actions = (
            self.buttons_update if not latest_version else [self.button_updated]
        )
        self.update_dialog.change_state(page)

    def __update(self):
        """
        Placeholder docstring.

        Will download the latest version from GitHub, unzip it and replace the "old" version of the user with the latest version when implemented.

        The actual documentation will be added later
        """

        print("Update")
