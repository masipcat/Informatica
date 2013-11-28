#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

def dictToStr(dic):
	txt = ""
	for k in dic:
		valors = ""
		for field in dic[k]:
			if field == "passwd":
				dic[k][field] = hashlib.sha224(dic[k][field]).hexdigest()
			valors += "|" + field + ":" + dic[k][field]
		txt += "\n" + k + "::" + valors[1:]
	return txt[1:]

camps = ["nom", "cognom", "passwd", "telf", "adress"]

def strToDict(txt):
	"""
	dic = {"user": {"nom":"", "cognom":"", "passwd":"", "telf": "", "adress": ""}}
	"""
	dic = {}
	if len(txt) > 1:
		for line in txt.split("\n"):
			user, values = line.split("::")
			dic[user] = {}
			for camp in values.split("|"):
				key, value = camp.split(":")
				dic[user][key] = value
	return dic

def addUser(dic, user, values):
	if not dic.has_key(user):
		dic[user] = {}
		modifyUser(dic, user, values)
		print "\n[OK] S'ha creat l'usuari", user
		return True
	else:
		print "\n[FAIL] L'usuari ja existeix"
		return False

def delUser(dic, user):
	if dic.has_key(user):
		del dic[user]
		return True
	else:
		print "\n[FAIL] L'usuari no existeix"
		return False

def modifyUser(dic, user, values):
	if dic.has_key(user):
		dic[user] = values
		return True
	else:
		addUser(dic, user)
		return modifyUser(dic, user, values)

def desa(filename, dic):
	f = open(filename, "w")
	f.write(dictToStr(dic))
	f.close()
	print "\n[OK] S'han desat els canvis"

def obre(filename):
	f = open(filename)
	usuaris = f.read()
	f.close()
	dic = strToDict(usuaris)
	if len(dic) == 0:
		print "\n[OK] S'ha carregat el fitxer, però és buit"
	else:
		print "\n[OK] S'ha carregat el fitxer"
	return dic