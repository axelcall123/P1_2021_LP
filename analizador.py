import Separador as Separador
def sepId(cadena,contador):
    array_respuesta = {}#DIRECTORIO
    array_modificar=[]
    array_entrada=[]
    cadena=cadena.replace(' ','')
    array_id = cadena.split('=')#SEPARA CONVIERTE ARRAY 0|ID;1|RESTO
    array_respuesta[contador] = array_id[0].strip() + '=' + array_id[1].strip()#UNION STR
    #print(array_id[0])
    if array_id[1]=='':#ERROR SI NO LO SEPARA =
        print('ERROR =')
    else:
        array_modificar.append(array_id[0])#AGREGA EL ID
        array_id[1]=array_id[1].replace('=','')#QUITA EL IGUAL DE LA ULTIMA PARTE PARA EL ERROR lista = 1
        array_id[1]=array_id[1].replace('\n','')#QUITA EL SALTO DE LINEA
        array_entrada=Separador.separar(array_id[1],contador)
        #print(array_entrada, 'EL ENVIO ES ESTE --------')
        for array in array_entrada:#AGREAGA str_numeros,str_ordenes,str_numero_ordenar
            array_modificar.append(array)
        #print(array_modificar, 'ARRAY ANALIZAR --------')

        ID=analizar_id(array_modificar[0],contador)
        NUMEROS=separar_numeros(array_modificar[1],contador)
        #tamaño=int(len(array_modificar[0]))+int(len(array_modificar[1]))
        COMANDOS=analizar_ordenes(array_modificar[2],contador)
        NUMERO=array_modificar[3]
        #print(ID,NUMEROS,COMANDOS,NUMERO)
        if ID!=' ' and NUMEROS!=' ' and COMANDOS!=' ' and NUMERO!=' ':
            print('')
            #print('COMANDOS SI ESTAN BUENOS')
        #return array_salida#[array_id,str_numeros,str_ordenes,str_numero_ordenar]


def analizar_id(palabra,contador):
    columna=0
    union=''
    for n in range(len(palabra)):
        if (ord(palabra[n].upper())>64 and ord(palabra[n].upper())<91) or (ord(palabra[n])>47 and ord(palabra[n])<58):# A-Z 0-9
            union=union+palabra[n]
            columna+=1
        else:
            print('ERROR EN EL ID',palabra[n],'COLUMNA:',columna,'FILA:',contador)
            return ' '
    #print('PALABRA:',union)
    return union
        
def separar_numeros(arrayNumeros,contador):
    array_Numeros=arrayNumeros.split(',')
    #print('ARRAY NUMEROS', array_Numeros)
    return array_Numeros

def analizar_ordenes(arrayComandos,contador):
    columna=0
    array_Comandos=arrayComandos.split(',')
    for n in range(len(array_Comandos)):
        if array_Comandos[n]=='ORDENAR' or array_Comandos[n]=='BUSCAR':
            columna+=1
            if n==(len(array_Comandos)-1):
                #print('ARRAY ORDENES', array_Comandos)
                return array_Comandos
        else:
            print('ERROR EN LAS ORDENES',array_Comandos[n],'COLUMNA:',columna,'FILA:',contador)
            return ' '
