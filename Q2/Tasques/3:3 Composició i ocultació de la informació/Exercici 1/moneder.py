#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=======
Moneder
=======
"""

class moneder(object):

	def __init__(self, m1=0, m2=0, m3=0):
		self._dict = {
			"1": m1,
			"2": m2,
			"3": m3
		}
		
	def obteMonedesM1(self):
		"""
		Obté el primer grup de monedes
		"""
		return self._dict[2]
		
	def obteMonedesM2(self):
		"""
		Obté el segon grup de monedes
		"""
		return self._dict[2]

	def obteMonedesM3(self):
		"""
		Obté el tercer grup de monedes
		"""
		return self._dict[3]
				
	def camviMonedesM1(self, d):

		self._dict[1] += d
		return self._dict[1]
		
	def camviMonedesM2(self, d):
		self._dict[2]+=d
		return self._dict[2]
		
	def camviMonedesM3(self, d):
		self._dict[3]+=d
		return self._dict[3]
	
	def dinersAlMoneder(self):
		return sum([key * value for key, value in self._dict.items()])
	
	def afegirMonedes(self, s):
		for a in self._dict:
			self._dict[a] += s._d[a]

