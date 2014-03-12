#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isMonosilab(paraula):
	'''
	Retorna True o False segons si és monosilab o not
	>>> isMonosilab("tal")
	True
	>>> isMonosilab("patata")
	False
	'''
	vocals = "aàeéèiíoòóuú"
	vocals += vocals.upper()
	nVocals = 0
	for char in paraula:
		if char in vocals:
			nVocals += 1
	return len(paraula) >= 2 and nVocals == 1

def foraVocals(paraula):
	'''
	El·limina totes les vocals d'una paraula
	>>> foraVocals("hola")
	"hl"
	>>> foraVocals("aeiou")
	""
	'''
	vocals = "aàeéèiíoòóuú"
	vocals += vocals.upper()
	resposta = ""
	for char in paraula:
		if char not in vocals:
			resposta += char
	return resposta

def removeFirstLetter(lletra, paraula):
	'''
	El·limina la primera lletra d'una paraula:
	>>> removeFirstLetter("h", "hola")
	"ola"
	>>> removeFirstLetter("c", "hola")
	"hola"
	'''
	if paraula[0] == lletra or paraula[0] == lletra.upper():
		return paraula[1:]
	return paraula

def transformarParaula(paraula):
	'''
	Aplica els 'filetres' següents
	'''
	if isMonosilab(paraula):
		paraula = foraVocals(paraula)
	else:
		# Canvia que -> ke
		paraula = paraula.replace("que", "ke")

		# Canvia qui -> ki
		paraula = paraula.replace("qui", "ki")

		# Canvia per -> x
		paraula = paraula.replace("per", "x")

		# Canvia ss -> s
		paraula = paraula.replace("ss", "s")

		# El·limina les "h" si és la primera lletra
		paraula = removeFirstLetter("h", paraula)
	return paraula

def toSMS(text):
	text += " " # Afegeixo un espai al final perquè "detecti" la última paraula
	paraula, sms = "", ""
	for char in text:
		if char == " ":
			sms += transformarParaula(paraula) + " "
			paraula = ""
		else:
			paraula += char
	return sms[0:len(sms) - 1]

print toSMS("Hola que tal per on passeu?")