#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date as d

class Data(object):
	def __init__(self, dia, mes, year):
		self.dia, self.mes = int(dia), int(mes)
		self.any = int(year)
		if year <= 99: # Si el format dels anys és de dos dígits...
			self.any = 1900 + self.any if 2000 + self.any > d.today().year else 2000 + self.any

	def anysDesDe(self, data):
		"""
		Retorna el nombre d'anys que han passat comptant els mesos i els dies. Si la data és negativa retorna -1
		"""
		if self.dia >= data.dia and self.mes >= data.dia:
			return self.any - data.any if self.any - data.any >= 0 else -1
		return self.any - data.any - 1 if self.any - data.any -1 >= 0 else -1

class Persona(object):
	def __init__(self, n, d):
		self.nom = n
		self.naixement = d

	def edat(self):
		"""
		Retorna un integer entre 0 i infinit si s'ha proporcionat una data de neixament correcta. Retorna -1 si és incorrecta
		"""
		neixament = [int(v) for v in self.naixement.split("/")]
		if len(neixament) != 3:
			return -1
		neixament = Data(neixament[0], neixament[1], neixament[2])
		avui = Data(d.today().day, d.today().month, d.today().year)
		return avui.anysDesDe(neixament)

Jordi = Persona("Jordi", "24/10/84")
print "Hola,\nem dic", Jordi.nom, "i tinc", Jordi.edat(), "anys"