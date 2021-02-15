def funcion(array):
    for LISTA in array:#LISTA1|LISTA2
        if LISTA!=' ':
            for SUBLISTA in LISTA:#ID:B:LISTAo;LISTA2 || ID:B:LISTAo;LISTA2
                if SUBLISTA[1]=='O':    
                    #print(SUBLISTA)
                    listaNum=''
                    for listOrde in SUBLISTA[3]:
                        listaNum=listaNum+','+str(listOrde)
                         #ID+DATOS: ORDENADOS=+1,2,3
                    print(SUBLISTA[0],'DATOS: ORDENADOS=',listaNum)
