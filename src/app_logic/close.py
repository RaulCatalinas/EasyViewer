"""Control the closing of the app"""

from tkinter import Toplevel

from client.app_settings import AppSettings
from client.create_buttons import CreateButton
from client.create_labels import CreateLabel
from client.logging_management import LoggingManagement

app_settings = AppSettings()
log = LoggingManagement()


class DialogClose:
    """Creates a dialog box that asks the user if they want to close the program."""

    def __init__(
        self,
        parent,
        background_color,
        color_button_exit_mouse_in,
        color_button_exit_mouse_out,
        color_button_minimize_mouse_in,
        color_button_minimize_mouse_out,
        color_button_cancel_mouse_in,
        color_button_cancel_mouse_out,
        high,
        color_label,
        width,
    ):

        self.parent = parent
        self.background_color = background_color
        self.color_button_exit_mouse_in = color_button_exit_mouse_in
        self.color_button_exit_mouse_out = color_button_exit_mouse_out
        self.color_button_minimize_mouse_in = color_button_minimize_mouse_in
        self.color_button_minimize_mouse_out = color_button_minimize_mouse_out
        self.color_button_cancel_mouse_in = color_button_cancel_mouse_in
        self.color_button_cancel_mouse_out = color_button_cancel_mouse_out
        self.high = high
        self.color_label = color_label
        self.width = width

        from interact_api_pytube import InteractAPIPytube
        from control_variables import ControlVariables

        self.variables_control = ControlVariables()
        self.interact_api_pytube = InteractAPIPytube()

        self.top = Toplevel()
        self.top.title(app_settings.get_config_excel(excel_column_number=10))

        # Calculations for window centering
        self.window_width = self.top.winfo_screenwidth()
        self.window_height = self.top.winfo_screenheight()

        self.x_coordinate = (self.window_width // 2) - (self.width // 2)
        self.y_coordinate = (self.window_height // 2) - (self.high // 2)

        # Resize Window
        self.top.geometry(
            f"{self.width}x{self.high}+{self.x_coordinate}+{self.y_coordinate}"
        )

        self.top.configure(bg=self.background_color)
        self.top.resizable(False, False)

        self.label_confirmation_closing = CreateLabel(
            text=app_settings.get_config_excel(excel_column_number=6),
            y_axis_position=10,
            width=26,
            background_color=self.color_label,
            font="Arial",
            font_size=12,
            window=self.top,
        )

        self.exit_button = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=7),
            x_axis_position=15,
            y_axis_position=50,
            width=15,
            background_color=self.color_button_exit_mouse_out,
            function=lambda: [self.exit()],
            font="Arial",
            font_size=12,
            window=self.top,
            color_mouse_in=self.color_button_exit_mouse_in,
            color_mouse_out=self.color_button_exit_mouse_out,
            absolute_position=False,
        )

        self.button_minimize = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=8),
            x_axis_position=173,
            y_axis_position=50,
            width=15,
            background_color=self.color_button_minimize_mouse_out,
            function=lambda: [self.minimize()],
            font="Arial",
            font_size=12,
            window=self.top,
            color_mouse_in=self.color_button_minimize_mouse_in,
            color_mouse_out=self.color_button_minimize_mouse_out,
            absolute_position=False,
        )

        self.button_cancel = CreateButton(
            text=app_settings.get_config_excel(excel_column_number=9),
            x_axis_position=40,
            y_axis_position=90,
            width=25,
            background_color=self.color_button_cancel_mouse_out,
            function=lambda: [self.cancel()],
            font="Arial",
            font_size=12,
            window=self.top,
            color_mouse_in=self.color_button_cancel_mouse_in,
            color_mouse_out=self.color_button_cancel_mouse_out,
            absolute_position=False,
        )

    def exit(self):
        """
        It destroys the top window and the main window and then exits the program.
        """
        try:
            self.top.destroy()
            self.parent.destroy()

            if not self.variables_control.get_downloaded_successfully():
                self.interact_api_pytube.cancel_download()

        except Exception as exc:
            print(exc)
            log.write_error(str(exc))

    def minimize(self):
        """
        Destroys the top window and iconifies the main window.
        """
        self.top.destroy()
        self.parent.iconify()

    def cancel(self):
        """
        Close the window
        """
        self.top.destroy()


class Close:
    """Create the closing confirmation window"""

    def __init__(
        self,
        parent,
        background_color,
        color_exit_button_mouse_in,
        color_button_exit_mouse_out,
        color_button_minimize_mouse_in,
        color_button_minimize_mouse_out,
        color_button_cancel_mouse_in,
        color_button_cancel_mouse_out,
        high,
        color_label,
        width,
    ):

        self.parent = parent
        self.background_color = background_color
        self.color_exit_button_mouse_in = color_exit_button_mouse_in
        self.color_button_exit_mouse_out = color_button_exit_mouse_out
        self.color_button_minimize_mouse_in = color_button_minimize_mouse_in
        self.color_button_minimize_mouse_out = color_button_minimize_mouse_out
        self.color_button_cancel_mouse_in = color_button_cancel_mouse_in
        self.color_button_cancel_mouse_out = color_button_cancel_mouse_out
        self.high = high
        self.color_label = color_label
        self.width = width

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """
        Create a new window.
        """
        self.dialog = DialogClose(
            parent=self.parent,
            background_color=self.background_color,
            color_button_exit_mouse_in=self.color_exit_button_mouse_in,
            color_button_exit_mouse_out=self.color_button_exit_mouse_out,
            color_button_minimize_mouse_in=self.color_button_minimize_mouse_in,
            color_button_minimize_mouse_out=self.color_button_minimize_mouse_out,
            color_button_cancel_mouse_in=self.color_button_cancel_mouse_in,
            color_button_cancel_mouse_out=self.color_button_cancel_mouse_out,
            width=self.width,
            high=self.high,
            color_label=self.color_label,
        )

        self.parent.wait_window(self.dialog.top)
