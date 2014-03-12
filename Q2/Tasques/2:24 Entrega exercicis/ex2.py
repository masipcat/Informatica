#!/usr/bin/python
# -*- coding: utf-8 -*-

class Fraccio(object):
	def __init__(self, numerador, denominador):
		self.n = numerador
		self.d = denominador

	def sumaFrac(self, frac):
		n = (self.n * frac.d) + (frac.n * self.d)
		d = self.d * frac.d
		return Fraccio(n, d)

	def divisioFrac(self, frac):
		return Fraccio(self.n * frac.d, self.d * frac.n)

	def formatted(self):
		return str(self.n) + "/" + str(self.d)

F1 = Fraccio(5, 1)
F2 = Fraccio(10, 2)
resultat = F1.divisioFrac(F2)
print "Divisió", resultat.formatted()