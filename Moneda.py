import tkinter as tk
from tkinter import *

class moneda(tk.Frame):
    def __init__(self,diccionario):
        Dolar=False
        Compra=False
        Venta=False
        moneda=diccionario['nombre']
        moneda=moneda.split()
        for x in range(0,len(moneda)):
            if (moneda[x]=="Dolar"):
                Dolar=True
        if (diccionario['compra']!= "No Cotiza"):
            Compra=True
        if (diccionario['venta']!= "0"):
            Venta=True
        super().__init__()
        if(Venta==True and Compra==True and Dolar==True):
            label_a = tk.Label(self, text=diccionario['nombre'])
            label_b = tk.Label(self, text=diccionario['venta'])
            label_c = tk.Label(self, text=diccionario['compra'])
            label_a.grid(row=0, column=0)
            long=140-(len(diccionario['nombre'])-6)*6
            label_b.grid(row=0, column=4,padx=(long))
            long2=((len(diccionario['nombre']))-5)*6
            print (long2)
            label_c.grid(row=0, column=5,padx=long2)

            
        