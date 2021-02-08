import analizador as analizador
from tkinter import filedialog
from tkinter import *
def load():
    #archivo = open(r'D:\AXEL\DOCUMENTOS\U\GITHUB\P1_2021_LP\TXT.txt','r')#LEE LA RUTA 
    #for linea in archivo.readlines():
    #        linea=linea+'='#ERROR SI NO TIENE =
    #        analizador.analizar(linea, contador)
    #        contador+=1
    contador=1
    root = Tk()
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P1_2021_LP",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    #contenido=archivo.read()
    for linea in archivo.readlines():#LEE LINEA POR LINEA
        linea=linea+'='#ERROR SI NO TIENE =
        analizador.analizar(linea, contador)
        contador+=1
    archivo.close()
