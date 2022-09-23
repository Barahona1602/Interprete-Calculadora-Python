from ast import For, Str
import itertools
from tkinter import *
import webbrowser
import pandas as pd
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import scrolledtext as st
import numpy as np
from tkinter import messagebox as MessageBox
from enum import Enum
from lib2to3.pgen2 import token
import re
import ntpath
import os
from analizador import Analizador


global nuevoarchivo1

#Método para abrir archivo
def abrirArchivo():
        global cuadro
        cuadro = tk.Text(inicio, width=110, height=29, font=('Open Sans Light', 10), fg="#000000", bg="#FF8087")
        cuadro.place(x=250, y=210)  
        global archivo1   
        archivo1 = filedialog.askopenfilename(title="Abrir archivo", initialdir="C:/", filetypes=(("txt files",".txt"),("Todos los archivos",".*")))
        global nombrearchivo
        nombrearchivo=ntpath.basename(archivo1)
        nombrearchivo=nombrearchivo.replace(".txt","")
        nombrearchivo=nombrearchivo.replace(".html","")
        Datos = open(archivo1, "r", encoding='utf-8')
        for line in Datos:
            cuadro.insert(END,line)













#---------------------------------------------------
#---------------------------------------------------





#Método para guardar archivo
def guardar():
    nuevoarchivo1=open(nombrearchivo+".txt","w+",encoding='utf-8')
    nuevoarchivo1.writelines(cuadro.get("1.0","end-1c"))





#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------





#Método para guardar como 
def guardarcomo():
    
    guardarcomo = tk.Tk()
    guardarcomo.geometry("500x150")
    guardarcomo["bg"]='#222831'
    guardarcomo.title("Guardar como")
    fontStylelbl = tkFont.Font(family='Open Sans Light', size='14', weight='bold')
    lbl1=tk.Label(guardarcomo, text="Elija el nombre de su archivo", font=fontStylelbl, fg="#DDDDDD", bg="#222831").place(x=25, y=25)
    entry1=tk.Entry(guardarcomo, font=fontStylelbl, fg="#222831", bg="#DDDDDD", width="30")
    entry1.place(x=25, y=65)


    def botonguardar():
        global nombrearchivo
        nombrearchivo=entry1.get()
        nuevoarchivo1=open(nombrearchivo+".txt","w+",encoding='utf-8')
        nuevoarchivo1.writelines(cuadro.get("1.0","end-1c"))
        print(nombrearchivo)
        MessageBox.showinfo("Guardar como", "Archivo guardado correctamente")
        guardarcomo.destroy()
    bttn1 = tk.Button(guardarcomo, text="Guardar como", font=fontStylelbl, command=botonguardar, fg="#30475E", bg="#DDDDDD").place(x=325, y=60)





#---------------------------------------------------
#---------------------------------------------------




#Método para analizar 
def analizar():
    Analizador(archivoimp=archivo1).compile()
    Analizador.htmlanalizar()




#---------------------------------------------------
#---------------------------------------------------




#Método para mostrar errores
def errores():
   Analizador.htmlerrores() 




#---------------------------------------------------
#---------------------------------------------------


#Comando Salir
def salirPro():
    exit()





#---------------------------------------------------
#---------------------------------------------------


#Comando para mostrar manual de usuario
def manualusuario():
    manualuser = 'I9-202100101-E1.pdf'
    webbrowser.open_new(manualuser)





#---------------------------------------------------
#---------------------------------------------------



#Comando para mostrar manual técnico
def manualtecnico():
    print("Manual técnico")





#---------------------------------------------------
#---------------------------------------------------



#Comando para mostrar info
def info():
    print("info")





#---------------------------------------------------
#---------------------------------------------------



#Ventana 1 (Inicio)
inicio = tk.Tk()
inicio.title("Proyecto 1")
inicio["bg"]="#222831"
inicio.geometry("1160x705")


#labels y botones
lblincial = tk.Label(inicio, width=138, height=3, font=('Open Sans Light', 10), fg="#FF8087", bg="#FF8087").place(x=25, y=140)
lblincial = tk.Label(inicio, width=25, height=29, font=('Open Sans Light', 10), fg="#FF8087", bg="#FF8087").place(x=25, y=210)
fontStyle= tkFont.Font(family='Open Sans Light', size='30', weight='bold')
fontStylebttn = tkFont.Font(family='Open Sans Light', size='14', weight='bold')
lbl1 = tk.Label(inicio, width=46, height=2, text="Analizador Léxico", font=fontStyle, fg="#DDDDDD", bg="#30475E").place(x=25, y=25)
bttn1 = tk.Button(inicio, text="Abrir Archivo", width=13, height='2', font=fontStylebttn, command=abrirArchivo, fg="#30475E", bg="#DDDDDD").place(x=45, y=230)
bttngurdar = tk.Button(inicio, text="Guardar", width=13,height='2', font=fontStylebttn, command=guardar, fg="#30475E", bg="#DDDDDD").place(x=45, y=300)
bttn3 = tk.Button(inicio, text="Guardar como",width=13,height='2', font=fontStylebttn, command=guardarcomo, fg="#30475E", bg="#DDDDDD").place(x=45, y=370)
bttn4 = tk.Button(inicio, text="Analizar Archivo",width=13,height='2', font=fontStylebttn, command=analizar, fg="#30475E", bg="#DDDDDD").place(x=45, y=440)
bttn5 = tk.Button(inicio, text="Ver errores",width=13,height='2', font=fontStylebttn, command=errores, fg="#30475E", bg="#DDDDDD").place(x=45, y=510)
bttn6 = tk.Button(inicio, text="Salir", width=13,height='2', font=fontStylebttn, command=salirPro, fg="#30475E", bg="#DDDDDD").place(x=45, y=580)
bttn7 = tk.Button(inicio, text="Manual de usuario", width=15, font=fontStylebttn, command=manualusuario, fg="#30475E", bg="#DDDDDD").place(x=260, y=147)
bttn8 = tk.Button(inicio, text="Manual Técnico", width=15, font=fontStylebttn, command=manualtecnico, fg="#30475E", bg="#DDDDDD").place(x=500, y=147)
bttn9 = tk.Button(inicio, text="Temas de Ayuda", width=15, font=fontStylebttn, command=info, fg="#30475E", bg="#DDDDDD").place(x=750, y=147)

inicio.mainloop()