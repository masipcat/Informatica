#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
EOT 8.1
Dins d'un mateix mòdul, dissenyeu una funció que demani a l'usuari dades utilitzant com a sentinella la paraula "fi", aquestes dades
es guardaran a una nova tupla. Afegiu un altre funció que elimini tots els elements imparells de la tupla, si aquests són números de
més de dos xifres o que modifiqui, si són cadenes de caràcters, tots els caràcters passant aquests a majúscules.
Finalment afegiu una funció que retornarà la llista que contindrà la tupla anteriorment modificada.
"""
def demanaDades(end_delimitator):
	dades = []
	end = False
	while not end:
		value = raw_input("Valor: ")
		if value == end_delimitator:
			end = True
		else:
			dades += [value]
	return tuple(dades)

def esborrar(tup):
	i = 0
	new_tup = []
	for el in tup:
		if i % 2 != 0:
			if el.isdigit():
				if float(el) <= 99:
					new_tup += [el]
			else:
				new_tup += [el.upper()]
		else:
			new_tup += [el]
		i += 1
	return tuple(new_tup)

def executa():
	dades = demanaDades("fi")
	return esborrar(dades)