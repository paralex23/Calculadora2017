class Calculadora():
	
	def __init__(self):
		self.edad= ""

	def obtener_edad(self):
		return self.edad

	def edad(self):
		if edad < 0:
			edad = "no existes"
		elif edad < 13 and edad > 0:
			edad = "eres nino"
		elif edad < 18 and edad > 13 :
			edad = "eres adolescente"
		elif edad < 120 and edad > 18:
			edad = "eres adulto mayor"
		elif edad > 120:
			edad = "eres Mumm-Ra"
