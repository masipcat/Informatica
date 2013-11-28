#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def endevina():
	return randint(1, 10)

solucio = endevina()
n = -1

print "Endevina el nombre entre l'1-10 que estic pensant"

while(n != solucio):
	n = input("Escriu un nombre: ")
	if n < solucio and n > 0:
		print "Estic pensant en un nombre més gran"
	elif n > solucio and n < 10:
		print "Estic pensant en un nombre més petit"
	elif n == solucio:
		break
	else:
		print "BURRO!!! Has d'escriure un número entre l'1-10!!!"

print "Molt bé!! El nombre que estava pensant és", n
