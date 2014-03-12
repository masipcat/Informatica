#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date as d

class Persona(object):
	def __init__(self, n, d):
		self.nom = n
		self.naixement = d

	def edat(self):
		"""
		Retorna un integer entre 0 i infinit si s'ha proporcionat una data de neixament correcta. Retorna -1 si és incorrecta
		"""
		data_n = [int(v) for v in self.naixement.split("/")]
		if len(data_n) != 3:
			return -1
		data_n[2] = 1900 + data_n[2] if data_n[2] > int(str(d.today().year)[-2:]) else 2000 + data[2]
		data_a = (d.today().day, d.today().month, d.today().year)
		if data_a[0] >= data_n[0] and data_a[1] >= data_n[1]:
			return data_a[2] - data_n[2]
		else:
			return data_a[2] - data_n[2] - 1

Jordi = Persona("Jordi", "6/11/95")
print "Hola,\nem dic", Jordi.nom, "i tinc", Jordi.edat(), "anys"