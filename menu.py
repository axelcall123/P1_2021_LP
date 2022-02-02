import principal as principal
import desLisBus as desLisBus
import desLisOrd as desLisOrd
import HTML as HTML
import os
array_general=[]
str_id=''
array_test=[]
array_numeros=[]
array_comandos=[]
int_numero=0# ID, [#,##,###],[COMANDO1,COMANDO2], int

def menu():
	
	print ("""
Selecciona una op1ción
t1 - CARGAR ARCHIVO DE ENTRADA
t2 - DESPLEGAR LISTAS ORDENADAS
t3 - DESPLEGAR BUSQUEDAS
t4 - DESPLEGAR TODAS
t5 - DESPLEGAR TODOS LOS ARCHIVOS
t6 - SALIR
	""")
while True:
	menu()
	opcionMenu = input('INSERTE UNA OPCION >>')
	if opcionMenu=='1':
		array_test=principal.load()
	elif opcionMenu=='2':
		if array_test!='':
			desLisOrd.funcion(array_test)#TRUE
	elif opcionMenu=='3':
		if array_test!='':
			desLisBus.funcion2(array_test)#TRUE
	elif opcionMenu=='4':
		if array_test!='':
			desLisOrd.funcion(array_test)#TRUE
			desLisBus.funcion2(array_test)#TRUE
	elif opcionMenu=='5':
		if array_test!='':
			HTML.descomponer(array_test)
	elif opcionMenu=='6':
		break
	elif opcionMenu=='7':
		print('VAMOS A VER EL TEXTO',array_test)
	else:
		print ('')
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')  