#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=======
Circuit
=======

Aquest mòdul conté la classe Circuit i és l'script principal
"""

from component import *

class Circuit(object):

	def __init__(self):
		self._components = []
		
	def afegirComponent(self, c):
		"""
		Afegeix un component al Circuit

		:param c: Component a afegir
		:type c: Component

		>>> c = Component(43, 130, 2.)
		>>> circ = Circuit()
		>>> circ.afegirComponent(c)
		>>> circ.calcPreu()
		2.0
		"""
		self._components.append(c)
	
	def calcPreu(self):
		"""
		Retorna un flotant que és la suma de tots els preus de tots els components

		>>> c = Component(43, 130, 2.)
		>>> c2 = Component(44, 230, 4.)
		>>> circ = Circuit()
		>>> circ.afegirComponent(c)
		>>> circ.afegirComponent(c2)
		>>> circ.calcPreu()
		6.0
		"""
		return sum([component.getPreu() for component in self._components])

c = Component(43, 130, 2.)
c2 = Component(44, 200, 1.5)
circ = Circuit()
circ.afegirComponent(c)
circ.afegirComponent(c2)
print "Preu total:", circ.calcPreu(), "€"
