from tkinter import Menu

from pyperclip import copy, paste


class MenuDeOpciones:
    def __init__(self, ventana, textoACopiar):
        self.ventana = ventana
        self.textoACopiar = textoACopiar
        self.menu = Menu(self.ventana, tearoff=0)
        self.menu.add_command(label="Copiar", command=self.__Copiar)
        self.menu.add_command(label="Pegar", command=self.__Pegar)

    def FuncionMenuDeOpciones(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def __Copiar(self):
        copy(self.textoACopiar.get())

    def __Pegar(self):
        self.textoACopiar.set(paste())
