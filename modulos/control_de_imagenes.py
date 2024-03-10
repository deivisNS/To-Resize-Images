from PIL import Image   #para el control de  imagenes
import os  #para interactuar con el sistema operativo





class Config_Imagenes():


	"""imagen_grande > imagen a reducir
	guardar > lugar donde se guardara la nueva imagen"""
	def __init__(self, imagen_grande, guardar):
		
		self.nombre, self.extencion = os.path.splitext(imagen_grande)	#extraemos el nombre y la extencion de la imagen
		
		self.imagen = Image.open(imagen_grande)

		self.guardar_en = guardar



	"""dimensiones > lista con el ancho y largo deseado o un entero que representara un porcentaje
	extencion_guardado > la extencion con la que se guardara la imagen"""
	def tamanno(self, dimensiones, extencion_guardado):

		try:

			#si es solo un entero
			if int(dimensiones):
				
				#tomamos el ancho y largo de la imagen
				width, height = self.imagen.size  
				
				#reducimos el ancho
				width = width * dimensiones // 100
				
				#reducimos el largo
				height = height * dimensiones // 100

				#creamos una nueva imagen pero con las reducciones hechas
				nueva_imagen = self.imagen.resize((width, height))
				
				#guardamos la imagen
				nueva_imagen.save(f"{self.guardar_en}/{self.nombre}.{extencion_guardado}")


		except:

			#si no es una lista
			if type(dimensiones) != list:
				
				return "No puede llevar Letras."


			else:
				
				#creamos la imagen con el ancho y largo de la lista	
				nueva_imagen = self.imagen.resize((dimensiones[0], dimensiones[1]))

				#guardamos la imagen
				nueva_imagen.save(f"{self.guardar_en}/{self.nombre}.{extencion_guardado}")



		
		