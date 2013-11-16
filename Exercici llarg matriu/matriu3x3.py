#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from funcionsMat import *

def getOpcions():
	return ["Llegir matriu A", "Llegir matriu B", "Calcular matriu A+B", "Calcular A*B", "Calcular det(A)"]

def menu():
	print "Menú (-1 per sortir):"
	for i, text in enumerate(getOpcions()):
		print "\t", i, "-", text

menu()

opcio = 10 # Valor arbitrari
matriuA = []
matriuB = []

while opcio >= 0:
	opcio = input("Escull una opció: ")
	if opcio == 0:
		matriuA = llegeixMatriu(3,3)
		print "La matriu A s'ha definit correctament"
	elif opcio == 1:
		matriuB = llegeixMatriu(3,3)
		print "La matriu B s'ha definit correctament"
	elif opcio == 2:
		print "La suma de matrius A i B és:"
		escriureMatriu(sumarMatriu(matriuA, matriuB))
	elif opcio == 3:
		print "El producte de A i B és:"
		escriureMatriu(producteMatriu(matriuA, matriuB))
	elif opcio == 4:
		print "El det(A) és:", determinantMatriu(matriuA)
	elif opcio == -1:
		print "Passi-ho bé :)"
	else:
		print "Opció incorrecte :(\nHas d'escriure un valor entre 0 i", len(getOpcions()) - 1
