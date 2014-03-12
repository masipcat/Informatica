#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcions import *

'''
TODO:
Tornar a jugar, comptar intents, sortir del programa
'''

paraula = paraulaCorrecta()
netejaPantalla()
oculta=len(paraula) * "*"
print "paraula a endevinar: " + oculta
while oculta != paraula:
	lletra = esLletraCorrecta()
	oculta = actualitzaOculta(paraula, lletra, oculta)
	print "paraula a endevinar: " + oculta
print "L'has endevinat!!\nJa pots tornar a jugar"
