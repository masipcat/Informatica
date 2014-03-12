#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=============
Utiles module
=============

This module contains other classes
"""

from string import letters

class Color(object):

	def __init__(self, red, green, blue):
		"""
		Color constructor

		:param red: Red color between 0-255
		:type red: int
		:param green: Green color between 0-255
		:type green: int
		:param blue: Blue color between 0-255
		:type blue: int

		>>> c = Color(255, 255, 255)
		>>> c.getValue()
		(255, 255, 255)
		"""
		self._color = (0, 0, 0)
		self.setValue(red, green, blue)

	def getValue(self):
		"""
		Get color value as tuple

		>>> c = Color(255, 255, 255)
		>>> c.getValue()
		(255, 255, 255)
		"""
		return self._color

	def setValue(self, red, green, blue):
		"""
		Set a new color

		:param red: Red color between 0-255
		:type red: int
		:param green: Green color between 0-255
		:type green: int
		:param blue: Blue color between 0-255
		:type blue: int

		>>> c = Color(255, 255, 255)
		>>> c.setValue(255, 0, 255)
		>>> c.getValue()
		(255, 0, 255)
		"""
		color_range = range(256)
		if red in color_range and green in color_range and blue in color_range:
			self._color = (red, green, blue)

class CarLicense(object):

	def __init__(self, license):
		"""
		CarLicense constructor. License format `1234 ABC`

		>>> l = CarLicense("1234 JMR")
		>>> l.getValue()
		'1234 JMR'
		"""
		self._license = "invalid"
		self._is_valid_license = False
		for i, char in enumerate(license):
			if i < 4:
				if char not in "0123456789": break
			elif i == 4:
				if char != " ": break
			elif i > 4 and i < 7:
				if char not in letters: break
		else:
			self._license = license
			self._is_valid_license = True

	def getValue(self):
		"""
		Get license value
		
		>>> l = CarLicense("1234 JMR")
		>>> l.getValue()
		'1234 JMR'
		"""
		return self._license

	def isValid(self):
		"""
		Return `True` o `False`. Check if license have a valid format
		
		>>> l = CarLicense("123456 JMR")
		>>> l.isValid()
		False
		>>> l.getValue()
		'invalid'
		"""
		return self._is_valid_license