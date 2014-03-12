#!/usr/bin/python
# -*- coding: utf-8 -*-

def esPalindroma(s):
	"""
	Retorna True o False segons si és palíndroma o no
	>>> esPalindroma("anna")
	True
	>>> esPalindroma("hola")
	False
	"""
	return s == s[::-1]