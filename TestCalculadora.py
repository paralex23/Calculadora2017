import unittest

from calculadora import Calculadora

class CalculadoraTEst(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2,2)
		self.assertEquals(self.calc.obtener_resultado(),4)

	def test_sumar_3_mas_3_igual_6(self):
		self.calc.suma(3,3)
		self.assertEquals(self.calc.obtener_resultado(),6)

	def test_sumar_menos_1_mas_2_igual_1(self):
		self.calc.suma(-1,2)
		self.assertEquals(self.calc.obtener_resultado(),1)

	def test_restar_2_menos_2_igual_0(self):
		self.calc.resta(2,2)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_restar_2_menos_3_igual_menos_1(self):
		self.calc.resta(2,3)
		self.assertEquals(self.calc.obtener_resultado(),-1)

	def test_multiplicacion_2_por_3_igual_6(self):
		self.calc.multiplicacion(2,3)
		self.assertEquals(self.calc.obtener_resultado(),6)

	def test_multiplicacion_menos_2_por_3_igual_menos_6(self):
		self.calc.multiplicacion(-2,3)
		self.assertEquals(self.calc.obtener_resultado(),-6)

	def test_multiplicacion_2_por_0_igual_0(self):
		self.calc.multiplicacion(2,0)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_divicion_2_entre_2_igual_1(self):
		self.calc.divicion(2,2)
		self.assertEquals(self.calc.obtener_resultado(),1)

	


if __name__ == '__main__':
	unittest.main()