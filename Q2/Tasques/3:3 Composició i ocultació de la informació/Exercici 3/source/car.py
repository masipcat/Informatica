#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
==========
Car module
==========

This module contains Car Class
"""

import os.path
from utiles import Color, CarLicense

class Car(object):

	# Constants que representen el tipus de motor
	ENGINE_DIESEL = 0
	ENGINE_GASOLINE = 1

	def __init__(self, car_license):
		"""
		Car constructor

		:param car_license: Car license
		:type car_license: CarLicense

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.getLicense().getValue()
		'1234 WWW'
		"""
		
		self._license = car_license
		self._engine = 0
		self._color = Color(0, 0, 0).getValue()
		self._model = "unknown model"

	def getLicense(self):
		"""
		Return an string from CarLicense object

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.getLicense().getValue()
		'1234 WWW'
		"""
		return self._license

	def setLicense(self, license):
		"""
		Set license using CarLicense class

		:param license: Set license
		:type license: CarLicense

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setLicense(CarLicense("2222 BCD"))
		>>> renault.getLicense().getValue()
		'2222 BCD'
		"""
		self._license = license

	def getModel(self):
		"""
		Get the model of this car

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setModel("Renault Grand Modus")
		>>> renault.getModel()
		'Renault Grand Modus'
		"""
		return self._model

	def setModel(self, model):
		"""
		Set the model of this car

		:param model: Car model
		:type model: str

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setModel("Renault Grand Modus")
		>>> renault.getModel()
		'Renault Grand Modus'
		"""
		self._model = model

	def getColor(self):
		"""
		Return an RGB Color

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setColor(Color(24,24,0))
		>>> renault.getColor()
		(24, 24, 0)
		"""
		return self._color

	def setColor(self, color):
		"""
		Change car color

		:param color: RGB Color
		:type color: Color

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setColor(Color(24,24,0))
		>>> renault.getColor()
		(24, 24, 0)
		"""
		self._color = color.getValue()

	def getEngine(self):
		"""
		Return 0 for `ENGINE_DIESEL` and 1 for `ENGINE_GASOLINE`

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setEngine(Car.ENGINE_GASOLINE)
		>>> renault.getEngine()
		1
		"""
		return self._engine

	def setEngine(self, engine):
		"""
		Set engine type. Use `ENGINE_DIESEL` and `ENGINE_GASOLINE` constants.

		:param engine: Car.ENGINE_DIESEL or Car.ENGINE_GASOLINE
		:type engine: int

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setEngine(Car.ENGINE_DIESEL)
		>>> renault.getEngine()
		0
		"""
		if engine in [0, 1]:
			self._engine = engine

	def save(self, fname):
		"""
		Save car instance to file with name `fname`

		:param fname: Filename
		:type fname: str
		
		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setEngine(1)
		>>> renault.setColor(Color(2,3,4))
		>>> renault.save("Renault")
		>>> renault.setModel("heyRe")
		>>> renault.setEngine(0)
		>>> renault.getEngine()
		0
		>>> renault.read("Seat")
		False
		>>> renault.read("Renault")
		True
		>>> renault.getModel()
		'unknown model'
		>>> renault.getEngine()
		1
		"""
		f = open(fname + ".car", "w")
		color = " ".join([str(e) for e in self._color])
		f.write(self._license.getValue() + "\n" + str(self._engine) + "\n" + color + "\n" + self._model)
		f.close()

	def read(self, fname):
		"""
		Read car instance from file with name `fname` and returns `True` or `False`

		:param fname: Filename
		:type fname: str

		>>> renault = Car(CarLicense("1234 WWW"))
		>>> renault.setEngine(1)
		>>> renault.setColor(Color(2,3,4))
		>>> renault.save("Renault")
		>>> renault.setModel("heyRe")
		>>> renault.setEngine(0)
		>>> renault.getEngine()
		0
		>>> renault.read("Seat")
		False
		>>> renault.read("Renault")
		True
		>>> renault.getModel()
		'unknown model'
		>>> renault.getEngine()
		1
		"""
		if os.path.isfile(fname + ".car"):
			f = open(fname + ".car", "r")
			content = f.read().split("\n")
			f.close()
			if len(content) == 4:
				self._license = CarLicense(content[0])
				self._engine = int(content[1])
				c = content[2].split(" ")
				if len(c) == 3:
					self._color = tuple(c)
				else:	
					self._color = Color(0, 0, 0).getValue()
				self._model = content[3]
			return True
		return False

	def __eq__(self, other):
		return self.getLicense().getValue() == other.getLicense().getValue()

	def __str__(self):
		return self.getLicense().getValue() + " - " + str(self.getColor()) + " - " + self.getModel()