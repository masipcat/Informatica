def lletraDNI(dni):
	"""
	retorna la lletra del DNI
	>>> lletraDNI(39405277)
	'K'
	"""
	lletres = "TRWAGMYFPDXBNJZSQVHLCKE"
	return lletres[dni % 23]

isValid = False
while not isValid:
	dni = input("Introdueix el DNI, sense la lletra: ")
	if dni > 0 and dni > 9999999 and dni < 100000000:
		isValid = True
		print "El teu DNI es:", dni, lletraDNI(dni)
	else:
		print "DNI invalid"
