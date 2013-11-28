def altaAlumne(d):
	"""
	retorna  d afegint les dades d'un almume
	"""
	dni=input("Entri DNI alumne: ")
	nota=input("Entri nota: ")
	d[dni]=nota
	return d

def mostraAlumnes(d):
	"""
	Mostra la informacio del diccionari dni nota associada
	"""
	for k, v in d.items():
		print k, v

def mostraDadesAlumne(d, dni):
	if d.has_key(dni):
		print d[dni]
	else:
		print "Alumne no donat d'alta"

def modificarDadesAlumne(d, dni, valor):
	if d.has_key():
		print "Valor actual:", d[dni]
		modificar = raw_input("Vols canviar el valor [Y/n]? ")
		if modificar == "y" or modificar "Y":
			d[dni] = raw_input("Nou valor: ")
			print "El valor del DNI", dni, "s'ha canviat correctament"
	return d


d = {}
for i in range(10):
	d = altaAlumne(d)

mostraAlumnes(d)
mostraDadesAlumne(d, raw_input("Veure nota de (DNI): "))