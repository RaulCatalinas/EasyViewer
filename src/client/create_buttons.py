from flet import IconButton, ElevatedButton, OutlinedButton


class CreateIconButton(IconButton):
    def __init__(self, icon_button, function, offset_button):
        self.icon_button = icon_button
        self.function = function
        self.offset_button = offset_button

    def _build(self):
        return super().__init__(
            icon=self.icon_button,
            on_click=self.function,
            scale=2.5,
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


class CreateOutlinedButton(OutlinedButton):
    def __init__(self, text_button, function):
        self.text_button = text_button
        self.function = function

        super().__init__(text=self.text_button, on_click=self.function)
