#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========
Component
=========

Aquest mòdul conté la classe Component
"""

class Component(object):
	
	def __init__(self, cid, weight, price):
		self._cid = cid
		self._weight = weight
		self._price = price
		
	def getId(self):
		"""
		Retorna l'id del component

		>>> c = Component(43, 130, 2.)
		>>> c.getId()
		43
		"""
		return self._cid
	
	def getPes(self):
		"""
		Retorna el pes del component
		>>> c = Component(43, 130, 2.)
		>>> c.getPes()
		130
		"""
		return self._weight
	
	def getPreu(self):
		"""
		Retorna el preu del component
		>>> c = Component(43, 130, 2.)
		>>> c.getPreu()
		2.0
		"""
		return self._price
	
	def setPreu(self, price):
		"""
		Es defineix un nou preu del component

		:param price: nou preu del component
		:type price: float

		>>> c = Component(43, 130, 2.0)
		>>> c.setPreu(4.)
		>>> c.getPreu()
		4.0
		"""
		self._price = price