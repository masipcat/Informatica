#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def esQuadrada(matriu):
	"""
	Retorna True o False, segons si és una matriu quadrada o no (comprova si té el mateix número de files i columnes)
	Jordi Masip
	>>> esQuadrada([[1,2],[1,3]])
	True
	>>> esQuadrada([[1,2]])
	False
	"""
	longitud = len(matriu)
	for row in matriu:
		if longitud != len(row):
			return False
	else:
		return True

def esBuida(m):
	return len(m) == 0

def matriuBuida(f, c):
	"""
	Retorna una matriu buida d'ordre fxc.
	Felipe Arango
	>>> matriuBuida(3, 3)
	[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	"""
	m = []
	for i in range(f):
		fila=[]
		for j in range(c):
			fila+=[0]
		m+=[fila]
	return m

def decodeMatriu(m):
	decodedMatrix = ""
	for row in m:
		decodedRow = ""
		for value in row:
			decodedRow += "," + str(value)
		decodedMatrix += "\n" + decodedRow[1:]
	return decodedMatrix[1:]

def encodeMatriu(txt):
	matriu = []
	for row in txt.split():
		matriu_row = []
		for value in row.split(","):
			matriu_row += [value]
		matriu += [matriu_row]
	return matriu

def llegeixMatriu(f, c):
	"""
	Retorna matriu d'ordre fxc amb les dades demanades a l'usuari.
	Felipe Arango
	"""
	print "introdueix dades matriu"
	m=matriuBuida(f,c)
	for i in range(f):
		print "Dades fila",i
		for j in range(c):
			print "Dades columnes",j
			m[i][j]=input()
	return m

def mostraMatriu(m):
	"""
	Mostra per pantalla les dades d'una matriu de qualsevol ordre.
	Felipe Arango
	"""
	for f in m:
		for d in f:
			if len(str(d)) == 1:
				print d, "  ",
			else:
				print d, " ",
		print

def sumarMatriu(a, b):
	"""
	Suma cada element de la matriu
	Felipe Arango
	"""
	matriu = matriuBuida(3, 3)
	for i in range(3):
		for j in range(3):
			matriu[i][j] = a[i][j] + b[i][j]
	return matriu

def determinantMatriu(m1):
	"""
	Retorna un enter amb la diferència de cada diagonal. Només funciona amb determinants de rang 2 i 3
	Felipe Arango
	"""
	diagonal1 = m1[0][1]*m1[1][2]*m1[2][0]+m1[0][2]*m1[1][0]*m1[2][1]+m1[0][0]*m1[1][1]*m1[2][2]
	diagonal2= m1[2][0]*m1[1][1]*m1[0][2]+m1[2][1]*m1[1][2]*m1[0][0]+m1[2][2]*m1[1][0]*m1[0][1]
	determinant = diagonal1-diagonal2
	return determinant

def producteMatriu(matriu1, matriu2):
	"""
	Retorna una matriu 2D resultat del producte de la primera amb la segona
	Jordi Masip
	"""
	
	m = len(matriu1) # Longitud d'una fila de la primera matriu
	n = len(matriu2) # Longitud de l'ultima columna de la segona matriu

	nova_matriu = []

	if n == m:
		for i, row in enumerate(matriu1):
			new_column = []
			for k in range(len(matriu2[-1])): # Realitza la multiplicacio per cada columna
				suma_productes = 0
				for j, value in enumerate(row): # Fa la suma del producte de cada fila
					suma_productes += value * matriu2[j][k]
				new_column += [suma_productes]
			nova_matriu += [new_column]
		return nova_matriu
	else:
		return False
