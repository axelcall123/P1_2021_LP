def aIz():
    return 'a-z'
def AIZ():
    return 'A-Z' 
def ceroInueve():
    return '0-9'

#TEXT=aIz()+' '+AIZ()+' '+ceroInueve()
#print(TEXT)
def automata(palabra):
    contador_palabra=0
    array_cadena=[]
    str_numeros=''
    str_resto=''
    str_ordenes=''
    str_numero_ordenar=''

    for n in range(len(palabra)):#SEPARAR EN ARRAY LAS PALABRAS
        array_cadena.append(palabra[n])

    for n in range(len(palabra)):#CONTAR LOS NUMEROS
        if ord(palabra[n])>47 and ord(palabra[n])<58 or palabra[n]==',':
            contador_palabra+=1
        else:
            n=len(palabra)+1
            break

    for n in range(len(palabra)):#SEPARA EN NUMEROS
        if n<contador_palabra:
            str_numeros=str_numeros+palabra[n]
        else:
            str_resto=str_resto+palabra[n]

    for n in range(len(str_resto)):#SEPARAR LOS COMANODS Y LOS NUMEROS
        if ord(str_resto[n])>64 and ord(str_resto[n])<91 or palabra[n]==',':
            str_ordenes=str_ordenes+str_resto[n]
        else:
            str_numero_ordenar=str_numero_ordenar+str_resto[n]

    print(str_numeros+' || '+str_ordenes+' || '+str_numero_ordenar)
txt='3,4,6,5,7,1ORDENAR8'
automata(txt)