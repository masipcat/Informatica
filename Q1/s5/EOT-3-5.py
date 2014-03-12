def capicua(a, b):
	"""
	retorna "ABBA" si c="A" i s="BB" -> a + b + a
	>>> capicua("ab", "cc")
	'ccabcc'
	>>> capicua("23", "5")
	'5235'
	>>> capicua(" ", " ")
	'   '
	"""
	return b + a + b