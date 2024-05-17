from PIL import Image   #para el control de  imagenes
import os  #para interactuar con el sistema operativo



"""dimensiones > lista con el ancho y largo deseado o un entero que representara un porcentaje
extencion_guardado > la extencion con la que se guardara la imagen"""
def tamanno(imagen_grande, dimensiones, extencion_guardado, guardar_en):

	nombre, extencion = os.path.splitext(imagen_grande)

	try:

		with Image.open(imagen_grande) as imagen:

			#si es solo un entero
			if int(dimensiones):

				#tomamos el ancho y largo de la imagen
				width, height = imagen.size
	
				#reducimos el ancho
				width = width * dimensiones // 100

				#reducimos el largo
				height = height * dimensiones // 100

				#creamos una nueva imagen pero con las reducciones hechas
				nueva_imagen = imagen.resize((width, height), Image.ANTIALIAS)

				if extencion_guardado == "jpeg":

					nueva_imagen = nueva_imagen.convert("RGB")

				#guardamos la imagen
				nueva_imagen.save(f"{guardar_en}/{nombre}.{extencion_guardado}", extencion_guardado.upper())


	except:
		print(imagen_grande)
