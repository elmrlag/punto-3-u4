import tkinter as ttk
from tkinter import *
class VentanaClasificar(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.title='Pack Geometry'
        self.label_a = ttk.Label(self, text="Moneda", bg='#A6CE68')
        self.label_b = ttk.Label(self, text="Compra", bg='#A6CE68')
        self.label_c = ttk.Label(self, text="Venta", bg='#A6CE68')
        self.label_a.grid(column=1, row=0, sticky=(W))
        self.label_b.grid(column=2, row=0, sticky=(E),ipadx=120)
        self.label_c.grid(column=3, row=0, sticky=(W),ipadx=30)


