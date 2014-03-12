#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Exercici 1.4
Sigui p una paraula. Definiu la funcio desplega(p) tal que donada una paraula p retorna
la llista de tots els prefixos de p. Per exemple, si p=’hola’ llavors desplega(p) ha de
tornar la llista [’h’, ’ho’, ’hol’, ’hola’].
"""

def desplega(p):
	"""
	Retorna la llista de tots els prefixos de p
	>>> desplega("hola")
	['h', 'ho', 'hol', 'hola']
	"""
	return [p[:s] for s in range(1, len(p) + 1)]