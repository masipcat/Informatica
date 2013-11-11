from funcionsMat import *

def esValida(matriu):
	"""
	Es valida si un array de 2d esta ben construit
	"""
	first_row_len = len(matriu[0])
	for row in matriu:
		if len(row) != first_row_len:
			return False
	return True

def producte_matriu(matriu1, matriu2):
	if esValida(matriu1) and esValida(matriu2):
		# Longitud d'una fila de la primera matriu
		m = len(matriu1)

		# Longitud de l'ultima columna de la segona matriu
		n = len(matriu2)

		nova_matriu = []

		if n == m:
			# Passa per cada fila
			for i, row in enumerate(matriu1):
				new_column = []
				# Realitza la multiplicació per cada columna
				for k in range(len(matriu2[-1])):
					suma_productes = 0
					# Fa la suma del producte de cada fila
					for j, value in enumerate(row):
						suma_productes += value * matriu2[j][k]
					new_column += [suma_productes]
				nova_matriu += [new_column]
			return nova_matriu
		else:
			return False
	else:
		return False

#matriu1 = [[1,2], [3,4]]
#matriu2 = [[1,2], [3,4]]

matriu1 = [[1,2,3], [-1, 5, 0], [2,1,2]]
matriu2 = [[1,2,-1,5], [0,-1,2,3], [3,2,4,6]]

matriu = producte_matriu(matriu1, matriu2)
if matriu != False:
	escriureMatriu(matriu)
else:
	print "Hi ha hagut un error alhora de calcula la matriu"