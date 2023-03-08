"""Menu with copy and paste options"""

from tkinter import Menu

from pyperclip import copy, paste


class OptionsMenu:
    """Create an options menu to be able to copy and paste the url from the clipboard"""

    def __init__(self, window, text_to_copy):
        self.window = window
        self.text_to_copy = text_to_copy
        self.menu = Menu(self.window, tearoff=0)
        self.menu.add_command(label="Copy", command=self.__copy)
        self.menu.add_command(label="Paste", command=self.__paste)

    def create_menu_of_options(self, event):
        """
        Create a menu of options.

        :param event: The event that triggered the popup
        """
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def __copy(self):
        """
        Copies the text in the text box to the clipboard.
        """
        copy(self.text_to_copy.get())

    def __paste(self):
        """
        Paste the text from the clipboard.
        """
        self.text_to_copy.set(paste())
