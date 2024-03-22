import os



class Cargar():


	#ingresamos la ruta y el limite de tamaño a buscar
	def analizar_ruta(self, ruta, tamanno):	

		#vamos a la ruta
		os.chdir(ruta)	

		#tomamos todos los archivos y carpetas
		lista = os.listdir(".")	

		#lista donde iran los archivos que cumplieron la condicion de tamaño
		archivos = []


		#recorremos los archivos
		for archivo in lista:

			#preguntamos por la extencion del archivo
			if archivo.endswith(".png") or archivo.endswith(".jpg"):

				#preguntamos por el tamaño del archivo
				if os.path.getsize(archivo) >= int(tamanno):

					archivos.append(archivo)

		
		return archivos

