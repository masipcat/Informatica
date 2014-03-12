#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

def comptaAprovats(text):
	resultat = [0, 0]
	for i, alumne in enumerate(text.split("\n")):
		alumne = alumne.split(" ")
		if len(alumne) == 2: 
			if int(alumne[1]) >= 5:
				resultat[0] += 1 
			else:
				resultat[1] += 1
		else:
			print "[ERROR] La línia", i, "té un format incorrecte"
	return resultat

def llegeixFitxer(nom):
	f = open(nom)
	content = f.read()
	f.close()
	return content

def init():
	args = sys.argv[1:]
	if len(args) == 1:
		notes = comptaAprovats(llegeixFitxer(args[0]))
		print "Aprovats:", notes[0]
		print "No aprovats:", notes[1]
	else:
		print "Has d'especificar al param. el nom del fitxer"

init()
