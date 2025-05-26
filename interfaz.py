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

ventana = tk.Tk()
ventana.title("Reporte de estadisticas del centro deportivo")
ventana.geometry()

boton_registro = tk.Button(ventana, text="Registrar participante", command= registro)
boton_registro.grid(row=0, column=0)

boton_reporte_general = tk.Button(ventana)
boton_reporte_general.grid(row=0, column=1)

boton_reporte_individual = tk.Button(ventana)
boton_reporte_individual.grid(row=0, column=2)

boton_salir = tk.Button(ventana)
boton_salir.grid(row=1, column=0)

text_area = ScrolledText(ventana, width= 70, height= 30)
text_area.grid(row=1, column=1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)


ventana.mainloop()