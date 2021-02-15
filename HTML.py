import webbrowser#pagia web
def descomponer(array):
    cuerpo1='''
        <table class="table"><thead><tr><th scope="col">
    '''
    cuerpo2='''</th> <tr></thead><tbody><tr><th scope="col">
    '''
    cuerpo3='''</th></tr></tbody></table>
    '''
    texto=''
    for LISTA in array:#LISTA1|LISTA2
        if LISTA!=' ':
            for SUBLISTA in LISTA:#ID:B:LISTAo;LISTA2 || ID:B:LISTAo;LISTA2
                listaOriginal=''
                listaModificada=''
                for n in SUBLISTA[2]:
                    listaOriginal=listaOriginal+','+str(n)
                for n in SUBLISTA[3]:
                    listaModificada=listaModificada+','+str(n)
                if SUBLISTA[1]=='O':#ORDENAR
                    texto=texto+cuerpo1+SUBLISTA[0]+cuerpo2+'ORDENADOS='+listaModificada+cuerpo3

                if SUBLISTA[1]=='B':#BUSCAR
                    if listaModificada!='':
                        texto=texto+cuerpo1+SUBLISTA[0]+cuerpo2+listaOriginal+'BUSQUEDA POSICIONES='+listaModificada+cuerpo3
                    else:
                        texto=texto+cuerpo1+SUBLISTA[0]+cuerpo2+listaOriginal+'BUSQUEDA POSICIONES=NO ENCONTRADO'+cuerpo3
    funcion(texto)

def funcion(texto):
    f = open('holamundo.html','w')
    principal = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="css/css.css">
        <link rel="stylesheet" href="boos/bootstrap.css">
        <title>Document</title>
        </head><body>
        """
    cuerpos=texto
    fin= """
        </body>
        <script src="boos/bootstrap.js"></script>
    </html>"""
    f.write(principal)#inicio
    f.write(cuerpos)#medio
    f.write(fin)#final
    f.close()#cerar
    webbrowser.open_new_tab('holamundo.html')#generar


'''
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">HOLA</th>
                <tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="col">esto es un texto</th>
                </tr>
            </tbody>
        </table>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">HELLO</th>
                <tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="col">esto es un otro texto</th>
                </tr>
            </tbody>
        </table>
            '''