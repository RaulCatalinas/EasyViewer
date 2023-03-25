from flet import AppBar, icons, IconButton

from app_settings import AppSettings


class TaskBar(AppBar, AppSettings):
    def __init__(self, page):
        self.page = page

        AppSettings.__init__(self)

        self.icon_theme = IconButton(
            icon=self.__set_initial_icon_theme(),
            on_click=lambda e: self.__change_theme(),
        )

        self.icon_language = IconButton(
            icon=icons.LANGUAGE, on_click=lambda e: self.__change_language()
        )

    def __change_theme(self):
        if self.page.theme_mode == "dark":
            self.page.theme_mode = "light"
            self.icon_theme.icon = icons.DARK_MODE
            self.page.client_storage.set("theme", "light")
            self.page.update()

        else:
            self.page.theme_mode = "dark"
            self.icon_theme.icon = icons.LIGHT_MODE
            self.page.client_storage.set("theme", "dark")
            self.page.update()

    def __set_initial_icon_theme(self):
        if self.page.theme_mode == "light":
            return icons.DARK_MODE

        return icons.LIGHT_MODE

    def __change_language(self):
        print("Change language")

    def _build(self):
        return AppBar.__init__(self, actions=[self.icon_theme, self.icon_language])
