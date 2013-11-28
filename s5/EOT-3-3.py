def esMesGran(a, b):
	"""
	retorna True si a > b i a*b = 1
	>>> esMesGran(3, 4)
	False
	>>> esMesGran(2, 0.5)
	True
	"""
	return a > b and a * b == 1
