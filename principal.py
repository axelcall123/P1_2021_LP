import analizador as analizador
from tkinter import filedialog
from tkinter import *
def load():
    array_salida=[]
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
        #array_salida.append(analizador.analizarId(linea, contador))
        array_salida.append(analizador.sepId(linea, contador))
        contador+=1
    return array_salida  
    #print(array_salida,'ARRAY EN EL PRINCIPAL.PY')
    #return array_salida
    '''
    [
        [array_id,str_numeros,str_ordenes,str_numero_ordenar],
        [array_id,str_numeros,str_ordenes,str_numero_ordenar]
    ]
    '''
    archivo.close()
