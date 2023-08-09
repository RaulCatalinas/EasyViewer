"""
Handles application updates through GitHub.
"""

from os import environ
from os.path import exists
from webbrowser import open_new_tab

from flet import Page
from github import Github
from github.GitReleaseAsset import GitReleaseAsset

from constants import (
    CACHE_FILE,
    GITHUB_REPO,
    GITHUB_USER,
    LATEST_RELEASE_URL,
    USER_VERSION,
)
from frontend.components.update_dialog import UpdateDialog
from utils import check_type

from ..cache import CacheManager


class Update(Github):
    """
    Handles application updates through GitHub.
    """

    @check_type
    def __init__(self, page: Page, update_dialog: UpdateDialog | None):
        self.page = page
        self.update_dialog = update_dialog

        if not exists(CACHE_FILE):
            CacheManager.create_json_cache()

        CacheManager.reset_cache_if_expired()

        self.cache = CacheManager.read_cache()

        self.is_the_cache_empty = CacheManager.is_the_cache_empty()

        token = environ.get("TOKEN")
        print(token)

        if not self.is_the_cache_empty:
            super().__init__(token)

    def __get_user(self):
        """
        Gets the GitHub user.

        Returns:
            AuthenticatedUser | NamedUser: The GitHub user object.
        """

        return self.get_user(GITHUB_USER)

    def __get_repo(self):
        """
        Retrieve the GitHub repository.

        Returns:
            Repository: The GitHub repository object.
        """

        user = self.__get_user()

        return user.get_repo(GITHUB_REPO)

    def __get_assets(self) -> GitReleaseAsset:
        """
        Gets the assets of the latest release.

        Returns:
            GitReleaseAsset: The asset object of the latest release.
        """

        repo = self.__get_repo()

        release = repo.get_latest_release()

        return release.get_assets()[0]

    def __get_download_url(self):
        """
        Retrieve the download URL of the latest release.

        Returns:
            str: The download URL of the latest release.
        """

        assets = self.__get_assets()

        return assets.browser_download_url

    def __get_release_version(self) -> str:
        """
        Gets the version number of the latest version.

        Returns:
            str: The version number of the latest release.
        """

        if self.is_the_cache_empty:
            self.cache.get("release_version")

        download_url = self.__get_download_url()
        release_version = download_url.split("/")[-2].replace("v", "")

        CacheManager.write_cache("release_version", release_version)

        return release_version

    def is_new_release_available(self) -> bool:
        """
        Checks if a new release is available on GitHub.

        Returns:
            bool: True if a new release is available, False otherwise.
        """

        release_version = self.__get_release_version()

        return USER_VERSION < release_version

    def update(self):
        """
        Opens the user's default web browser to the latest version page on GitHub
        """

        open_new_tab(LATEST_RELEASE_URL)

        if self.update_dialog is not None:
            self.update_dialog.change_state(self.page)
