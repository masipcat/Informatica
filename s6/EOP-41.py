#!/usr/bin/env python
# -*- coding: utf-8 -*-

def detectaPatro(patro, adn):
	# Cerca a quina posició es troba el valor indefinit
	i, j, l = 0, 0, 0
	for c in patro:
		if c == "O":
			j=i
			l+=1
		else:
			i+=1

	# Es recorra l'adn cercant el patro
	k = 0
	while k < len(adn):
		if adn[k:k+j] == patro[0:j] and adn[k+j+l:] == patro[j+l:]:
			return adn[k:k+len(patro)]
		k+=1
	return False

# S'han d'expresar els valors desconeguts del patro com a "OO".
detactat = detectaPatro("ggttaacaaOOggtttca", "ggaattggcctggttaacaattggtttca")

if detactat != False:
	print "El resultat de cercar el patró és:", detactat
else:
	print "No s'ha trobat cap coincidència"