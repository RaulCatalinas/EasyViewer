from flet import IconButton, ElevatedButton, OutlinedButton


class CreateIconButton(IconButton):
    def __init__(self, icon_button, function, offset_button=None, scale_button=1):
        self.icon_button = icon_button
        self.function = function
        self.offset_button = offset_button
        self.scale_button = scale_button

        super().__init__(
            icon=self.icon_button,
            on_click=self.function,
            scale=self.scale_button,
            offset=self.offset_button,
        )

    def desactivate(self):
        self.disabled = True

    def activate(self):
        self.disabled = False


class CreateElevatedButton(ElevatedButton):
    def __init__(self, text_button, function):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)

    def change_text_button(self, new_text):
        self.text = new_text


class CreateOutlinedButton(OutlinedButton):
    def __init__(self, text_button, function):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)
