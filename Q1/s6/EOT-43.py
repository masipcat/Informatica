def customReplace(cadena):
	"""
	>>> customReplace("Hola")
	'HolA'
	"""
	nova_cadena = ""
	for char in cadena:
		if char == "a":
			char = "A"
		nova_cadena += char
	return nova_cadena
