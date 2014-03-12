from math import ceil # ceil arrodoneix per excés

def calcula_quadrant(a):
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