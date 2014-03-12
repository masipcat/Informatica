#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=============
Garage module
=============

This module contains Garage Class
"""

from car import *
import random

class Garage(object):

	def __init__(self, name):
		"""
		Garage constructor

		:param name: Garage name
		:type name: str
		"""
		self._name = name
		self._cars = {}

	def addCar(self, car):
		"""
		Add a car to this garage. Car must have a valid license

		:param car: Car object
		:type car: Car

		>>> car = Car(CarLicense("7777 JMR"))
		>>> car_2 = Car(CarLicense("matricula-invalida"))
		>>> g = Garage("Cal Masip")
		>>> g.addCar(car)
		>>> g.addCar(car_2)
		>>> g.countCars()
		1
		"""
		if car.getLicense().getValue() not in self._cars.keys() and car.getLicense().isValid():
			self._cars[car.getLicense().getValue()] = car

	def removeCarByLicense(self, license):
		"""
		Remove the car with license `license`, if exist. Return `True` if car is removed and `False` if isn't removed

		:param license: Car license
		:type license: CarLicense

		>>> car = Car(CarLicense("7777 JMR"))
		>>> car.setColor(Color(0, 255, 50))
		>>> g = Garage("Cal Masip")
		>>> g.addCar(car)
		>>> g.removeCarByLicense(CarLicense("4444 RMJ"))
		False
		>>> g.removeCarByLicense(CarLicense("7777 JMR"))
		True
		"""
		if license.getValue() in self._cars.keys():
			del self._cars[license.getValue()]
			return True
		return False

	def countCars(self):
		"""
		Count the number of cars in the garage. Returns an `int`.

		>>> car = Car(CarLicense("7777 JMR"))
		>>> car_2 = Car(CarLicense("6688 JMR"))
		>>> g = Garage("Cal Massip")
		>>> g.addCar(car)
		>>> g.addCar(car_2)
		>>> g.countCars()
		2
		"""
		return len(self._cars)

	def getRandomCar(self):
		"""
		Returns a random car object from garage
		"""
		n_cars = self.countCars()
		return self._cars.values()[random.randint(0, n_cars - 1)] if n_cars > 1 else False

	def listOfCars(self):
		return self._cars.keys()