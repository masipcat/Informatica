def nRepeticions(cadena1, cadena2):
	"""
	>>> nRepeticions("papapapapaapa", "pa")
	6
	"""
	i = 0
	j = 0
	for c in cadena1:
		if cadena1[j:j+2] in cadena2 and len(cadena1[j:j+2]) == len(cadena2):
			i+=1
		j+=1
	return i
