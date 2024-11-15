import tkinter
from tkinter import *

class Navbar:

    def __init__(self,ventana):
        self.ventana = ventana
        barra_menus = Menu()

        menu_archivo = Menu(barra_menus,tearoff=False)
        menu_archivo.add_command(
            label="Nuevo",
            command=self.archivo_nuevo_presionado()
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir",command=ventana.destroy)

        barra_menus.add_cascade(menu=menu_archivo,label="Archivo")

        self.ventana.config(menu=barra_menus)

    def archivo_nuevo_presionado(self):
        print("Has presionado")