def esDobleDeSenar(n):
	"""
	retorna True si n es el doble d'un nombre senar
	>>> esDobleDeSenar(14)
	True
	>>> esDobleDeSenar(8)
	False
	>>> esDobleDeSenar(0)
	False
	"""
	return (n/2)%2 != 0