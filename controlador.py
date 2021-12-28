from tkinter import Tk
from vista import VistaApp
from tkinter import ttk


class MiApp:
    def __init__(self, window):
        """controlador de la App
           Inicializacion de la ventana principal
           Envio parametro de ventana principial a la Clase Vistapp en vista.py"""

        self.ventana = window

        VistaApp(self.ventana)


if __name__ == "__main__":

    root = Tk()
    obj = MiApp(root)
    root.mainloop()
