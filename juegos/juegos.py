import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg
import uuid


#Funcion que se encarga de crear un objeto en formato json, y lo escribe en el arcivo jugador.txt
def juego(nombre, juegos):
	# Chequeo para no agregar un objeto nulo
	if(nombre != None):
		diccionario = {
			## Agregue un id para que cada jugada quede grabada y se pueda acceder a ella.
			str(uuid.uuid1()): {
				"nombre": nombre,
				"juego": juegos,
			}
		}
		with open('jugador.txt', 'a') as archivo:
			json.dump(diccionario, archivo,indent=2)



def main(args):
	# Instanciacion  de variables
	sigo_jugando = True
	while sigo_jugando:
		#Creacion de la UI
		layout = [[sg.Text("Ingrese su nombre")],
		[sg.InputText(key="name")],
		[sg.Text("Elegí con qué juego querés jugar:")],
		[sg.Text("1.- Ahorcado")],
		[sg.Text("2.- Ta-TE-TI")],
		[sg.Text("3.- Otello")],
		[sg.Text("4.- Salir")],
		[sg.InputText(key="selection")],
		[sg.Submit()]
		]
		event,values = window = sg.Window("Juegos",layout).read(close=True)
		#Sentencia que se usa para cerrar la ventana cuando se hace click en la "X"
		if event in (None, 'Quit'):
			break

		#Traer los valores ingresados
		nombre = values["name"]
		opcion = values["selection"]
		if(opcion != "4"):
			juego(nombre,opcion)
		if opcion == '1':
			hangman.main()
		elif opcion == '2':
			tictactoeModificado.main()
		elif opcion == '3':
			reversegam.main()
		elif opcion == '4':
			sigo_jugando = False
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
