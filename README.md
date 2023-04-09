# EasyViwer

## Description

EasyViewer is an application that allows you to download videos and/or audio from YouTube videos.

The user enters the URL of the video and selects the location to save the file.

The app offers two buttons: Download Video and Download Audio.

While the file is downloading, a progress bar is displayed.

## Requirements

### Python Version

The app has been developed and tested on Python 3.11, although it may work with older versions.

However, I cannot guarantee full app functionality on Python versions prior to 3.11.

If you're having trouble running your app on an older version of Python, upgrade to version 3.11 or higher to ensure that everything works correctly.

To download the latest version of Python, visit the [official website](https://www.python.org/downloads).

### Dependencies

* Python 3.11 or higher
* python-dotenv (Environment variable for language switching)
* pandas (Read the Excel file for game texts)
* openpyxl (Dependence on "pandas" to read the Excel file for the texts of the game)
* requests (Checking if the user has internet)

  To install these dependencies execute in a terminal with the virtual environment activated this command: `poetry install`.

  This will automatically install all the dependencies specified in your project's `pyproject.toml` file.

  I explain more about "Poetry" in the next section

## Poetry

### Installation

Poetry is a dependency management tool that simplifies the installation and management of Python packages.

#### Globally

To install Poetry globally, follow these steps:

1. Download and install Poetry by running the following command in a terminal as administrator:
   * On Unix or WSL: `curl -sSL https://install.python-poetry.org | python3 -`
   * On Windows in a PowerShell terminal: `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`
2. Add the Poetry installation path to your `PATH` environment variable.
3. To verify that Poetry is installed correctly, run the following command in a terminal: `poetry --version`.

#### Locally

Installing Poetry locally can be useful if you want to manage different dependencies for different projects. To install Poetry locally, follow these steps:

1. Create a virtual environment for your project.
2. Activate the virtual environment.
3. Run the following command in a terminal: `pip install poetry`.

### Dependencies

To install the dependencies required for your project, run the following command in a terminal with the virtual environment activated: `poetry install`.

This will automatically install all the dependencies specified in your project's `pyproject.toml` file.

For more information on Poetry, visit the [official website](https://python-poetry.org).

## Contributions

Thank you for considering contributing to the project! Here are some ways you can help:

* Clone the repository and work on new features or bug fixes in your own branch.
* Submit pull requests for your changes and make sure you follow our coding standards and documentation requirements.
* Help review and approve pull requests from other developers.
* Share the project on your social networks or blog so that more people can learn about it.

## Social Networks

* [Instagram](https://www.instagram.com/raulf1foreveryt_oficial/?hl=en)
* [Twitter](https://twitter.com/F1foreverRaul)
* [Facebook](https://www.facebook.com/Raul-F1forever-114186780454598/)
