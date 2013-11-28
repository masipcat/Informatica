from math import ceil

def calcula_quadrant(a):
	"""
	retorna el quadrant en que es troba un angle en graus: => [0, 3]
	>>> calcula_quadrant(30)
	0
	>>> calcula_quadrant(120)
	1
	>>> calcula_quadrant(269)
	2
	>>> calcula_quadrant(350)
	3
	"""
	return int(ceil(a) % 360) / 90

angle = float(raw_input("Escriu un angle en graus: "))
quadrant = calcula_quadrant(angle)
if quadrant == 0:
   print "primer quadrant"
elif quadrant == 1:
   print "segon quadrant"
elif quadrant == 2:
   print "tercer quadrant"
elif quadrant == 3:
   print "quart quadrant"