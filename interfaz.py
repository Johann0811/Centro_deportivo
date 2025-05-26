import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import os
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from procesos import archivo
from procesos import rendimiento
from procesos import DataAnalyzer
from procesos import PuntajeAnalyzer

def registro():
     Rendimiento = rendimiento()
     Rendimiento.registro()
     archivo_existe = os.path.isfile('deportes.csv')
     if not archivo_existe:
         messagebox.showwarning("Error", "No existen datos")
     else:
        df = pd.read_csv(archivo)

def reporte():
    archivo_existe = os.path.isfile('deportes.csv')
    if not archivo_existe:
        messagebox.showwarning("Error", "No existen datos")
    else:
        df = pd.read_csv(archivo)
        Rendimiento = rendimiento()
        reporte = Rendimiento.reporte_general()
        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, reporte.to_string(index=True))
        pruebas = PuntajeAnalyzer(df)
        promedio_grupo = pruebas.promedio()
        descripcion = round(pruebas.describe())
        text_area2.delete("1.0",tk.END)
        text_area2.insert(tk.END, "Promedio del grupo\n")
        text_area2.insert(tk.END,f"{promedio_grupo}\n\n")
        text_area2.insert(tk.END, "Resumen estadistico\n")
        text_area2.insert(tk.END,descripcion)
        pruebas.estadistica_grupal()

def reporte_individual():
    archivo_existe = os.path.isfile('deportes.csv')
    if not archivo_existe:
        messagebox.showwarning("Error", "No existen datos")
    else:
        df = pd.read_csv(archivo)
        Rendimiento = rendimiento() 
        text_area3.delete("1.0",tk.END)
        reporte_solo = Rendimiento.reporte_individual()
        text_area3.insert(tk.END,reporte_solo)

def terminar():
    ventana.destroy()
    #https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/  

ventana = tk.Tk()
ventana.title("Reporte de estadisticas del centro deportivo")
ventana.geometry()

boton_registro = tk.Button(ventana, text="Registrar participante", command= registro)
boton_registro.grid(row=0, column=0)

boton_reporte_general = tk.Button(ventana, text="Mostrar reporte general", command=reporte)
boton_reporte_general.grid(row=0, column=1)

boton_reporte_individual = tk.Button(ventana, text="Buscar participante", command= reporte_individual)
boton_reporte_individual.grid(row=0, column=2)

boton_salir = tk.Button(ventana, text="Salir", command=terminar)
boton_salir.grid(row=1, column=0)

text_area = ScrolledText(ventana, width= 70, height= 30)
text_area.grid(row=1, column=1)
text_area2 = ScrolledText(ventana, width= 100, height= 30)
text_area2.grid(row=1, column=2)
text_area3 = ScrolledText(ventana, width=70, height= 10)
text_area3.grid(row=2, column=1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)


ventana.mainloop()