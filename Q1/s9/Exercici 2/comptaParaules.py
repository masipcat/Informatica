#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

def llegeixFitxer(nom):
	f = open(nom)
	content = f.read()
	f.close()
	return content

def init():
	args = sys.argv[1:]
	if len(args) == 1:
		contingut = llegeixFitxer(args[0])
		print contingut.count("de")
	else:
		print "Has d'especificar al param. el nom del fitxer"

init()
