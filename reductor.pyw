from tkinter import *	#para hacer gui
from tkinter import ttk #para hacer gui
from tkinter import filedialog as fd  #para crear cuadros de dialogos
from modulos.control_de_imagenes import *	#modulo para reducir las imagenes
import os
import threading	#para crear hilos



root = Tk()



from modulos.variables import *



#buscamos la carpeta a buscar las imagenes
def buscar_carpeta():
	
	ruta.set("")

	carpeta = fd.askdirectory(title = "Buscar Carpeta...")

	if carpeta != "":

		ruta.set(carpeta)



#extraemos las imagenes
def comenzar_reduccion():
	global Archivos, resultado
	
	#lista con las imagenes que cumplan las condiciones de peso
	resultado = Archivos.analizar_ruta(ruta.get(), f"{kb.get()}000000")
	
	#creamos la carpeta donde se guardaran las imagenes reducidas	
	os.mkdir(f"./reduccion a partir de {kb.get()} MB")

	notificacion("Reduciendo...", "")

	#hilo donde se reducen las imagenes
	proceso = threading.Thread(
		target = proceso_reduccion, 
		args = (resultado, f"./reduccion a partir de {kb.get()} MB")
		)

	proceso.start()



#proceso donde se reducen las imagenes
def proceso_reduccion(imagenes, ruta_guardado):
	
	#recorremos las imagenes pesadas
	for imagen in imagenes:
		
		"""clase que se encargara de la reduccion de imagenes y se le pasara
		datos de la imagen y la ruta donde se guardara"""
		reduccion = Config_Imagenes(f"{imagen}", ruta_guardado)

		#metodo encargada de la reduccion de imagenes
		reduccion.tamanno(100 - int(porcentaje.get()), formato.get())


	notificacion("¡¡Listo!!", "El Proceso se ha Realizado con Exito.")



#pruntamos si hay ruta hacia alguna carpeta
def confirmar_reduccion():
	
	if ruta.get() != "":

		notificacion("¿Comenzar Reduccion?", f"Se buscaran imagenes de {kb.get()} MB en adelante.\nSe reduciran un {int(porcentaje.get())} %.\nY se guardaran con la extencion .{formato.get().upper()}.")


	else:

		notificacion("Sin Ruta", "No has Ingresado una Ruta a Analizar.")



#ventana de alerta y que nos mustra informaciondel proceso que se lleva a cabo
def notificacion(alerta, mensaje):
	

	if alerta == "¿Comenzar Reduccion?":
		cols = 2

	else:
		cols = 1


	if alerta == "¡¡Listo!!":

		top_alerta = Toplevel()

		top_alerta.destroy()


	top_alerta = Toplevel()	
	top_alerta.resizable(0,0)
	top_alerta.overrideredirect(1)
	top_alerta.geometry(f"+{200 + posicion_x}+{170 + posicion_y}")


	marco = Frame(top_alerta, bd = 4, relief = "solid", bg = "white", pady = 10, padx = 10)
	marco.pack()


	Label(marco, text = alerta.upper(), bg = "white", fg = "red", 
		font = ("arial black", 26)).grid(row = 0, column = 0, columnspan = cols)


	if mensaje != "":
		Label(marco, text = mensaje, bg = "white", fg = "black", 
			font = ("verdana", 16)).grid(row = 1, column = 0,  pady = 20, columnspan = cols)


	if alerta == "¿Comenzar Reduccion?":	
	
		Button(marco, text = "Cerrar", takefocus = False, bd = 2, relief = "raised", fg = "white", bg = "black",
			command = top_alerta.destroy, font = ("verdana", 20)).grid(row = 2, column = 1, pady = 10)

		Button(marco, text = "Comenzar", takefocus = False, bd = 2, relief = "raised", fg = "white", 
			bg = "black", command = lambda:[comenzar_reduccion(), top_alerta.destroy()],
			font = ("verdana", 20)).grid(row = 2, column = 0)


	elif alerta == "Reduciendo...":
		pass


	else:

		Button(marco, text = "Cerrar", takefocus = False, bd = 2, relief = "raised", fg = "white", bg = "black",
			command = top_alerta.destroy, font = ("verdana", 20)).grid(row = 2, column = 0, pady = 10)
	


