def funcion2(array):
    for LISTA in array:#LISTA1|LISTA2
        if LISTA!=' ':
            for SUBLISTA in LISTA:#ID:B:LISTAo;LISTA2 || ID:B:LISTAo;LISTA2
                if SUBLISTA[1]=='B':    
                    #print(SUBLISTA)
                    listaOriginal=''
                    listaPosciones=''
                    for n in SUBLISTA[2]:
                        listaOriginal=listaOriginal+','+str(n)
                    for n in SUBLISTA[3]:
                        listaPosciones=listaPosciones+','+str(n)
                    if listaPosciones!='':
                        print(SUBLISTA[0],':'+listaOriginal,'BUSQUEDA POSICIONES=',listaPosciones)
                    else:
                        print(SUBLISTA[0],':'+listaOriginal,'BUSQUEDA POSICIONES=NO ENCONTRADO')

                    