import string

def neteja_paraula(paraula):
	nova_paraula = ""
	for char in paraula:
		if char in string.letters:
			nova_paraula += char
	return nova_paraula

def extreu_paraules(cadena):
	llista = []
	for paraula in cadena.split():
		llista.append(neteja_paraula(paraula))
	return llista

def conta_paraula(paraula, llista):
	i = 0
	for el in llista:
		if paraula == el:
			i += 1
	return i

def crea_llista_buida(longitud):
	llista = []
	for el in range(longitud):
		llista.append(0)
	return llista

def conta_caracters(cadena):
	# string.printable es la llista de tots els caracters ASCII que es poden mostrar per pantalla
	n_aparicions = crea_llista_buida(len(string.printable))
	for char in cadena:
		# S'incrementa 1 a la posicio equivalent del caracter a string.printable
		n_aparicions[string.printable.index(char)] += 1
	
	# Es cerca quin es el valor mes gran
	max_val = 0
	for val in n_aparicions:
		if val > max_val:
			max_val = val
	posicio_caracter_repetit = n_aparicions.index(max_val)
	return [posicio_caracter_repetit, string.printable[posicio_caracter_repetit]]

def paraula_mes_repetida(llista):
	paraules_llista = []
	for paraula in llista:
		if paraula_mes_repetida not in paraules_llista:
			paraules_llista += [paraula]

	n_aparicions = crea_llista_buida(len(paraules_llista))
	for paraula in llista:
		# S'incrementa 1 a la posicio equivalent del caracter a string.printable
		n_aparicions[paraules_llista.index(paraula)] += 1
	
	# Es cerca quin es el valor mes gran
	max_val = 0
	for val in n_aparicions:
		if val > max_val:
			max_val = val
	posicio_caracter_repetit = n_aparicions.index(max_val)
	return paraules_llista[posicio_caracter_repetit]

def paraula_llarga(paraules):
	llargaria = 0
	paraula_mes_llarga = ""
	for paraula in paraules:
		if len(paraula) > llargaria:
			llargaria = len(paraula)
			paraula_mes_llarga = paraula
	return paraula_mes_llarga