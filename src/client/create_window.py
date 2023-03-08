"""Create the main window"""

from tkinter import Tk, PhotoImage


class CreateWindow(Tk):
    """Create the main window of the app"""

    def __init__(self, background_color, window_title, width, high, icon):
        self.background_color = background_color
        self.window_title = window_title
        self.width = width
        self.high = high
        self.icon = icon

        super().__init__()

        self.title(self.window_title)

        # Calculations for window centering
        self.window_width = self.winfo_screenwidth()
        self.window_height = self.winfo_screenheight()
        self.x_coordinate = (self.window_width // 2) - (self.width // 2)
        self.y_coordinate = (self.window_height // 2) - (self.high // 2)

        # Resize window
        self.geometry(
            f"{self.width}x{self.high}+{self.x_coordinate}+{self.y_coordinate}"
        )

        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file=self.icon))
        self.config(bg=self.background_color)

    def update_window(self):
        """
        Update the window.
        """
        self.mainloop()
