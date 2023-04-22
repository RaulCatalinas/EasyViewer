"""
Interacts with the GitHub API
"""

from github.MainClass import Github

from app_settings import AppSettings


class InteractApiGitHub(Github, AppSettings):
    """
    interacts with the GitHub API
    """

    def __init__(self):
        AppSettings.__init__(self)

        self.token = self.get_token()

    def connect_to_api(self):
        """
        Initialize the connection to the Github API.
        """

        Github.__init__(self, self.token)

    def __get_user(self):
        """
        Gets the user.

        :return: The user
        """

        return self.get_user("RaulCatalinas")

    def __get_repo(self):
        """
        Gets the repository.

        :return: The repository
        """

        return self.__get_user().get_repo("EasyViewer")

    def __get_latest_release(self):
        """
        Gets the latest release of the repository.

        :return: The latest release of the repository.
        """

        return self.__get_repo().get_latest_release().get_assets()[0]

    def get_download_url(self):
        """
        Returns the download URL of the latest release.

        :return: The download URL of the latest release.
        """

        return self.__get_latest_release().browser_download_url

    def get_release_version(self) -> str:
        """
        Gets the release version

        :return: The release version
        """

        return self.get_download_url().split("/")[-2].replace("v", "")

    def get_release_name(self) -> str:
        """
        Gets the name of the release.

        :return: The name of the release
        """

        return self.get_download_url().split("/")[-1]
