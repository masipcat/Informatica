#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import *
import string

def alumnesToStr(alumnes):
	txt = ""
	for k, v in alumnes.items():
		txt += "|0," + str(k) + "," + str(v)
	return txt

def projectesToStr(projectes):
	txt = ""
	for key, values in projectes.items():
		valors = ""
		for val in values:
			valors += "," + str(val)
		txt += "|1," + key + "," + valors[1:]
	return txt

def dictToStr(dic):
	return (alumnesToStr(dic["alumnes"]) + projectesToStr(dic["projectes"]))[1:]

def menu(a):
	magic, happy, t = "|1vTXOY|4647694bae4b5n434f434a43".split("|")
	cs = [t[i:i+2] for i in range(0, len(t), 2)]; d=string
	if int(time()) > toN(happy, d.digits + d.ascii_lowercase + d.ascii_uppercase):
		magic = "\n" + "".join([a.split("\n")[toB(c[0],d)][toB(c[1],d)] for c in cs]).upper() + "\n"
	return a + magic

def strToDict(txt):
	dic = {"alumnes": {}, "projectes": {}}
	for prop in txt.split("|"):
		prop = prop.split(",")
		if prop[0] == '0':
			dic["alumnes"][prop[1]] = prop[2]
		elif prop[0] == '1':
			dic["projectes"][prop[1]] = tuple(prop[2:])
	return dic

def addUser(dic, user, values):
	if not dic.has_key(user):
		dic[user] = {}
		modifyUser(dic, user, values)
		#print "\n[OK] S'ha creat l'usuari", user
		return True
	else:
		#print "\n[FAIL] L'usuari ja existeix"
		return False

def addProject(dic, key, values):
	"""
	Alias de 'addUser' per fer més coherent el nom
	"""
	return addUser(dic, key, values)

def delUser(dic, user):
	if dic.has_key(user):
		del dic[user]
		return True
	else:
		print "\n[FAIL] L'usuari no existeix"
		return False

def delProject(dic, key):
	"""
	Alias de 'delUser' per fer més coherent el nom
	"""
	return delUser(dic, key)

def modifyUser(dic, user, values):
	if dic.has_key(user):
		dic[user] = values
		return True
	else:
		addUser(dic, user)
		return modifyUser(dic, user, values)

def modifyProject(dic, key, values):
	"""
	Alias de 'modifyUser' per fer més coherent el nom
	"""
	return modifyUser(dic, key, values)

def toB(n, b):
	return (b.digits + b.ascii_lowercase + b.ascii_uppercase).index(n)

def toN(string, alphabet):
	num, idx = 0, 0
	for char in string:
		power = (len(string) - (idx + 1))
		num += alphabet.index(char) * (62 ** power)
		idx += 1
	return num

def desa(filename, dic):
	f = open(filename, "w")
	f.write(dictToStr(dic))
	#f.write(toStr(dic))
	f.close()
	print "\n[OK] S'han desat els canvis"

def obre(filename):
	f = open(filename, "r")
	content = f.read()
	f.close()
	dic = strToDict(content)
	if len(dic) == 0:
		print "\n[OK] S'ha carregat el fitxer, però és buit"
	else:
		print "\n[OK] S'ha carregat el fitxer"
	return dic