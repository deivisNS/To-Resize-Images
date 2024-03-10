from modulos.posicionar_ventana import *
from modulos.cargar_archivos import *
from tkinter import StringVar



#objetos de posicionar_ventana y otro de cargar_archivos
X_Y = Posicionar()
Archivos = Cargar()

#dimensiones de la ventana
width = 900
height = 460

#extenciones a elegir y porcentaje de reducciones que se aplicaran en el programa
extenciones = ["png", "jpeg", "webp"]
porcentajes = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]

#variables tkinter
ruta = StringVar()
kb = StringVar()
formato = StringVar()
formato.set(extenciones[0])
porcentaje = StringVar()
porcentaje.set(porcentajes[0])


