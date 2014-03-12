def es_capicua(s):
	"""
	>>> es_capicua('abba')
	True
	>>> es_capicua('abab')
	False
	>>> es_capicua('tenet')
	True
	>>> es_capicua('banana')
	False
	>>> es_capicua('straw warts')
	True
	"""
	s_invertida = ""
	for c in s:
		s_invertida = c + s_invertida
	return s == s_invertida
