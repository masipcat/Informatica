def desa(self, fn):
	"""
	Desa la instancia del cotxe a un fitxer

	:param fn: Nom del fitxer
	:type fn: str
	"""
	f = open(fn + ".txt", "w")
	f.write(self._matricula + ":" + self._motor + ":" + self._color + ":" + self._model)
	f.close()

def recupera(self, fn):
	"""
	Recupera la instancia desada al fitxer fn

	:param fn: Nom del fitxer
	:type fn: str
	"""
	f = open(fn + ".txt", "r")
	content = f.read().split(":")
	f.close()
	self._matricula = content[0]
	self._motor = content[1]
	self._color = content[2]
	self._model = content[3]