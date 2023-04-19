"""
Create three types of buttons
"""

from flet import IconButton, ElevatedButton, OutlinedButton, Offset


class CreateIconButton(IconButton):
    """
    Create a button of type IconButton
    """

    def __init__(self, icon_button, function, offset_x=0, offset_y=0, scale_button=1):
        self.icon_button = icon_button
        self.function = function
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.scale_button = scale_button

        super().__init__(
            icon=self.icon_button,
            on_click=self.function,
            scale=self.scale_button,
            offset=Offset(self.offset_x, self.offset_y),
        )

    def change_state(self, page):
        """
        If the button is activated, it deactivates it and vice versa

        :param page: Is a reference to the app window
        """

        if not self.disabled:
            self.disabled = True

        else:
            self.disabled = False

        return page.update(self)

    def change_offset(self, offset_x, offset_y):
        """
        Changes the offset of the button using the given x and y values.

        :param offset_x: x-coordinate offset

        :param offset_y: y-coordinate offset
        """

        self.offset = Offset(offset_x, offset_y)


class CreateElevatedButton(ElevatedButton):
    """
    Create a button of type ElevatedButton
    """

    def __init__(self, text_button, function):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    def change_text_button(self, new_text):
        """
        Changes the text of the button.

        :param new_text: The new text that will replace the current text of the button
        """

        self.text = new_text

    def change_function(self, new_function, *args):
        """
        Takes a new function and its arguments, and sets it as the on_click event.

        :param new_function: The new function that will be executed when the button is clicked
        """

        self.on_click = lambda e: new_function(*args)


class CreateOutlinedButton(OutlinedButton):
    """
    Create a button of type OutlinedButton
    """

    def __init__(self, text_button, function):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    def change_function(self, new_function, *args):
        """
        Takes a new function and its arguments, and sets it as the on_click event.

        :param new_function: The new function that will be executed when the button is clicked
        """

        self.on_click = lambda e: new_function(*args)
