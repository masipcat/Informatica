#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Exercici 1.3
Sigui l una llista de 10 cadenes de caràcters. Sigui p una llista de 10 enters x
amb 0 ≤ x ≤ 9 que representa una permutaci ́o. Dissenyeu i implementeu una funci ́o tal
que que donats dos paràmetres com l i p retorna la llista l permutada d'acord amb el
que indica p.
"""

def permuta(llista, nou_ordre):
	"""
	Retorna la llista "llista" reordenada segons l'ordre especificat a "nou_ordre".
	>>> permuta(["hola", "1", "22", "3", "4", "55", "6", "7", "0.8", "9"], [8, 9, 7, 6, 5, 4, 3, 2, 1, 0])
	['9', '0.8', '7', '6', '55', '4', '3', '22', 'hola', '1']
	>>> permuta(["1", "2", "3", "5", "4", "6", "8", "7", "9","-1"], [1, 2, 3, 5, 4, 6, 8, 7, 9, 0])
	['-1', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	"""
	return [llista[nou_ordre.index(i)] for i in range(10)]