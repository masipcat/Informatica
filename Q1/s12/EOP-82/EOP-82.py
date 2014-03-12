#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Dissenyeu una funció que, donat el nom d'un fitxer, retorni una tupla formada pel nom del fitxer, la lletra que més vegades apareix en el fitxer i el
nombre de vegades que hi apareix.
"""

import sys

def open_f(filename):
	f = open(filename)
	content = f.read()
	f.close()
	return content

def crea_llista_buida(longitud):
	llista = []
	for el in range(longitud):
		llista.append(0)
	return llista

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
	return (paraules_llista[posicio_caracter_repetit], max_val)

def listToStr(llista):
	new_str = ""
	for each in llista:
		new_str += "\n" + str(each)
	return new_str[1:]

if len(sys.argv) > 1:
	filename = sys.argv[1]
	print (filename,) + paraula_mes_repetida(open_f(filename).split(" "))
else:
	print "S'ha d'especificar un nom de fitxer"