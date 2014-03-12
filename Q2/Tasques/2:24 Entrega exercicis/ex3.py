#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Exercici 2.6
Les resistències es marquen amb unes bandes de color per indicar el seu valor nominal i la seva tolerància.
En aquesta referència trobareu els detalls d'aquesta codificaci ́o:
"""

class Codif(object):
	# Valors del multiplicador
	__multiplier = [1, 10, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**9, 10**9, 10**(-1), 10**(-2)]
	__colors = ["Negre", "Marró", "Vermell", "Taronja", "Groc", "Verd", "Blau", "Violeta", "Gris", "Blanc"]

	def __toNum(self, color):
		return str(self.__colors.index(color))

	def __init__(self, a, b, c):
		if a in self.__colors and b in self.__colors and c in self.__colors:
			a, b, c = self.__toNum(a), self.__toNum(b), self.__toNum(c)
			self.__value = int(a + b + str(self.__multiplier[int(c)])[1:])
			self.__color = self.__colors[int(a)] + ", " + self.__colors[int(b)] + ", " + self.__colors[int(c)]
		else:
			self.__value = -1
			self.__color = "ERROR"

	def value(self):
		return self.__value

	def colors(self):
		return self.__color

# "Doctest" de la classe
Resitor = Codif("Negre", "Marró", "Vermell")
print "El valor de la resistència és", Resitor.value()
print "Els colors de la resistència són", Resitor.colors()