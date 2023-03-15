"""Create a taskbar"""

from tkinter import Menu
from webbrowser import open_new_tab

from app_settings import AppSettings

app_settings = AppSettings()


class TaskBar:
    """Create a menu bar with two menus, one for social networks and one for language"""

    def __init__(self, window, update_text_widgets):
        self.window = window
        self.update_text_widgets = update_text_widgets

        self.taskbar = Menu(self.window, tearoff=False)

        self.contact = Menu(self.taskbar, tearoff=False)
        self.contact.add_command(command=self.instagram, label="Instagram")
        self.contact.add_command(command=self.twitter, label="Twitter")
        self.contact.add_command(command=self.facebook, label="Facebook")

        self.language = Menu(self.taskbar, tearoff=False)
        self.language.add_command(
            label=app_settings.get_config_excel(excel_column_number=13),
            command=self.spanish,
        )

        self.language.add_command(
            label=app_settings.get_config_excel(excel_column_number=14),
            command=self.english,
        )

        self.taskbar.add_cascade(
            menu=self.contact,
            label=app_settings.get_config_excel(excel_column_number=11),
        )
        self.taskbar.add_cascade(
            menu=self.language,
            label=app_settings.get_config_excel(excel_column_number=12),
        )

        self.window.app_settings(menu=self.taskbar)

    @staticmethod
    def instagram():
        """
        Open a new tab in your browser and navigate to the Instagram page of the user who
        specify
        """
        open_new_tab("https://www.instagram.com/raulf1foreveryt_oficial")

    @staticmethod
    def twitter():
        """
        Open a new tab in your browser and go to the instagram of the author of this code.
        """
        open_new_tab("https://twitter.com/F1foreverRaul")

    @staticmethod
    def facebook():
        """
        Open a new tab in your browser and go to the Facebook page of the author of this code.
        """
        open_new_tab("https://www.facebook.com/profile.php?id=100063559000286")

    def english(self):
        """
        Sets the language to English.
        """
        app_settings.set_language("English")
        self.update_text_widgets()
        self.update_taskbar_text()

    def spanish(self):
        """
        Sets the language to Spanish.
        """
        app_settings.set_language("Español")
        self.update_text_widgets()
        self.update_taskbar_text()

    def update_taskbar_text(self):
        """
        Updates the menu bar text and the taskbar text.
        """
        self.language.entryconfig(
            0,
            label=app_settings.get_config_excel(excel_column_number=13),
        )
        self.language.entryconfig(
            1,
            label=app_settings.get_config_excel(excel_column_number=14),
        )
        self.taskbar.entryconfig(
            0, label=app_settings.get_config_excel(excel_column_number=11)
        )
        self.taskbar.entryconfig(
            1,
            label=app_settings.get_config_excel(excel_column_number=12),
        )
