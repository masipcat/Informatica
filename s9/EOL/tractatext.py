#!/usr/bin/python
# -*- coding: utf-8 -*-

from tractaparaules import *
import sys

def llegeixFitxer(nom):
	f = open(nom)
	content = f.read()
	f.close()
	return content

def escriuFitxer(contingut):
	f = open("resultat.txt", "a")
	f.write(contingut)
	f.close()

params = sys.argv[1:]
if len(params) >= 2:
	filename = params[0]
	paraules = params[1:]
	contingut_fitxer = llegeixFitxer(filename)
	paraules_del_fitxer = extreu_paraules(contingut_fitxer)
	paraula_llarga = paraula_llarga(contingut_fitxer.split())
	caracter_apareix = conta_caracters(contingut_fitxer)
	paraula_mes_repetida = paraula_mes_repetida(paraules_del_fitxer)

	aparicions = ""
	for paraula in paraules:
		n = conta_paraula(paraula, paraules_del_fitxer)
		if n > 0:
			aparicions += ', la paraula "' + paraula + '" apareix ' + str(n) + " vegada"
		else:
			aparicions += ', la paraula "' + paraula + '" no apareix cap vegada'
	aparicions = aparicions[2:].capitalize() + "."

	nou_fitxer = "RESULTATS EN {file}:\n{separator}\nParaula més llarga: {paraula_llarga}\nCaràcter que apareix més vegades: lletra \"{lletra_repeteix}\", {vegades_repeteix} vegades\n{vegades_apareixen_paraules}\nEn les {n_linies} primeres línies, la paraula que més és repeteix és: \"{paraula_mes_repetida}\""
	nou_fitxer = nou_fitxer.replace("{file}", filename.upper())
	nou_fitxer = nou_fitxer.replace("{separator}", (len(filename) + 14)*"=")
	nou_fitxer = nou_fitxer.replace("{paraula_llarga}", paraula_llarga)
	nou_fitxer = nou_fitxer.replace("{lletra_repeteix}", caracter_apareix[1])
	nou_fitxer = nou_fitxer.replace("{vegades_repeteix}", str(caracter_apareix[0]))
	nou_fitxer = nou_fitxer.replace("{n_linies}", str(len(contingut_fitxer.split("\n"))))
	nou_fitxer = nou_fitxer.replace("{vegades_apareixen_paraules}", aparicions)
	nou_fitxer = nou_fitxer.replace("{paraula_mes_repetida}", paraula_mes_repetida)
	
	# Desa l'analisi:	
	escriuFitxer(nou_fitxer)
else:
	print "Has d'especificar al param. el nom del fitxer i una paraula com a minim"