#!/usr/bin/python
# -*- coding: utf-8 -*-

from gestioUsuaris import *
import hashlib

filename = raw_input("Nom del fitxer dels usuaris: ")
dic = obre(filename)
logged = False

while not logged:
	username = raw_input("Usuari: ")
	passwd = raw_input("Contrasenya: ")
	passwd = hashlib.sha224(passwd).hexdigest()
	
	if dic.has_key(username):
		if dic[username]["passwd"] == passwd:
			print "\n[OK] Has iniciat sessió"
			logged = True
		else:
			print "\n[FAIL] Usuari o contrasenya incorrecte"
	else:
		print "\n[FAIL] Usuari o contrasenya incorrecte"