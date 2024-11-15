import sqlite3
import os

class Nucleox:

    def __init__(self):
        db_path = './db/noldorin.db'
        if not os.path.exists(db_path):
            print("Creando base de datos")
            try:
                os.makedirs(os.path.dirname(db_path),exist_ok=True)
                self.conn = sqlite3.connect(db_path)
                self.cursor = self.conn.cursor()
                self.createSQL()
            except OSError as e:
                print(f"Error al crear la base de datos: {e}")
        else:
            print("No se crea")
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()

    def create(self, nombre_tabla, columnas):
        sql = f"CREATE TABLE {nombre_tabla} ("
        for nombre, tipo in columnas:
            sql += f"{nombre} {tipo}, "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self,tabla,datos):
        placeholders = ', '.join(['?'] * len(datos))
        sql = f"INSERT INTO {tabla} VALUES ({placeholders})"
        self.cursor.execute(sql,datos)
        self.conn.commit()

    def select(self,tabla,columnas='*',condicion=None):
        sql = f"SELECT {columnas} FROM {tabla}"
        if condicion:
            sql += f" WHERE {condicion}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self,tabla,datos,condicion):
        sets = ', '.join([f"{k} = ?" for k, v in datos.items()])
        sql = f"UPDATE {tabla} SET {sets} WHERE {condicion}"
        self.cursor.execute(sql,tuple(datos.values()))
        self.conn.commit()

    def delete(self,tabla,condicion):
        sql = f"DELETE FROM {tabla} WHERE {condicion}"
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_credentials(self,name,password):
        sql = f"SELECT * FROM users WHERE name = ? AND password = ?"
        self.cursor.execute(sql,(name,password))
        return self.cursor.fetchone()

    def createSQL(self):

        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """
        self.cursor.execute(sql)
        sql = f"INSERT INTO users VALUES (1,'Danel',123456)"
        self.cursor.execute(sql)
        self.conn.commit()