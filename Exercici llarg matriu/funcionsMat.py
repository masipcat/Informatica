def matriuBuida(f, c):
	"""
	Retorna una matriu buida d'ordre fxc
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
	Retorna matiu d'ordre fxc amb les dades demanades a l'usuari
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
	Mostra per pantalla les dades d'una matriu de qualsevol ordre
	"""
	for f in m:
		for d in f:
			if len(str(d)) == 1:
				print d, "  ",
			else:
				print d, " ",
		print

def sumarMatriu(a, b):
	c=matriuBuida(3, 3)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i][j]+b[i][j]
	return c

#def determinantMatriu(m):

def multiplicarMatriu(a, b):
	c=matriuBuida(3, 3)
	for r in range(3):
		for t in range(3):
			for i in range(3):
				#c[r][]=a[r][i]*b[i][t]
				#return c
				pass