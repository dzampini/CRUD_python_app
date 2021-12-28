import sqlite3


class A_base:
    def __init__(self,):
        """Conexion a base de datos, creacion de base de datos y tabla"""
        pass

    def b_ase(self,):
        try:
            self.b_conexion = sqlite3.connect('mi_personal.db')
            print("base creada con exito")

        except:
            print("Base ya existe")

    def tabla(self,):
        self.b_conexionb = sqlite3.connect('mi_personal.db')
        try:

            self.cursor = self.b_conexion.cursor()
            self.cursor.execute("""CREATE TABLE personas (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            mail TEXT,
            dni INTEGER)""")
            self.b_conexion.commit()
        except:
            print("tabla ya creada")
