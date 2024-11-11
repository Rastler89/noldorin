import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Notebook


class Noldorin:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("300x380")
        self.root.title("Bienvenidos")
        #pantalla1.iconbitmap("")

        self.login()

    def login(self):

        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill="both", expand=True)

        Label(self.login_frame, text="Por favor ingrese su Usuario y Contraseña").pack()
        Label(self.login_frame, text="").pack()

        global user_name_verify
        global user_password_verify

        user_name_verify = StringVar()
        user_password_verify = StringVar()

        global user_name_entry
        global user_password_entry

        Label(self.login_frame, text="Usuario").pack()
        user_name_entry = Entry(self.login_frame, textvariable=user_name_verify)
        user_name_entry.pack()
        Label().pack()

        Label(self.login_frame, text="Contraseña").pack()
        user_password_entry = Entry(self.login_frame, textvariable=user_password_verify)
        user_password_entry.pack()
        Label().pack()

        Button(self.login_frame, text="Iniciar sesión",command=self.validar_datos).pack()

        self.root.mainloop()

    def principal(self):
        self.notebook = Notebook(self.root)
        self.pet_label = Label(self.notebook, text="Animales")
        self.info_label = Label(self.notebook, text="Info")

        self.notebook.add(self.pet_label, text="Animales", padding=20)
        self.notebook.add(self.info_label, text="Info", padding=20)

        self.notebook.pack(fill="both", expand=True)
        self.root.mainloop()

    def validar_datos(self):
        if(user_name_entry.get() == "Danel"):
            messagebox.showinfo(title="Inicio de Sesión perfecto",message="Usuario correcto")
            self.login_frame.pack_forget()
            self.principal()




if __name__ == "__main__":
    app = Noldorin()