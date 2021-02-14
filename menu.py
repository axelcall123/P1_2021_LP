import principal as principal
import os
array_general=[]
str_id=''
array_numeros=[]
array_comandos=[]
int_numero=0# ID, [#,##,###],[COMANDO1,COMANDO2], int

def menu():
	
	print ("""
Selecciona una opción
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
	elif opcionMenu=='6':
		break
	elif opcionMenu=='7':
		print('VAMOS A VER EL TEXTO',array_test)
	else:
		print ('')
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')  