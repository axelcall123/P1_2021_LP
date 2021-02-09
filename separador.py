def separar(palabra,contador):
    columna=0
    contador_palabra=0
    array_cadena=[]
    str_numeros=''
    str_resto=''
    str_ordenes=''
    str_numero_ordenar=''
    array_salida=[]
    for n in range(len(palabra)):#SEPARAR EN ARRAY LAS PALABRAS
        array_cadena.append(palabra[n])
    #CONTAR LOS NUMEROS
    for n in range(len(palabra)):
        if (ord(palabra[n])>47 and ord(palabra[n])<58 or palabra[n]==',') or palabra[n]=='.':# 0-9 .
            contador_palabra+=1
            columna=contador_palabra
        elif palabra[n]=='O' or palabra[n]=='B':# A|B
            n=len(palabra)+1
            break
        else:
            print('ERROR EN LOS NUMEROS EN EL CADENA', palabra[n],'COLUMNA:',columna,'FILA:',contador)
            array_salida.append(' ')
            array_salida.append(' ')
            array_salida.append(' ')
            #print('ARRAY ERROR', array_salida)
            return array_salida

    #SEPARA EN NUMEROS
    for n in range(len(palabra)):
        if n<contador_palabra:
            str_numeros=str_numeros+palabra[n]
        else:
            str_resto=str_resto+palabra[n]
    #SEPARAR LOS COMANODS Y LOS NUMEROS
    #print(str_resto+'@',':RESTO')#VEO 1,2,3 BUSCAR, ORDENAR 123
    for n in range(len(str_resto)):
        if (ord(str_resto[n])>64 and ord(str_resto[n])<91) or str_resto[n]==',':#A-B
            str_ordenes=str_ordenes+str_resto[n]
            columna+=1
        elif (ord(str_resto[n])>47 and ord(str_resto[n])<58) or str_resto[n]=='.':# 0-9 .
            str_numero_ordenar=str_numero_ordenar+str_resto[n]
            columna+=1
        else:
            print('ERROR EN EL COMANDO O NUMERO', str_resto[n],'COLUMNA:',columna,'FILA:',contador)
            array_salida.append(' ')
            array_salida.append(' ')
            array_salida.append(' ')
            #print('ARRAY ERROR', array_salida)
            return array_salida

    array_salida.append(str_numeros)
    array_salida.append(str_ordenes)
    array_salida.append(str_numero_ordenar)
    #print(str_numeros+' || '+str_ordenes+' || '+str_numero_ordenar)
    return array_salida#[str_numeros,str_ordenes,str_numero_ordenar]
    