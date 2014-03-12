#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Exercici 1.2
Implementeu una funci ́o tal que, donat un diccionari d i una cadena s retorna True si existeix
algun valor del diccionari que  ́es una subcadena d’s. Podeu considerar que els valors del
diccionari sempre s ́on cadenes de caràcters.
"""

def exist(d, s):
	"""
	Retorna True o False segons si existeix algun valor del diccionari que  ́es una subcadena d’s.
	>>> exist({"a": "la", "b": "hola"}, "hola")
	True
	"""
	for value in d.values():
		if s in value:
			return True
	else:
		return False

print exist({"a": "la", "b": "ahola"}, "hola")