#capturamos el ancho y largo de la pantalla 
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

#posiciones que usaremos para centrar la ventana
posicion_x, posicion_y = X_Y.construir_posicion(int(width), int(height), monitor_width, monitor_height)



#configuracion de la ventana
root.title("Reductor de Imagenes")
root.geometry(f"{width}x{height}+{posicion_x}+{posicion_y}")
root.resizable(0,0)
root.iconbitmap("imagen.ico")
root.config(bg = "#662d8c",)


#frames donde van colocados los botones y letras
frame_1 = Frame(root, bg = "#662d8c", padx = 10, pady = 10)
frame_1.grid(row = 0, column = 0, columnspan = 3, pady = 20)

frame_2 = Frame(root, bg = "#662d8c", padx = 10, pady = 10,)
frame_2.grid(row = 1, column = 0, padx = 25, pady = 10)

frame_3 = Frame(root, bg = "#662d8c", padx = 10, pady = 10,)
frame_3.grid(row = 1, column = 1, padx = 25, pady = 10)

frame_4 = Frame(root, bg = "#662d8c", padx = 10, pady = 10,)
frame_4.grid(row = 1, column = 2, padx = 25, pady = 10)


#widgets
Label(frame_1, text = "Reduce tus Imagenes :D", fg = "white", bg = "#662d8c", 
	font = ("herdrock", 37)).grid(row = 0, column = 0, columnspan = 2)

Label(frame_1, text = "Busca la Carpeta con Imagenes:", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 1, column = 0, columnspan = 2)

Entry(frame_1, textvariable = ruta, bd = 2, relief = "solid", bg = "#596164", fg = "black", 
	width = 29, state = DISABLED, font = ("arial black", 14),).grid(row = 2, column = 0, 
	ipady = 3, padx = 5)

Button(frame_1, text = "Buscar", bg = "white", font = ("arial black", 12), pady = 5, 
	padx = 5, command = buscar_carpeta).grid(row = 2, column = 1)


#widgets
Label(frame_2, text = "Tamaño a Buscar:", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 0, column = 0)

Label(frame_2, text = "Mb", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 1, column = 1,)

Spinbox(frame_2, from_ = 1, to = 20, increment = 1, justify = "center", bg = "#596164", fg = "black",
	width = 10, font = ("arial black", 14), textvariable = kb, state = "readonly", bd = 2, 
	relief = "solid").grid(row = 1, column = 0)


#widgets
Label(frame_3, text = "Elige la Extencion:", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 0, column = 0)

estilo_principal = ttk.Style()

estilo_principal.theme_use("clam")

combobox_style = ttk.Style()

combobox_style.configure("style.TCombobox", fieldbackground = "#596164", background = "#596164", 
	foreground = "black", border_width = 2, relief = "solid")

ttk.Combobox(frame_3, values = extenciones, style = "style.TCombobox", textvariable = formato, 
	state = "readonly", justify = "center", width = 10,
	font = ("arial black", 14),).grid(row = 1, column = 0)


#widgets
Label(frame_4, text = "porcentaje de Reduccion:", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 0, column = 0)

Label(frame_4, text = "%", bg = "#662d8c", fg = "white",
	font = ("herdrock", 27)).grid(row = 1, column = 1,)

Spinbox(frame_4, values = porcentajes, increment = 1, justify = "center", bg = "#596164", fg = "black",
	width = 10, font = ("arial black", 14), textvariable = porcentaje, state = "readonly", bd = 2, 
	relief = "solid").grid(row = 1, column = 0)


Button(root, text = "Comenzar", bg = "white", fg = "black", pady = 5, padx = 5, 
	font = ("arial black", 18), command = confirmar_reduccion).grid(row = 2, column = 0, 
	columnspan = 3, pady = 40)


root.mainloop()