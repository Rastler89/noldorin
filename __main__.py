from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook

from nucleox.DB import Nucleox
from nucleox.Navbar import Navbar


class Noldorin:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("300x380")
        self.root.title("Bienvenidos")
        #pantalla1.iconbitmap("")

        self.db = Nucleox()

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

        self.navbar = Navbar(self.root)

        self.notebook = Notebook(self.root)
        self.pet_label = Label(self.notebook, text="Animales")
        self.info_label = Label(self.notebook, text="Info")

        self.notebook.add(self.pet_label, text="Animales")
        self.notebook.add(self.info_label, text="Info")

        self.notebook.pack(fill="both", expand=True)
        self.root.mainloop()

    def validar_datos(self):
        if(self.db.get_credentials(user_name_entry.get(),user_password_entry.get())):
            messagebox.showinfo(title="Inicio de Sesión perfecto",message="Usuario correcto")
            self.login_frame.pack_forget()
            self.principal()
        else:
            messagebox.showerror(title="Error al loguearse", message="Las credenciales no son correctas")




if __name__ == "__main__":
    app = Noldorin()