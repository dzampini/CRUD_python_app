from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from database import A_base
from modelo import log
from tkinter import Pack


class VistaApp:
    def __init__(self, window):
        """Clase que posee la vista de la App y recibe la variable desde el controlador, ejecutando la ventana.
           Envia los parametros al modelo y su logica para trabajar sobre el CRUD
           Declaracion de variables.
           Etiquetas de la ventana.
           Variables de entrada.
           Declaracion de objetos pertenecientes a las clases y metodos que se conectan para compartir parametros.
           Creacion de botones.
           Metodos por los cuales se comparten los parametros ingresados por el usuario.
           Creacion de fobjetos que conectan las clases y metodos compartidos.
           """

        self.root = window
        self.root.geometry("400x200")

        self.a_val = StringVar()
        self.b_val = StringVar()
        self.c_val = StringVar()
        self.d_val = StringVar()
        w_ancho = 40

        self.root.title("Entrega Intermedia")
        self.et1 = Label(self.root, text="Nombres")
        self.et1.grid(row=1, column=0)
        self.et2 = Label(self.root, text="Apellidos")
        self.et2.grid(row=2, column=0)
        self.et3 = Label(self.root, text="Mail de Contacto")
        self.et3.grid(row=3, column=0)
        self.et4 = Label(self.root, text="Dni")
        self.et4.grid(row=4, column=0)
        self.et5 = Label(
            self.root, text="Para borrar o actualizar un registro, debe ingresar el DNI")
        self.et5.place(x=10, y=170)

        self.entrada1 = Entry(
            self.root, textvariable=self.a_val, width=w_ancho)
        self.entrada1.grid(row=1, column=1)
        self.entrada2 = Entry(
            self.root, textvariable=self.b_val, width=w_ancho)
        self.entrada2.grid(row=2, column=1)
        self.entrada3 = Entry(
            self.root, textvariable=self.c_val, width=w_ancho)
        self.entrada3.grid(row=3, column=1)
        self.entrada4 = Entry(
            self.root, textvariable=self.d_val, width=w_ancho)
        self.entrada4.grid(row=4, column=1,)

        self.objeto_b = A_base()
        self.objeto_m = log()

        b1 = Button(self.root, text="Crear Registro", command=lambda: self.para_alta(self.a_val,
                                                                                     self.b_val, self.c_val, self.d_val), bg="light blue")
        b1.grid(row=6, column=1)
        b2 = Button(self.root, text="Crear Base",
                    command=lambda: (self.para_base(), self.para_tabla()), bg="light blue")
        b2.grid(row=7, column=1)
        b3 = Button(self.root, text="Upgrade",
                    command=lambda: self.para_upgrade(self.a_val, self.b_val, self.c_val, self.d_val), bg="light blue")
        b3.grid(row=6, column=2)

        b3 = Button(self.root, text="Consulta",
                    command=lambda: self.para_consul(), bg="light blue")
        b3.grid(row=7, column=2)

        b4 = Button(self.root, text="Borrar",
                    command=lambda: (self.para_borrar(self.d_val)), bg="light blue")
        b4.grid(row=7, column=0)

    def para_alta(self, param1, param2, param3, param4):
        self.objeto_m.alta(param1.get(), param2.get(),
                           param3.get(), param4.get())

    def para_consul(self,):

        self.objeto_m.consulta()

    def para_base(self,):
        self.objeto_b.b_ase()

    def para_tabla(self,):
        self.objeto_b.tabla()

    def para_upgrade(self, param1, param2, param3, param4):
        self.objeto_m.upgrade(param1.get(), param2.get(),
                              param3.get(), param4.get())

    def para_borrar(self, param4):
        self.objeto_m.delete(param4.get())
