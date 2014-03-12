from time import *

# El problema esta modificat de manera que puguis posar tantes vegades com vulguis el codi PUK, pero t'has d'esperar 2s entre intent i entent per evitar que es pugui endevinar facilment per forca bruta

def comprovarPin(pin):
	"""
	comprova si el pin introduit es = 1234
	>>> comprovarPin(12)
	False
	>>> comprovarPin(1234)
	True
	"""
	return pin == 1234

def comprovarPuk(puk):
	"""
	comprova si el puk introduit es = 123456789
	>>> comprovarPuk(12)
	False
	>>> comprovarPuk(123456789)
	True
	"""
	return puk == 123456789

intents_restants_pin = 3
intents_restants_puk = 5
while False == False:
	if intents_restants_pin > 0:
		if comprovarPin(input("Introdueix el PIN: ")):
			print "El codi PIN es correcte"
			break
		else:
			intents_restants_pin -= 1
			print "No es correcte, et queden", intents_restants_pin + 1
	elif intents_restants_puk > 0:
		if comprovarPuk(input("Introdueix el PUK: ")):
			print "El codi PUK es correcte"
			break
		else:
			#comento la seguent linia per evitar el bloqueig de la SIM	
			#intents_restants_puk -= 1
			print "El codi PUK no es correcte, et queden", intents_restants_puk + 1
			sleep(2)
	else:
		print "S'ha bloquejat la SIM"
		break