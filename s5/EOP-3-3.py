def estaCompres(x, a, b):
	"""
	es comprova si x esta dins de [a,b] i retorna "=" (esta compres), "+" (es mes petit) i "-" (es mes gran)
	>>> estaCompres(1, 0, 2)
	'='
	>>> estaCompres(4, 0, 2)
	'-'
	>>> estaCompres(-1, 0, 2)
	'+'
	"""
	if x >= a and x <= b:
		return "="
	elif x < a:
		return "+"
	else:
		return "-"
