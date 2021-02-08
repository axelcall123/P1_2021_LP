import principal as principal
import os

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
		principal.load()
	elif opcionMenu=='6':
		break
	else:
		print ('')
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')  