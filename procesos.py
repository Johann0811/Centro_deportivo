import random as rd
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import csv
import matplotlib.pyplot as plt
import seaborn as sns 
archivo = "deportes.csv"
df = None

registro = {"Nombre": None, "Puntaje_total": None, "Clasificacion": None,
            "Puntaje_resistencia": None, "Puntaje_fuerza": None, "Puntaje_velocidad": None,
            "dificultad_resistencia": None, "dificultad_fuerza": None, "dificultad_velocidad": None,
            "Puntaje_resistencia_final": None, "Puntaje_fuerza_final": None, "Puntaje_velocidad_final": None}

class rendimiento():
    def registro(self):
        registro["Nombre"] = simpledialog.askstring("Registro","Ingrese el nombre del participantes")
        while True:   
            puntaje1 = simpledialog.askinteger("Puntajes. Recuerde que se califica de 0-100", "Cuanto puntaje obtuvó en la prueba de resistencia?: ")
            if puntaje1 < 0 or puntaje1 > 100:
                messagebox.showerror("ERROR", "El puntaje solo puede ser de 0-100")
                continue 
            else:
                dificultad1 = round(rd.uniform(1.0,1.3),2)
                registro["Puntaje_resistencia"] = puntaje1
                registro["dificultad_resistencia"] = dificultad1
                calculo_puntaje1 = round(puntaje1 * dificultad1)
                registro["Puntaje_resistencia_final"] = calculo_puntaje1 
                break 
        
        while True:   
            puntaje2 = simpledialog.askinteger("Puntajes. Recuerde que se califica de 0-100", "Cuanto puntaje obtuvó en la prueba de fuerza?: ")
            if puntaje2 < 0 or puntaje2 > 100:
                messagebox.showerror("ERROR", "El puntaje solo puede ser de 0-100")
                continue 
            else:                        
                dificultad2 = round(rd.uniform(1.0,1.3),2)
                registro["Puntaje_fuerza"] = puntaje2
                registro["dificultad_fuerza"] = dificultad2
                calculo_puntaje2 = round(puntaje2 * dificultad2)
                registro["Puntaje_fuerza_final"] = calculo_puntaje2
                break
                
        while True:   
            puntaje3 = simpledialog.askinteger("Puntajes. Recuerde que se califica de 0-100", "Cuanto puntaje obtuvó en la prueba de velocidad?: ")
            if puntaje3 < 0 or puntaje3 > 100:
                messagebox.showerror("ERROR", "El puntaje solo puede ser de 0-100")
                continue 
            else:                        
                dificultad3 = round(rd.uniform(1.0,1.3),2)
                registro["Puntaje_velocidad"] = puntaje3
                registro["dificultad_velocidad"] = dificultad3
                calculo_puntaje3 = round(puntaje3 * dificultad3)
                registro["Puntaje_velocidad_final"] = calculo_puntaje3 
                break
            
    
        puntaje_final = round(sum([calculo_puntaje1,calculo_puntaje2,calculo_puntaje3])/sum([dificultad1,dificultad2,dificultad3]))
        if puntaje_final >= 70:
            registro["Clasificacion"] = "Clasifico"
        else:
            registro["Clasificacion"] = "No clasifico"
        
        registro["Puntaje_total"] = puntaje_final
        archivo_existe = os.path.isfile('deportes.csv')
        with open(archivo, 'a', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=registro.keys())
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(registro)

    def reporte_general(self): 
         archivo_existe = os.path.isfile('deportes.csv')
         if archivo_existe:
            df = pd.read_csv(archivo)
            reporte = df[["Nombre", "Puntaje_total", "Clasificacion"]]
            return reporte

    def reporte_individual(self):
        Nombre_buscar = simpledialog.askstring("Busqueda por nombre", "De cual participante desea ver el reporte?: ")
        df = pd.read_csv(archivo)
        busqueda = df[df["Nombre"] == Nombre_buscar].index[0]
        individual = pd.DataFrame([df.loc[busqueda].to_dict()])
        df_individual = (individual[["Nombre", "Puntaje_total", "Clasificacion"]])
        return df_individual
        