#clase encargada de devolver direcciones para centrar la ventana
class Posicionar():

	posicion_x = ""
	posicion_y = ""


	"""proceso para devolver las direcciones donde estara centrada la ventana
	width > de la ventana
	height > de la ventana
	monitor_width > de la pantalla
	monitor_height > de la pantalla"""
	def construir_posicion(self, width, height, monitor_width, monitor_height):

		self.posicion_x = monitor_width // 2

		self.posicion_x = self.posicion_x - (width // 2) 

		self.posicion_y = monitor_height // 2

		self.posicion_y = self.posicion_y - (height // 2)


		#se devuelven las cordenadas X & Y
		return (self.posicion_x, self.posicion_y)





