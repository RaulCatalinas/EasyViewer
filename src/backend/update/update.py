"""
Handles application updates through GitHub.
"""

from tomllib import load
from webbrowser import open_new_tab

from github import Github

from cache import CacheManager
from github_credentials import Email, PASSWORD


class Update(Github):
    """
    Handles application updates through GitHub.
    """

    def __init__(self, page, update_dialog):
        self.page = page
        self.update_dialog = update_dialog

        CacheManager.reset_cache_if_expired()

        array_versions = CacheManager.read_cache()
        self.length_array_versions = len(array_versions)

        if self.length_array_versions != 0:
            self.release_version = array_versions[0]["release_version"]
            self.user_version = array_versions[1]["user_version"]

        elif self.length_array_versions == 0:
            super().__init__(login_or_token=Email, password=PASSWORD)

    def __get_user(self):
        """
        Retrieve the GitHub user.

        Returns:
            AuthenticatedUser | NamedUser: The GitHub user object.
        """

        return self.get_user("RaulCatalinas")

    def __get_repo(self):
        """
        Retrieve the GitHub repository.

        Returns:
            Repository: The GitHub repository object.
        """

        user = self.__get_user()

        return user.get_repo("EasyViewer")

    def __get_assets(self):
        """
        Retrieve the assets of the latest release.

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

    def __get_release_version(self):
        """
        Retrieve the version number of the latest release.

        Returns:
            str: The version number of the latest release.
        """

        if self.length_array_versions != 0:
            return self.release_version

        download_url = self.__get_download_url()
        release_version = download_url.split("/")[-2].replace("v", "")

        CacheManager.write_cache("release_version", release_version)

        return release_version

    def __get_user_version(self):
        """
        Retrieve the version number of the user's current application.

        Returns:
            str: The version number of the user's current application.
        """

        if self.length_array_versions != 0:
            return self.user_version

        with open("../pyproject.toml", mode="rb") as f:
            data = load(f, parse_float=float)

        user_version = data["tool"]["poetry"]["version"]

        CacheManager.write_cache("user_version", user_version)

        return user_version

    def is_new_release_available(self):
        """
        Checks if a new release is available on GitHub.

        Retrieves the latest version from the repository and compares it with the user's current version.

        Returns:
            bool: True if a new release is available, False otherwise.
        """

        release_version = self.__get_release_version()
        user_version = self.__get_user_version()

        return user_version < release_version

    def update(self):
        """
        Opens the browser to the latest release page on GitHub.

        This method opens the user's default web browser and navigates to the latest release page of the application's repository on GitHub.

        Users can manually download the latest version from the release page.
        """

        open_new_tab("https://github.com/RaulCatalinas/EasyViewer/releases/latest")

        self.update_dialog.change_state(self.page)
