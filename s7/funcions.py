#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def netejaPantalla():
	"""
	Mostra cinc linies en blanc
	"""
	print "\n" * 25

def menuOpcions():
	'''
	Mostra menu opcions per pantalla
	'''
	print "1. Inici partida"
	print "0. Sortir"

def paraulaCorrecta():
	"""
	Retorna una paraula correcte. Demana tantes paraules fins que sigui paraula alfanumèrica
	"""
	lletres = ""
	t = False
	while not t:
		paraula = raw_input("Entra paraula: ")
		t = checkParaula(paraula)
		if not t:
			print "Paraula no vàlida. Tornar-ho a provar"
	return paraula

def checkParaula(paraula):
	"""
	retorna True si "paraula" no conté digits ni caràcters especials, equival .isalpha()
	>>> checkParaula("hola1+!·")
	False
	>>> checkParaula("hola")
	True
	"""
	isValid = True
	for char in paraula:
		if char not in string.letters:
			isValid = False
			break
	return isValid

def checkOpcio(dada):
	"""
	retorna True si es un caràcter amb valor 0 o 1
	>>> checkOpcio("11")
	False
	>>> checkOpcio("1")
	True
	>>> checkOpcio("0")
	True
	"""
	return len(dada) == 1 and (dada == "0" or dada == "1")

def opcioCorrecte():
	'''
	Mostra menu opcions i demana opcio fins que sigui correcta
	'''
	t = False
	while not t:
		menuOpcions()
		opcio = raw_input("Introdueix opcio: ")
		t = checkOpcio(opcio)
		if not t:
			print "Reintrodueix una opcio correcte"

def esLletraCorrecta():
	"""
	Demana letres a l'usuari fins que sigui lletra alfanumerica. Retorna la lletra.
	"""
	t = False
	while not t:
		c = raw_input("Entri una lletra: ")
		t = len(c) == 1 and c in string.letters
	return c

def actualitzaOculta(paraula, lletra, oculta):
	"""
	Donada una paraula substitueix a "oculta" la lletra que es trobi a "paraula
	>>> actualitzaOculta("prova", "v", "p$$$$")
	'p$$v$'
	>>> actualitzaOculta("informatica", 'i', "$nformat$ca")
	'informatica'
	>>> actualitzaOculta("test", 'j', "$$$$")
	'$$$$'
	"""
	s = ""
	i = 0
	for c in paraula:
		if c == lletra:
			s += lletra
		else:
			s += oculta[i]
		i+=1
	return s