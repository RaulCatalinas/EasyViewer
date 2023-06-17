"""
Handles application updates through GitHub.
"""

from tomllib import load

from github import Github

from github_credentials import Email, PASSWORD
from webbrowser import open_new_tab


class Update(Github):
    """
    Handles application updates through GitHub.
    """

    def __init__(self):
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

        download_url = self.__get_download_url()

        return download_url.split("/")[-2].replace("v", "")

    def __get_user_version(self):
        """
        Retrieve the version number of the user's current application.

        Returns:
            str: The version number of the user's current application.
        """

        with open("../pyproject.toml", mode="rb") as f:
            data = load(f, parse_float=float)

        return data["tool"]["poetry"]["version"]

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
