from tkinter import Menu


# Menu de opciones para copiar o pegar cosas del portapapeles


class MenuDeOpciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.menu = Menu(self.ventana, tearoff=0)
        self.menu.add_command(label="Copiar", command=self.__Copiar)
        self.menu.add_command(label="Pegar", command=self.__Pegar)

    def FuncionMenuDeOpciones(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    @staticmethod
    def __Copiar():
        pass

    @staticmethod
    def __Pegar():
        pass
