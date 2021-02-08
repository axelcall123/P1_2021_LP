#import tkinter
#ventana=tkinter.Tk()
#boton1=tkinter.Button(ventana, text="boton1", width=10, height=5)
#boton1.grid(row=0,column=0)
#ventana.mainloop()
from tkinter import filedialog
from tkinter import *

root = Tk()
root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P1_2021_LP",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
archi1=open(root, 'r', encoding="utf-8")
contenido=archi1.read()
print(contenido)
archi1.close()