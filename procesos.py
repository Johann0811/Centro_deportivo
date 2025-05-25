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

        plt.figure(figsize=(10,8))
        plt.suptitle('Histogramas de Puntajes, dificultades y ponderados')
        plt.subplot(3,3,1)
        sns.histplot(individual["Puntaje_resistencia"], bins=10, color="#2727FF")
        plt.title("Resistencia")
        plt.subplot(3,3,2)
        sns.histplot(individual["Puntaje_fuerza"], bins=10, color="#FF2424")
        plt.title("Fuerza")
        plt.subplot(3,3,3)
        sns.histplot(individual["Puntaje_velocidad"], bins=10, color="#69FF23")
        plt.title("Velocidad")
        plt.subplot(3,3,4)
        sns.histplot(individual["dificultad_resistencia"], bins=10, color="#1717A1")
        plt.title("Dificultad de resistencia")
        plt.subplot(3,3,5)
        sns.histplot(individual["dificultad_fuerza"], bins=10, color="#B81919")
        plt.title("Dificultad de Fuerza")
        plt.subplot(3,3,6)
        sns.histplot(individual["dificultad_velocidad"], bins=10, color="#3F911A")
        plt.title("Dificultad de velocidad")
        plt.subplot(3,3,7)
        sns.histplot(individual["Puntaje_resistencia_final"], bins=10, color="#0C0C55")
        plt.title("Total resistencia")
        plt.subplot(3,3,8)
        sns.histplot(individual["Puntaje_fuerza_final"], bins=10, color="#4C0A0A")
        plt.title("Total fuerza")
        plt.subplot(3,3,9)
        sns.histplot(individual["Puntaje_velocidad_final"], bins=10, color="#224B0F")
        plt.title("Total velocidad")

        plt.tight_layout(rect=[0, 0, 1, 1])
        #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html
        plt.show()
        return df_individual


class DataAnalyzer():
    def __init__(self, df):
        self.df = df

class PuntajeAnalyzer(DataAnalyzer):
    def __init__(self, df):
        super().__init__(df)
        self.puntajes_cols = ["Puntaje_resistencia", "Puntaje_fuerza", "Puntaje_velocidad"]
        self.describe_cols = ["Puntaje_resistencia_final", "Puntaje_fuerza_final", "Puntaje_velocidad_final", "Puntaje_total"]

    def estadistica_grupal(self):
        plt.figure(figsize=(14,7))
        plt.subplot(1,2,1)
        correlation = self.df[self.puntajes_cols].corr()
        sns.heatmap(correlation, annot=True, cmap='seismic')
        plt.title('Matriz de Correlación')
        plt.subplot(1,2,2)
        Clasificados = self.df['Clasificacion'].value_counts()
        plt.title("Porcentaje de clasificados y no clasificados")
        plt.pie(Clasificados, colors = ["#008000", "#8B0000"])
        plt.legend(Clasificados, labels = Clasificados.index)
        plt.grid()
        plt.show()    

    def promedio(self):
        promediar = round(sum(self.df['Puntaje_total'])/len(self.df['Puntaje_total']))      
        return promediar
    
    def describe(self):
        resumen = self.df[self.describe_cols].describe() 
        return resumen
        