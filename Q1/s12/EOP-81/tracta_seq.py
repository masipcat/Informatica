#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

"""
Dissenyeu un programa anomenat tracta_seq.py que, donats una sèrie de valors enters entrats per la línia de comandes, en generi una tupla,
en calculi el màxim i el mínim (en una sola funció) i guardi aquestes tres dades en una llista. Finalment, el programa ha d'emmagatzemar en un fitxer
anomenat fitxer_tupla.txt la llista creada.
"""

def save(content):
	f = file("fitxer_tupla.txt", "w+")
	f.write(content)
	f.close()

def toTuple(llista):
	new_llista = []
	for each in llista:
		new_llista.append(int(each))
	return tuple(new_llista)

def listToStr(llista):
	new_str = ""
	for each in llista:
		new_str += "\n" + str(each)
	return new_str[1:]

def calcular(tup):
	return [min(tup), max(tup), tup]

save(listToStr(calcular(toTuple(sys.argv[1:]))))