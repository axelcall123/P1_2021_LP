import Separador as Separador
def sepId(cadena,contador):
    array_respuesta = {}#DIRECTORIO
    
    cadena=cadena.replace(' ','')
    array_id = cadena.split('=')#SEPARA CONVIERTE ARRAY 0|ID;1|RESTO
    array_respuesta[contador] = array_id[0].strip() + '=' + array_id[1].strip()#UNION STR
    #print(array_id[0])
    if array_id[1]=='':#ERROR SI NO LO SEPARA =
        print('ERROR =')
        return ' '
    else:
        array_modificar=[]
        array_entrada=[]

        array_modificar.append(array_id[0])#AGREGA EL ID
        array_id[1]=array_id[1].replace('=','')#QUITA EL IGUAL DE LA ULTIMA PARTE PARA EL ERROR lista = 1
        array_id[1]=array_id[1].replace('\n','')#QUITA EL SALTO DE LINEA
        array_entrada=Separador.separar(array_id[1],contador)
        #print(array_entrada, 'EL ENVIO ES ESTE --------')
        for array in array_entrada:#AGREAGA str_numeros,str_ordenes,str_numero_ordenar
            array_modificar.append(array)
        #print(array_modificar, 'ARRAY ANALIZAR --------')
        #ID|array_numeros|array_comandos|NUMERO
        ID=analizar_id(array_modificar[0],contador)
        array_numeros=separar_numeros(array_modificar[1],contador)
        #tamaño=int(len(array_modificar[0]))+int(len(array_modificar[1]))
        array_comandos=analizar_ordenes(array_modificar[2],contador)
        NUMERO=numero_inspeccion(array_modificar[3],array_modificar[2],contador)
        #print(ID,array_numeros,array_comandos,NUMERO,'--')
        if ID!=' ' and array_numeros!=' ' and array_comandos!=' ' and NUMERO!=' ':
            array_salida=[]
            array_funciones_comandos=[]
            array_funciones_comandos2=[]#EVITA ESTO: ID,COMANDO,LISTA,LISTA1 , ID,COMANDO,LISTA2,LISTA3 
            contador2=1
            array_posiciones=[]
            
            for n in array_comandos:#CICLO PARA LOS COMANODS BUSCAR | ORDENAR
                if n=='BUSCAR':#ARRAY_NUMEROS | NUMERO BUSCAR
                    for NUM in array_numeros:#BUSCA TODAS LAS POSICIONES
                        if NUM==NUMERO:
                            array_posiciones.append(contador2)
                        contador2+=1#CUENTA LAS POSICIONES
                    array_funciones_comandos.append(ID)
                    array_funciones_comandos.append('B')
                    array_funciones_comandos.append(array_numeros)
                    array_funciones_comandos.append(array_posiciones)
                    array_salida.append(array_funciones_comandos)
                    #print('quieres buscar')
                if n=='ORDENAR':#ARRAY
                    array_ordenado=array_numeros
                    array_ordenado=[int(x) for x in array_ordenado]#CONVERTIR EN INTS
                    array_ordenado.sort()#ORDENARLO
                    #array_ordenado.sort(reverse=Tru)#ORDENARLO AL REVES
                    array_funciones_comandos2.append(ID)
                    array_funciones_comandos2.append('O')
                    array_funciones_comandos2.append(array_numeros)
                    array_funciones_comandos2.append(array_ordenado)
                    array_salida.append(array_funciones_comandos2)
                    #print('quieres ordenar')
            #print('COM,SI,FUNC',array_salida)
            return array_salida
        else:
            return ' '
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
def numero_inspeccion(int,comandoO,contador):
    if comandoO=='ORDENAR':#ORDENAR ''
        if int=='':
            return '0'#ENVIE ALGO DIFERENTE DE ' ' 
        else:
            return int#EL NUMERO
    else:
        if int=='':
            return ' ' 
        else:
            return int

