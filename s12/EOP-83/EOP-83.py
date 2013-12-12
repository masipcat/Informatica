#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

"""
Dissenyeu una funció que, donat el nom d'un fitxer, retorni una tupla formada pel nom del fitxer, la frase més llarga del fitxer i la frase més curta.
"""

def open_f(filename):
	f = open(filename)
	content = f.read()
	f.close()
	return content

def max_i_min(string):
	llista = string.split(". ")
	frase_mes_llarga = ""
	for frase in llista:
		if len(frase) > len(frase_mes_llarga):
			frase_mes_llarga = frase
	frase_mes_curta = " " * len(frase_mes_llarga)
	for frase in llista:
		if len(frase) < len(frase_mes_curta):
			frase_mes_curta = frase
	return (frase_mes_llarga, frase_mes_curta)

if len(sys.argv) > 1:
	filename = sys.argv[1]
	print (filename,) + max_i_min(open_f(filename))
else:
	print "S'ha d'especificar un nom de fitxer"