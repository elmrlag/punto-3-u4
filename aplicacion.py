import tkinter as tk
from tkinter import *
import tkinter as ttk
from clasificar import VentanaClasificar
from Moneda import moneda
from urllib import request
from datetime import date
from datetime import datetime
import os
import sys

class Aplicacion(tk.Tk):
    __fecha=None
    __Hora=None
    def __init__(self):
        lista=self.cargarlista()
        super().__init__()
        self.geometry('420x170')
        self.resizable(0,1)
        self.clasificar = VentanaClasificar()
        self.clasificar.grid(row=0,column=0,sticky=(N,W,E,S))
        unitem=moneda(lista[0]['casa'])
        for x in range(0,len(lista)):
            self.unitem=moneda(lista[x]['casa'])
            self.unitem.grid(row=x+1,column=0,sticky=(W))
        ttk.Button(self, text="Actualizar", command=self.actualizar,bg= '#A6CE68').grid(column=0, row=len(lista), sticky=W)
        
        self.label_a = ttk.Label(self, text=f"Actualizado {self.__fecha} a las {self.__Hora}")
        self.label_a.grid(column=0, row=len(lista))
        print(self.__fecha)

    def actualizar(self):
        self.destroy()
        self.__init__()
    def cargarlista(self):
        url='https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        response= request.urlopen(url)
        lista = response.read().decode('utf-8')
        lista=eval(lista)
        self.__fecha=date.today()
        self.__Hora=datetime.now().time()
        return(lista)
