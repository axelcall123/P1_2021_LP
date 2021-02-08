import separador as separador
def analizar(cadena,contador):
    array_respuesta = {}#DIRECTORIO
    cadena=cadena.replace(' ','')
    array_id = cadena.split('=')#SEPARA CONVIERTE ARRAY 0|ID;1|RESTO
    array_respuesta[contador] = array_id[0].strip() + '=' + array_id[1].strip()#UNION STR
    print(array_id[0])
    if array_id[1]=='':#ERROR SI NO LO SEPARA =
        print('ERROR =')
    else:
        separador.separar(array_id[1])
    