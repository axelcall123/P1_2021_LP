import analizador as analizador
archivo = open(r'D:\AXEL\DOCUMENTOS\U\GITHUB\P1_2021_LP\TXT.txt','r')
contador=1

for linea in archivo.readlines():
        analizador.analizar(linea, contador)
        contador+=1

archivo.close()

#import os.path
#my_path = os.path.abspath(os.path.dirname(__file__))
#path_1 = os.path.join(my_path, "..\TXT.txt")
