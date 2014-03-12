#!/usr/bin/python
# -*- coding: utf-8 -*-

from gestioUsuaris import *
import sys

def mostraMenu():
	print "\nMENÚ:"
	print "0. Sortir"
	print "1. Afegir usuari"
	print "2. Modificar usuari"
	print "3. Eliminar usuaris"
	print "4. Desar canvis"
	print "5. Llegir fitxer\n"

nom_camps = {"nom": "Nom", "cognom": "Cognom", "passwd": "Clau d'accés", "telf": "Telèfon", "adress": "Adreça"}
fitxerLlegit, canvisDesats = False, False
dic = {}
n = -2
while n != 0:
	mostraMenu()
	n = input("Escull una opció: ")

	if n == 0:
		if not canvisDesats:
			opcio = raw_input("\nNo has desat els canvis, estas segur que vols sortir [Y,n]? ")
			if opcio == "n" or opcio == "N":
				n = -2
	elif n == 1:
		if fitxerLlegit:
			values = {}
			username = ""
			while dic.has_key(username) or username == "":
				username = raw_input("Nom d'usuari: ")
				if dic.has_key(username):
					print "\n[FAIL] Aquest usuari ja existeix"
			# camps està definit a "gestióUsuaris.py"
			for camp in camps:
				values[camp] = raw_input(nom_camps[camp] + ": ")
			if addUser(dic, username, values):
				canvisDesats = False
		else:
			print "\n[FAIL] Encara no s'ha obert cap fitxer"
	elif n == 2:
		if fitxerLlegit:
			username = ""
			while not dic.has_key(username) or username == "":
				username = raw_input("Nom d'usuari: ")
				if not dic.has_key(username):
					print "\n[FAIL] Aquest usuari no existeix"
			# camps està definit a "gestióUsuaris.py"
			values = dic[username]
			for camp in camps:
				valor_actual = " (" + dic[username][camp] + ")"
				if camp == "passwd":
					valor_actual = ""
				new_value = raw_input(nom_camps[camp] + valor_actual + ": ")
				if new_value != "":
					values[camp] = new_value
			if modifyUser(dic, username, values):
				canvisDesats = False
		else:
			print "\n[FAIL] Encara no s'ha obert cap fitxer"
	elif n == 3:
		if fitxerLlegit:
			username = ""
			while not dic.has_key(username) or username == "":
				username = raw_input("Nom d'usuari: ")
				if not dic.has_key(username):
					print "\n[FAIL] Aquest usuari no existeix"
			if delUser(dic, username):
				print "\n[OK] L'usuari ha estat el·liminat"
				canvisDesats = False
		else:
			print "\n[FAIL] Encara no s'ha obert cap fitxer"
	elif n == 4:
		if fitxerLlegit:
			desa(filename, dic)
			canvisDesats = True
		else:
			print "\n[FAIL] Encara no s'ha obert cap fitxer"
	elif n == 5:
		filename = raw_input("Nom del fitxer dels usuaris: ")
		dic = obre(filename)
		fitxerLlegit, canvisDesats = True, True
	else:
		print "Opcio invàlida"
print "Bye :)"