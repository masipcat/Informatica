#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def esQuadrada(matriu):
	"""
	Retorna True o False, segons si és una matriu quadrada o no (comprova si té el mateix número de files i columnes)
	Jordi Masip
	"""
	longitud = len(matriu)
	for row in matriu:
		if longitud != len(row):
			return False
	else:
		return True

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

def escriureMatriu(m):
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
	suma cada element de la matriu
	Felipe Arango
	"""
	c=matriuBuida(3, 3)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i][j]+b[i][j]
	return c

def sumaDiagonals(det, diagonal_invertida):
	"""
	Retorna la suma del producte de cada element de la diagonal.
	Jordi Masip
	"""
	# Es duplica el determinant original
	determinant = []
	determinant.extend(det)
	determinant.extend(det)

	valors = range(len(det))
	valors2 = valors
	invertir = 1

	# Si es volen calcular les diagonals invertides
	if diagonal_invertida:
		invertir = -1
		valors2.reverse() # Fer que 'start' vagi del valor gran al petit

	print "Start"

	resultat = 0
	for start in valors2:
		diagonal = 1
		for i in valors:
			# Multiplica cada element de la diagonal
			diagonal *= determinant[(i+start)*invertir][i]
			print diagonal
		resultat += diagonal # Suma la llista de diagonals
		print "---"
	return resultat

def determinantMatriu(determinant):
	"""
	Retorna un enter amb la diferència de cada diagonal. Només funciona amb determinants de rang 2 i 3
	Jordi Masip
	"""
	if esQuadrada(determinant):
		return sumaDiagonals(determinant, False) - sumaDiagonals(determinant, True)
	return False

def producte_matriu(matriu1, matriu2):
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