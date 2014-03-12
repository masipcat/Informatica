#!/usr/bin/python
# -*- coding: utf-8 -*-

from gestioUsuaris import *
import sys, time

"""
EOL 8.1
Per aquest exercici de laboratori cal usar les "List Comprehensions" quan fem un recorregut de les tuples.

Un departament de la universitat vol guardar la informació dels grups que treballen en un projecte. Per cada grup cal guardar la informació
sobre la nota del projecte i el titol del projecte. Per tal de fer aquesta pràctica ens cal un menú on el professor pugui entrar primer els
diferents alumnes, afegir i borrar grups de projecte i finalment escriure la informació de cada projecte. El menú quedaria amb les opcions de:

- Afegir alumne
- Afegir grup de projecte - Aquí t'ha de demanar quins alumnes vols escollir i el titol del projecte
- Llistar els grups de projecte
- Posar nota al grup de projecte
- Esborrar alumne - Cal estar alerta que esborrar un alumne pot modificar els grups de projecte, en cas de que un grup es quedi sense alumnes
s'ha d'esborrar el grup
- Calcular la mitjana de les notes dels grups de projecte
"""

def mostraMenu():
	print "\n MENÚ:\n=============================="
	print "  0. Sortir"
	print "  1. Afegir alumne"
	print "  2. Afegir grup de projecte"
	print "  3. Llistar els grups de projecte"
	print "  4. Esborrar alumne"
	print "  5. Posar nota al grup de projecte"
	print "  6. Calcular la mitjana de les notes dels grups de projecte"
	print "  7. Obrir fitxer"
	print "  8. Desar fitxer"
	print

dic = {}
if dic == {}:
	dic["alumnes"] = {}
	dic["projectes"] = {}
n = -2
while n != 0:
	mostraMenu()
	n = input("Escull una opció: ")
	if n == 1: # Afegir alumne
		key = int(time.time())
		addUser(dic["alumnes"], str(key), raw_input("Nom complet: "))
	elif n == 2: # Afegir projecte
		project_name = raw_input("Nom del projecte: ")
		if dic["projectes"].has_key(project_name):
			print "[FAIL] Aquest projecte ja existeix"
		else:
			# (project_name, description, nota, usuaris)
			if len(dic["alumnes"]) > 0:
				addProject(dic["projectes"], project_name, (project_name, "", 0.0))
				print "Llista d'alumnes:\n"
				for key, value in dic["alumnes"].items():
					print "\t" + str(key), "-", value
				print "\n[-1 per finalitzar l'entrada d'alumnes]"
				n = -2
				alumnes = []
				while n != -1:
					n = input("\nIdentificador de l'alumne/a: ")
					#print dic
					if dic["alumnes"].has_key(str(n)):
						alumnes.append(n)
					elif n != -1:
						print "[FAIL] No existeix cap alumne amb aquest identificador"
				modifyProject(dic["projectes"], project_name, dic["projectes"][project_name] + tuple(alumnes))
			else:
				print "[FAIL] Com ha mínim has d'afegir un projecte"
	elif n == 3: # Llistar projectes
		if len(dic["projectes"]) > 0:
			print "Llista de grups de projectes:"
			for project, values in dic["projectes"].items():
				print "\n" + project + " (nota: " + values[2] + "):\n"
				for alumne in values[3:]:
					print "\t- " + dic["alumnes"][str(alumne)]
		else:
			print "[FAIL] Com a mínim has d'afegir un projecte"
	elif n == 4: # El·liminar alumnes
		if len(dic["alumnes"]) > 0:
			print "Llista d'alumnes:\n"
			for key, value in dic["alumnes"].items():
				print "\t" + str(key), "-", value
			print "\n[-1 per finalitzar l'el·liminació d'alumnes]"
			n = -2
			#print dic["projectes"]
			while n != -1:
				n = input("\nIdentificador de l'alumne/a: ")
				if dic["alumnes"].has_key(str(n)):
					del dic["alumnes"][str(n)]
				elif n != -1:
					print "[FAIL] No existeix cap alumne amb aquest identificador"
			for project in dic["projectes"].values():
				nous_alumnes_grup = [value for value in project[3:] if value in dic["alumnes"].keys()]
				if len(nous_alumnes_grup) == 0:
					del dic["projectes"][project[0]]
				else:
					dic["projectes"][project[0]] = project[:3] + tuple(nous_alumnes_grup)
			#print dic["projectes"]
			#modifyProject(dic["projectes"], project_name, dic["projectes"][project_name] + tuple(alumnes))
		else:
			print "[FAIL] Primer has d'afegir algun alumne/a"
	elif n == 5:
		if len(dic["projectes"]) > 0:
			print "Posar nota al grup de projecte:\n"
			project_keys = []
			for project in enumerate(dic["projectes"].keys()):
				project_keys += [project[1]]
				print "\t" + str(project[0] + 1) + ". " + project[1]
			print
			n = -2
			print "[-1 per acabar]"
			while n != -1:
				n = input("Escull un projecte: ")
				if n > 0 and n <= len(dic["projectes"]):
					val = list(dic["projectes"][project_keys[n-1]])
					val[2] = input("Nota del projecte: ")
					dic["projectes"][project_keys[n-1]] = tuple(val)
					break
				else:
					print "[FAIL] Aquest projecte no existeix"
		else:
			print "[FAIL] Com a mínim has d'afegir un projecte"
	elif n == 6:
		if len(dic["projectes"]) > 0:
			llista_notes = [float(values[2]) for values in dic["projectes"].values()]
			sumatori = 0
			for nota in llista_notes:
				sumatori += nota
			print "\nMitjana: " + str(sumatori / len(llista_notes))
		else:
			print "[FAIL] Com a mínim has d'afegir un projecte"
	elif n == 7:
		dic = obre(raw_input("Nom del fitxer: "))
		if dic == {}:
			dic["alumnes"] = {}
			dic["projectes"] = {}
	elif n == 8:
		desa(raw_input("Nom del fitxer: "), dic)
	else:
		print "Opció invàlida"
print "Bye :D"