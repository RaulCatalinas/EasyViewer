from os.path import abspath

from flet import MainAxisAlignment
from github.MainClass import Github
from tomlkit import load

from app_settings import AppSettings
from create_buttons import CreateElevatedButton, CreateOutlinedButton
from create_dialog import CreateDialog


class UpdateApp(Github, AppSettings):
    def __init__(self):
        AppSettings.__init__(self)

        self.token = self.get_token()

        Github.__init__(self, self.token)

        self.user = self.get_user("RaulCatalinas")
        self.repo = self.user.get_repo("EasyViewer")
        self.latest_release = self.repo.get_latest_release()
        self.download_url = self.latest_release.get_assets()[0].browser_download_url
        self.release_version = self.download_url.split("/")[-2].replace("v", "")

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
            title_dialog="Update app",
            content_dialog="",
            title_size=20,
            content_size=18,
            actions_alignment_dialog=MainAxisAlignment.END,
            actions_dialog=None,
        )

    def __get_user_version(self):
        pyproject_path = abspath("../pyproject.toml")

        with open(pyproject_path, "r", encoding="utf-8") as f:
            self.toml = load(f)

        return self.toml["tool"]["poetry"]["version"]

    def check_updates(self, page):
        if self.user_version == self.release_version:
            self.__show_dialog_update(
                text=self.get_config_excel(18),
                latest_version=True,
                page=page,
            )

        else:
            self.__show_dialog_update(
                text=self.get_config_excel(19),
                latest_version=False,
                page=page,
            )

    def __show_dialog_update(self, text, latest_version, page):
        self.button_update_later.change_function(self.update_dialog.change_state, page)
        self.button_updated.change_function(self.update_dialog.change_state, page)

        self.update_dialog.content_text.change_text(text)

        self.update_dialog.actions = (
            self.buttons_update if not latest_version else [self.button_updated]
        )

        self.update_dialog.change_state(page)

    def __update(self):
        print("Update")
