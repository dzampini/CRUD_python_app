import sqlite3
import re


class log:
    def __init__(self,):
        """Creacion de logica del modelo para el Alta, baja, modificacion y Actualizacion de Registros.
        Clase que contiene las funciones que reciben parametros enviados desde el archivo vista.py
        cada uno de los parametros corresponde a una entry """
        pass

    def alta(self, para_uno, para_dos, para_tres, para_cuatro):

        self.cadena_b = para_uno
        self.patron_cad = "^[A-Za-z]+(?i:[ _-][A-Za-z]+[@.]+)*"

        if (re.match(self.patron_cad, self.cadena_b)):
            print("Ingreso valido" + para_uno)

            self.b_conexion = sqlite3.connect('mi_personal.db')
            self.cursor = self.b_conexion.cursor()
            self.sql = """INSERT INTO personas(nombre, apellido, mail, dni) VALUES (?, ?, ?, ?);"""
            self.datos = (para_uno, para_dos, para_tres, para_cuatro)
            self.cursor.execute(self.sql, self.datos)
            self.b_conexion.commit()

        else:
            print("No validado", para_uno)

    def consulta(self,):
        self.b_conexion = sqlite3.connect('mi_personal.db')

        try:
            self.cursor = self.b_conexion.cursor()
            self.cursor.execute("SELECT * FROM personas")
            self.data = self.cursor.fetchall()
            self.b_conexion.commit()
            for row in self.data:
                print(row)

        except:
            print("no hay registros")

    def upgrade(self, param1, param2, param3, param4):
        self.b_conexion = sqlite3.connect('mi_personal.db')

        try:
            self.cursor = self.b_conexion.cursor()
            self.sql = "UPDATE personas SET nombre= ?, apellido=?, mail=? WHERE dni= ?"
            self.datos = (param1, param2, param3, param4)
            self.cursor.execute(self.sql, self.datos)
            self.b_conexion.commit()
            print("Se ha actualizado un registro")
        except:

            print(self.cursor.rowcount, "Cantidad de registros afectados.")

    def delete(self, param_dni):
        self.b_conexion = sqlite3.connect('mi_personal.db')
        try:

            self.cursor = self.b_conexion.cursor()
            self.sql = "DELETE FROM personas WHERE dni= ?"
            self.datos = param_dni
            self.cursor.execute(self.sql, self.datos)
            self.b_conexion.commit()
            print("Registro borrado")
        except:
            print(self.cursor.rowcount, "No se encontro registro")
