from flet import TextField, KeyboardType


class CreateInputs(TextField):
    def __init__(
        self,
        placeholder_input,
        text_size_input,
        text_align_input,
        offset_input=None,
        keyboard_type_input=KeyboardType.TEXT,
        autofocus_input=False,
        read_only_input=False,
    ):
        self.placeholder_input = placeholder_input
        self.text_size_input = text_size_input
        self.keyboard_type_input = keyboard_type_input
        self.text_align_input = text_align_input
        self.autofocus_input = autofocus_input
        self.read_only_input = read_only_input
        self.offset_input = offset_input

    def _build(self):
        return super().__init__(
            hint_text=self.placeholder_input,
            keyboard_type=self.keyboard_type_input,
            autofocus=self.autofocus_input,
            read_only=self.read_only_input,
            text_size=self.text_size_input,
            text_align=self.text_align_input,
            offset=self.offset_input,
        )

    def desactivate(self):
        self.disabled = True

    def activate(self):
        self.disabled = False

    def change_placeholder(self, new_placeholder):
        self.hint_text = new_placeholder
